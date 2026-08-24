#!/usr/bin/env python3
"""Sweep Inkscape multi-scan trace parameters and rank rendered SVG fidelity."""

from __future__ import annotations

import argparse
import base64
import csv
import itertools
import os
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image

from reference_fidelity import calculate_metrics


SVG_NS = "http://www.w3.org/2000/svg"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
ET.register_namespace("", SVG_NS)
ET.register_namespace("inkscape", INKSCAPE_NS)


def find_inkscape(explicit: Path | None) -> Path:
    if explicit:
        if explicit.exists():
            return explicit
        raise ValueError(f"Inkscape executable not found: {explicit}")
    discovered = shutil.which("inkscape.com") or shutil.which("inkscape")
    if discovered:
        return Path(discovered)
    for env_name, suffix in (
        ("ProgramFiles", ("Inkscape", "bin", "inkscape.com")),
        ("LOCALAPPDATA", ("Programs", "Inkscape", "bin", "inkscape.com")),
    ):
        base = os.environ.get(env_name)
        if base:
            candidate = Path(base).joinpath(*suffix)
            if candidate.exists():
                return candidate
    raise ValueError("Inkscape was not found. Pass --inkscape with the executable path.")


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def float_tag(value: float) -> str:
    return f"{value:g}".replace(".", "p")


def make_input_svg(reference: Path, output: Path) -> tuple[int, int]:
    with Image.open(reference) as image:
        width, height = image.size
    encoded = base64.b64encode(reference.read_bytes()).decode("ascii")
    root = ET.Element(
        f"{{{SVG_NS}}}svg",
        {"width": str(width), "height": str(height), "viewBox": f"0 0 {width} {height}"},
    )
    ET.SubElement(
        root,
        f"{{{SVG_NS}}}image",
        {
            "x": "0",
            "y": "0",
            "width": str(width),
            "height": str(height),
            "preserveAspectRatio": "none",
            "href": f"data:image/png;base64,{encoded}",
        },
    )
    ET.ElementTree(root).write(output, encoding="utf-8", xml_declaration=True)
    return width, height


def remove_images(source: Path, output: Path) -> int:
    tree = ET.parse(source)
    root = tree.getroot()
    removed = 0
    for parent in root.iter():
        for child in list(parent):
            if child.tag.split("}")[-1] == "image":
                parent.remove(child)
                removed += 1
    paths = [child for child in root.iter() if child.tag.split("}")[-1] == "path"]
    path_count = len(paths)
    if removed == 0 or path_count == 0:
        raise ValueError(
            f"Trace output was invalid: removed_images={removed}, paths={path_count}"
        )
    groups = [child for child in root.iter() if child.tag.split("}")[-1] == "g"]
    artwork = max(groups, key=lambda group: len(list(group.iter(f"{{{SVG_NS}}}path"))))
    artwork.set("id", "editable-vector-artwork")
    artwork.set(f"{{{INKSCAPE_NS}}}groupmode", "layer")
    artwork.set(f"{{{INKSCAPE_NS}}}label", "Editable vector artwork")
    for index, path in enumerate(artwork.iter(f"{{{SVG_NS}}}path"), start=1):
        path.set("id", f"vector-color-path-{index:02d}")
    root.set("data-raster-images", "0")
    root.set("data-editable-vector", "true")
    tree.write(output, encoding="utf-8", xml_declaration=True)
    return path_count


def load_render_rgb(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, "white")
        background.alpha_composite(rgba)
        return np.asarray(background.convert("RGB"))


def run_checked(command: list[str]) -> None:
    subprocess.run(
        command,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--inkscape", type=Path)
    parser.add_argument("--scans", type=int, nargs="+", default=[24, 32, 40, 48])
    parser.add_argument("--speckles", type=int, nargs="+", default=[0])
    parser.add_argument("--smooth-corners", type=float, nargs="+", default=[0.3])
    parser.add_argument("--optimize", type=float, nargs="+", default=[0.08])
    parser.add_argument("--smooth", action="store_true")
    parser.add_argument("--no-stack", action="store_true")
    parser.add_argument("--remove-background", action="store_true")
    parser.add_argument("--max-variants", type=int, default=48)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--keep-raw", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        inkscape = find_inkscape(args.inkscape)
        args.output_dir.mkdir(parents=True, exist_ok=True)
        input_svg = args.output_dir / "_trace_input.svg"
        width, _ = make_input_svg(args.reference, input_svg)
        with Image.open(args.reference) as image:
            reference = np.asarray(image.convert("RGB"))

        configs = list(
            itertools.product(
                args.scans, args.speckles, args.smooth_corners, args.optimize
            )
        )
        if len(configs) > args.max_variants:
            raise ValueError(
                f"Sweep expands to {len(configs)} variants; max is {args.max_variants}"
            )

        rows: list[dict[str, object]] = []
        for scans, speckles, corners, optimize in configs:
            tag = (
                f"s{scans}_sm{int(args.smooth)}_st{int(not args.no_stack)}_"
                f"rb{int(args.remove_background)}_sp{speckles}_"
                f"sc{float_tag(corners)}_op{float_tag(optimize)}"
            )
            raw_svg = args.output_dir / f"{tag}_raw.svg"
            clean_svg = args.output_dir / f"{tag}.svg"
            png = args.output_dir / f"{tag}.png"
            for stale in (raw_svg, clean_svg, png):
                if stale.exists():
                    stale.unlink()
            started = time.time()
            try:
                output_action = raw_svg.resolve().as_posix()
                action = (
                    "select-all;"
                    f"object-trace:{scans},{bool_text(args.smooth)},"
                    f"{bool_text(not args.no_stack)},{bool_text(args.remove_background)},"
                    f"{speckles},{corners},{optimize};"
                    f"export-type:svg;export-filename:{output_action};export-do;quit-immediate"
                )
                run_checked(
                    [str(inkscape), str(input_svg), "--batch-process", f"--actions={action}"]
                )
                path_count = remove_images(raw_svg, clean_svg)
                if not args.keep_raw:
                    raw_svg.unlink()
                run_checked(
                    [
                        str(inkscape),
                        str(clean_svg),
                        "--export-type=png",
                        f"--export-filename={png}",
                        f"--export-width={width}",
                    ]
                )
                candidate = load_render_rgb(png)
                metrics = calculate_metrics(reference, candidate)
                row: dict[str, object] = {
                    "tag": tag,
                    **metrics,
                    "svg_bytes": clean_svg.stat().st_size,
                    "path_count": path_count,
                    "seconds": time.time() - started,
                    "svg": str(clean_svg.resolve()),
                    "png": str(png.resolve()),
                    "error": "",
                }
            except (OSError, ValueError, subprocess.CalledProcessError, ET.ParseError) as exc:
                row = {
                    "tag": tag,
                    "ssim": -1.0,
                    "mae": float("inf"),
                    "psnr": -1.0,
                    "exact_pixel_percent": 0.0,
                    "svg_bytes": 0,
                    "path_count": 0,
                    "seconds": time.time() - started,
                    "svg": str(clean_svg.resolve()),
                    "png": str(png.resolve()),
                    "error": str(exc),
                }
            rows.append(row)
            print(
                f"{tag}\tSSIM={row['ssim']:.6f}\tMAE={row['mae']:.3f}\t"
                f"paths={row['path_count']}\tsec={row['seconds']:.1f}",
                flush=True,
            )

        rows.sort(key=lambda row: (-float(row["ssim"]), float(row["mae"])))
        csv_path = args.output_dir / "results.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print("TOP")
        for row in rows[: args.top]:
            print(f"{row['tag']}\tSSIM={row['ssim']:.6f}\tMAE={row['mae']:.3f}")
        print(f"results: {csv_path.resolve()}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
