#!/usr/bin/env python3
"""Deterministic QA and delivery helpers for reference-guided figures."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import numpy as np
    from PIL import Image
    from skimage.metrics import peak_signal_noise_ratio, structural_similarity
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Run with the NanaDraw .venv or install pillow, numpy, and scikit-image."
    ) from exc


SVG_NS = "http://www.w3.org/2000/svg"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
XLINK_NS = "http://www.w3.org/1999/xlink"

ET.register_namespace("", SVG_NS)
ET.register_namespace("inkscape", INKSCAPE_NS)
ET.register_namespace("xlink", XLINK_NS)


def load_rgb(path: Path) -> Image.Image:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, "white")
        background.alpha_composite(rgba)
        return background.convert("RGB")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def calculate_metrics(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    if reference.shape != candidate.shape:
        raise ValueError(f"Shape mismatch: {reference.shape} != {candidate.shape}")
    reference_i16 = reference.astype(np.int16)
    candidate_i16 = candidate.astype(np.int16)
    mae = float(np.abs(candidate_i16 - reference_i16).mean())
    exact = float((candidate == reference).all(axis=2).mean() * 100.0)
    ssim = float(
        structural_similarity(reference, candidate, channel_axis=2, data_range=255)
    )
    mse = float(np.square(candidate_i16 - reference_i16, dtype=np.float64).mean())
    psnr = math.inf if mse == 0.0 else float(
        peak_signal_noise_ratio(reference, candidate, data_range=255)
    )
    return {
        "ssim": ssim,
        "mae": mae,
        "psnr": psnr,
        "exact_pixel_percent": exact,
    }


def normalized_candidate(
    candidate: Image.Image, reference_size: tuple[int, int], resize: bool
) -> tuple[Image.Image, bool]:
    if candidate.size == reference_size:
        return candidate, False
    if not resize:
        raise ValueError(
            f"Dimension mismatch: candidate={candidate.size}, reference={reference_size}"
        )
    return candidate.resize(reference_size, Image.Resampling.LANCZOS), True


def compare_paths(reference_path: Path, candidate_path: Path, resize: bool) -> dict[str, Any]:
    reference_image = load_rgb(reference_path)
    candidate_original = load_rgb(candidate_path)
    candidate_image, resized = normalized_candidate(
        candidate_original, reference_image.size, resize
    )
    reference = np.asarray(reference_image)
    candidate = np.asarray(candidate_image)
    result: dict[str, Any] = {
        "reference": str(reference_path.resolve()),
        "candidate": str(candidate_path.resolve()),
        "reference_size": list(reference_image.size),
        "candidate_size": list(candidate_original.size),
        "candidate_resized_for_comparison": resized,
        "reference_sha256": sha256(reference_path),
        "candidate_sha256": sha256(candidate_path),
        "byte_identical": reference_path.read_bytes() == candidate_path.read_bytes(),
    }
    result.update(calculate_metrics(reference, candidate))
    return result


def parse_boundaries(value: str) -> list[int]:
    try:
        boundaries = [int(item.strip()) for item in value.split(",")]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Boundaries must be comma-separated integers") from exc
    if len(boundaries) < 2 or boundaries != sorted(boundaries):
        raise argparse.ArgumentTypeError("Boundaries must contain increasing coordinates")
    if len(set(boundaries)) != len(boundaries):
        raise argparse.ArgumentTypeError("Boundaries must not contain duplicates")
    return boundaries


def json_safe(value: Any) -> Any:
    if isinstance(value, float) and not math.isfinite(value):
        return "infinity"
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def print_result(result: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(json_safe(result), indent=2, ensure_ascii=True))
        return
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {json_safe(value)}")
        return
    print(result)


def command_compare(args: argparse.Namespace) -> int:
    result = compare_paths(args.reference, args.candidate, not args.no_resize)
    print_result(result, args.json)
    return 0


def command_rank_panels(args: argparse.Namespace) -> int:
    reference_image = load_rgb(args.reference)
    reference = np.asarray(reference_image)
    boundaries = args.boundaries
    if boundaries[0] != 0 or boundaries[-1] != reference_image.width:
        raise ValueError(
            f"Boundaries must start at 0 and end at reference width {reference_image.width}"
        )

    ranked: list[list[dict[str, Any]]] = [[] for _ in range(len(boundaries) - 1)]
    for candidate_path in args.candidates:
        candidate_original = load_rgb(candidate_path)
        candidate_image, resized = normalized_candidate(
            candidate_original, reference_image.size, not args.no_resize
        )
        candidate = np.asarray(candidate_image)
        for panel_index, (x0, x1) in enumerate(zip(boundaries, boundaries[1:])):
            metrics = calculate_metrics(reference[:, x0:x1], candidate[:, x0:x1])
            ranked[panel_index].append(
                {
                    "candidate": str(candidate_path.resolve()),
                    "candidate_resized_for_comparison": resized,
                    "x0": x0,
                    "x1": x1,
                    **metrics,
                }
            )

    result = []
    for panel_index, rows in enumerate(ranked, start=1):
        rows.sort(key=lambda item: (-item["ssim"], item["mae"]))
        result.append({"panel": panel_index, "ranking": rows[: args.top]})
    print_result(result, args.json)
    return 0


def local_name(element: ET.Element) -> str:
    return element.tag.split("}")[-1]


def numeric_dimension(value: str | None) -> float | None:
    if value is None:
        return None
    match = re.match(r"^\s*([0-9]+(?:\.[0-9]+)?)", value)
    return float(match.group(1)) if match else None


def validate_svg_size(root: ET.Element, width: int, height: int) -> None:
    svg_width = numeric_dimension(root.get("width"))
    svg_height = numeric_dimension(root.get("height"))
    if svg_width is not None and abs(svg_width - width) > 0.01:
        raise ValueError(f"Vector width {svg_width} does not match reference width {width}")
    if svg_height is not None and abs(svg_height - height) > 0.01:
        raise ValueError(f"Vector height {svg_height} does not match reference height {height}")


def command_make_layered_svg(args: argparse.Namespace) -> int:
    reference_image = load_rgb(args.reference)
    width, height = reference_image.size
    tree = ET.parse(args.vector)
    root = tree.getroot()
    validate_svg_size(root, width, height)
    if any(element.get("id") == "reference-locked-exact-appearance" for element in root.iter()):
        raise ValueError("The vector already contains a reference-locked layer")

    root.set("width", str(width))
    root.set("height", str(height))
    root.set("viewBox", f"0 0 {width} {height}")
    movable = [
        child
        for child in list(root)
        if local_name(child) not in {"defs", "metadata", "namedview", "title", "desc"}
    ]
    for child in movable:
        root.remove(child)

    vector_layer = ET.SubElement(
        root,
        f"{{{SVG_NS}}}g",
        {
            "id": "editable-vector-reconstruction",
            f"{{{INKSCAPE_NS}}}groupmode": "layer",
            f"{{{INKSCAPE_NS}}}label": "Editable vector reconstruction",
        },
    )
    for child in movable:
        vector_layer.append(child)

    reference_layer = ET.SubElement(
        root,
        f"{{{SVG_NS}}}g",
        {
            "id": "reference-locked-exact-appearance",
            f"{{{INKSCAPE_NS}}}groupmode": "layer",
            f"{{{INKSCAPE_NS}}}label": "Reference-locked exact appearance",
        },
    )
    encoded = base64.b64encode(args.reference.read_bytes()).decode("ascii")
    ET.SubElement(
        reference_layer,
        f"{{{SVG_NS}}}image",
        {
            "id": "exact-reference-image",
            "x": "0",
            "y": "0",
            "width": str(width),
            "height": str(height),
            "preserveAspectRatio": "none",
            "href": f"data:image/png;base64,{encoded}",
            "style": "image-rendering:auto",
        },
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(args.output, encoding="utf-8", xml_declaration=True)
    result = {
        "output": str(args.output.resolve()),
        "reference_sha256": sha256(args.reference),
        "layers": [
            "Editable vector reconstruction",
            "Reference-locked exact appearance",
        ],
    }
    print_result(result, args.json)
    return 0


def prefix_ids(element: ET.Element, prefix: str) -> None:
    mapping: dict[str, str] = {}
    for index, child in enumerate(element.iter()):
        old_id = child.get("id")
        if old_id:
            new_id = f"{prefix}-{index}-{old_id}"
            mapping[old_id] = new_id
            child.set("id", new_id)
    if not mapping:
        return
    for child in element.iter():
        for key, value in list(child.attrib.items()):
            for old_id, new_id in mapping.items():
                value = value.replace(f"url(#{old_id})", f"url(#{new_id})")
                if value == f"#{old_id}":
                    value = f"#{new_id}"
            child.set(key, value)


def command_assemble_panels(args: argparse.Namespace) -> int:
    reference_image = load_rgb(args.reference)
    width, height = reference_image.size
    boundaries = args.boundaries
    if len(args.vectors) + 1 != len(boundaries):
        raise ValueError("The number of vectors must equal the number of panel intervals")
    if boundaries[0] != 0 or boundaries[-1] != width:
        raise ValueError(f"Boundaries must start at 0 and end at reference width {width}")

    root = ET.Element(
        f"{{{SVG_NS}}}svg",
        {
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
            "version": "1.1",
            "id": "panel-specific-vector-composite",
        },
    )
    defs = ET.SubElement(root, f"{{{SVG_NS}}}defs")
    sources: list[tuple[ET.Element, list[ET.Element]]] = []
    for panel_index, vector_path in enumerate(args.vectors, start=1):
        source_root = ET.parse(vector_path).getroot()
        validate_svg_size(source_root, width, height)
        source_defs = [child for child in list(source_root) if local_name(child) == "defs"]
        visuals = [
            child
            for child in list(source_root)
            if local_name(child) not in {"defs", "metadata", "namedview", "title", "desc"}
        ]
        bundle = ET.Element(f"{{{SVG_NS}}}g")
        for source_def in source_defs:
            for child in list(source_def):
                bundle.append(deepcopy(child))
        visual_copies = [deepcopy(child) for child in visuals]
        for child in visual_copies:
            bundle.append(child)
        prefix_ids(bundle, f"panel{panel_index}")
        bundled_children = list(bundle)
        defs_count = sum(len(list(source_def)) for source_def in source_defs)
        for child in bundled_children[:defs_count]:
            bundle.remove(child)
            defs.append(child)
        sources.append((bundle, visual_copies))

    for panel_index, ((x0, x1), (bundle, _)) in enumerate(
        zip(zip(boundaries, boundaries[1:]), sources), start=1
    ):
        clip_id = f"panel-clip-{panel_index}"
        clip = ET.SubElement(
            defs,
            f"{{{SVG_NS}}}clipPath",
            {"id": clip_id, "clipPathUnits": "userSpaceOnUse"},
        )
        ET.SubElement(
            clip,
            f"{{{SVG_NS}}}rect",
            {"x": str(x0), "y": "0", "width": str(x1 - x0), "height": str(height)},
        )
        wrapper = ET.SubElement(
            root,
            f"{{{SVG_NS}}}g",
            {"id": f"panel-{panel_index}", "clip-path": f"url(#{clip_id})"},
        )
        for child in list(bundle):
            bundle.remove(child)
            wrapper.append(child)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(args.output, encoding="utf-8", xml_declaration=True)
    print_result(
        {"output": str(args.output.resolve()), "panels": len(args.vectors)}, args.json
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    compare = subparsers.add_parser("compare", help="Compare one candidate image to a reference")
    compare.add_argument("--reference", type=Path, required=True)
    compare.add_argument("--candidate", type=Path, required=True)
    compare.add_argument("--no-resize", action="store_true")
    compare.add_argument("--json", action="store_true")
    compare.set_defaults(func=command_compare)

    rank = subparsers.add_parser("rank-panels", help="Rank candidates independently per panel")
    rank.add_argument("--reference", type=Path, required=True)
    rank.add_argument("--boundaries", type=parse_boundaries, required=True)
    rank.add_argument("--candidates", type=Path, nargs="+", required=True)
    rank.add_argument("--top", type=int, default=3)
    rank.add_argument("--no-resize", action="store_true")
    rank.add_argument("--json", action="store_true")
    rank.set_defaults(func=command_rank_panels)

    layered = subparsers.add_parser(
        "make-layered-svg", help="Add an exact reference layer above an editable vector layer"
    )
    layered.add_argument("--reference", type=Path, required=True)
    layered.add_argument("--vector", type=Path, required=True)
    layered.add_argument("--output", type=Path, required=True)
    layered.add_argument("--json", action="store_true")
    layered.set_defaults(func=command_make_layered_svg)

    assemble = subparsers.add_parser(
        "assemble-panels", help="Clip panel-specific vector winners into one SVG"
    )
    assemble.add_argument("--reference", type=Path, required=True)
    assemble.add_argument("--boundaries", type=parse_boundaries, required=True)
    assemble.add_argument("--vectors", type=Path, nargs="+", required=True)
    assemble.add_argument("--output", type=Path, required=True)
    assemble.add_argument("--json", action="store_true")
    assemble.set_defaults(func=command_assemble_panels)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
