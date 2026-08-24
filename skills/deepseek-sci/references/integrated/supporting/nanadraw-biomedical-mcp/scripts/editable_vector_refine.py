#!/usr/bin/env python3
"""Refine and audit pure-vector SVG reconstructions with editable text."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SVG_NS = "http://www.w3.org/2000/svg"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
ET.register_namespace("", SVG_NS)
ET.register_namespace("inkscape", INKSCAPE_NS)


def tag(name: str) -> str:
    return f"{{{SVG_NS}}}{name}"


PATH_TOKEN_RE = re.compile(
    r"[MmLlHhVvCcZz]|[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
)


@dataclass
class ParsedSubpath:
    commands: list[str]
    points: list[tuple[float, float]]

    @property
    def bbox(self) -> tuple[float, float, float, float]:
        xs = [point[0] for point in self.points]
        ys = [point[1] for point in self.points]
        return min(xs), min(ys), max(xs), max(ys)

    def serialize(self) -> str:
        return " ".join(self.commands)


def number(value: float) -> str:
    rounded = round(value, 4)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.4f}".rstrip("0").rstrip(".")


def parse_subpaths(data: str) -> list[ParsedSubpath]:
    tokens = PATH_TOKEN_RE.findall(data)
    subpaths: list[ParsedSubpath] = []
    current: ParsedSubpath | None = None
    current_x = current_y = 0.0
    start_x = start_y = 0.0
    command: str | None = None
    index = 0

    while index < len(tokens):
        token = tokens[index]
        if token.isalpha():
            command = token
            index += 1
            if command in "Zz":
                if current is not None:
                    current.commands.append("Z")
                    current_x, current_y = start_x, start_y
                command = None
                continue
        if command is None:
            continue

        relative = command.islower()
        upper = command.upper()
        count = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6}.get(upper)
        if count is None or index + count > len(tokens):
            raise ValueError(f"Unsupported or incomplete SVG path command: {command}")
        values = [float(value) for value in tokens[index:index + count]]
        index += count

        if upper == "M":
            x = values[0] + (current_x if relative else 0.0)
            y = values[1] + (current_y if relative else 0.0)
            if current is not None:
                subpaths.append(current)
            current = ParsedSubpath([f"M {number(x)},{number(y)}"], [(x, y)])
            current_x, current_y = x, y
            start_x, start_y = x, y
            command = "l" if relative else "L"
            continue

        if current is None:
            raise ValueError("SVG path starts without a moveto command")
        if upper == "L":
            x = values[0] + (current_x if relative else 0.0)
            y = values[1] + (current_y if relative else 0.0)
            current.commands.append(f"L {number(x)},{number(y)}")
            current.points.append((x, y))
            current_x, current_y = x, y
        elif upper == "H":
            x = values[0] + (current_x if relative else 0.0)
            current.commands.append(f"L {number(x)},{number(current_y)}")
            current.points.append((x, current_y))
            current_x = x
        elif upper == "V":
            y = values[0] + (current_y if relative else 0.0)
            current.commands.append(f"L {number(current_x)},{number(y)}")
            current.points.append((current_x, y))
            current_y = y
        elif upper == "C":
            x1 = values[0] + (current_x if relative else 0.0)
            y1 = values[1] + (current_y if relative else 0.0)
            x2 = values[2] + (current_x if relative else 0.0)
            y2 = values[3] + (current_y if relative else 0.0)
            x = values[4] + (current_x if relative else 0.0)
            y = values[5] + (current_y if relative else 0.0)
            current.commands.append(
                f"C {number(x1)},{number(y1)} {number(x2)},{number(y2)} "
                f"{number(x)},{number(y)}"
            )
            current.points.extend(((x1, y1), (x2, y2), (x, y)))
            current_x, current_y = x, y

    if current is not None:
        subpaths.append(current)
    return subpaths


def find_artwork(root: ET.Element, artwork_id: str) -> ET.Element:
    artwork = root.find(f".//{tag('g')}[@id='{artwork_id}']")
    if artwork is None:
        raise ValueError(f"Artwork layer not found: {artwork_id}")
    return artwork


def parent_map(root: ET.Element) -> dict[ET.Element, ET.Element]:
    return {child: parent for parent in root.iter() for child in list(parent)}


def artwork_paths(artwork: ET.Element) -> list[ET.Element]:
    return list(artwork.iter(tag("path")))


def load_regions(path: Path) -> list[tuple[float, float, float, float]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("regions", payload) if isinstance(payload, dict) else payload
    if not isinstance(rows, list):
        raise ValueError("Region JSON must be a list or contain a regions list")
    regions: list[tuple[float, float, float, float]] = []
    for row in rows:
        if isinstance(row, dict):
            values = (row["x"], row["y"], row["width"], row["height"])
        else:
            values = row
        if len(values) != 4:
            raise ValueError(f"Invalid region: {row}")
        x, y, width, height = (float(value) for value in values)
        regions.append((x, y, width, height))
    return regions


def inside_region(
    bbox: tuple[float, float, float, float],
    regions: list[tuple[float, float, float, float]],
    tolerance: float,
) -> bool:
    x1, y1, x2, y2 = bbox
    return any(
        x1 >= rx - tolerance
        and y1 >= ry - tolerance
        and x2 <= rx + width + tolerance
        and y2 <= ry + height + tolerance
        for rx, ry, width, height in regions
    )


def remove_near_white_page_paths(artwork: ET.Element) -> int:
    removed = 0
    parents = parent_map(artwork)
    for path in artwork_paths(artwork):
        style = path.get("style", "")
        match = re.search(r"(?:^|;)fill:([^;]+)", style)
        fill = (path.get("fill") or (match.group(1) if match else "")).lower()
        if fill in {"#ffffff", "#fefefe", "#fdfdfd"} and len(path.get("d", "")) < 120:
            parents[path].remove(path)
            removed += 1
    return removed


def command_remove_text(args: argparse.Namespace) -> int:
    tree = ET.parse(args.input)
    root = tree.getroot()
    artwork = find_artwork(root, args.artwork_id)
    regions = load_regions(args.regions)
    if args.drop_page_background:
        remove_near_white_page_paths(artwork)

    removed = 0
    for path in artwork_paths(artwork):
        parsed = parse_subpaths(path.get("d", ""))
        kept = []
        for subpath in parsed:
            if inside_region(subpath.bbox, regions, args.tolerance):
                removed += 1
            else:
                kept.append(subpath)
        path.set("d", " ".join(subpath.serialize() for subpath in kept))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(args.output, encoding="utf-8", xml_declaration=True)
    print(json.dumps({"output": str(args.output.resolve()), "removed_subpaths": removed}))
    return 0


def command_hybridize(args: argparse.Namespace) -> int:
    detail_tree = ET.parse(args.detail)
    detail_root = detail_tree.getroot()
    detail_artwork = find_artwork(detail_root, args.artwork_id)
    outline_root = ET.parse(args.outline).getroot()
    outline_artwork = find_artwork(outline_root, args.artwork_id)
    detail_paths = artwork_paths(detail_artwork)
    outline_paths = artwork_paths(outline_artwork)
    if args.remove_detail_tail < 1 or args.remove_detail_tail > len(detail_paths):
        raise ValueError("remove-detail-tail is outside the available detail path count")
    if args.append_outline_tail < 1 or args.append_outline_tail > len(outline_paths):
        raise ValueError("append-outline-tail is outside the available outline path count")

    parents = parent_map(detail_artwork)
    insertion_parent = parents[detail_paths[-1]]
    for path in detail_paths[-args.remove_detail_tail:]:
        parents[path].remove(path)
    for path in outline_paths[-args.append_outline_tail:]:
        insertion_parent.append(deepcopy(path))

    final_paths = artwork_paths(detail_artwork)
    for index, path in enumerate(final_paths, start=1):
        path.set("id", f"vector-color-path-{index:02d}")
    detail_root.set("data-color-paths", str(len(final_paths)))
    detail_root.set("data-detail-source", str(args.detail.resolve()))
    detail_root.set("data-outline-source", str(args.outline.resolve()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    detail_tree.write(args.output, encoding="utf-8", xml_declaration=True)
    print(json.dumps({"output": str(args.output.resolve()), "color_paths": len(final_paths)}))
    return 0


def audit_svg(path: Path, artwork_id: str) -> dict[str, Any]:
    raw = path.read_bytes()
    root = ET.fromstring(raw)
    artwork = find_artwork(root, artwork_id)
    color_paths = artwork_paths(artwork)
    ids = [path.get("id") for path in color_paths]
    expected = [f"vector-color-path-{index:02d}" for index in range(1, len(ids) + 1)]
    layers = [
        {
            "id": group.get("id"),
            "label": group.get(f"{{{INKSCAPE_NS}}}label"),
        }
        for group in root.findall(f"./{tag('g')}")
    ]
    return {
        "svg": str(path.resolve()),
        "bytes": len(raw),
        "images": len(root.findall(f".//{tag('image')}")),
        "masks": len(root.findall(f".//{tag('mask')}")),
        "clip_paths": len(root.findall(f".//{tag('clipPath')}")),
        "embedded_rasters": len(re.findall(br"data:image/(?:png|jpeg|webp)", raw)),
        "color_paths": len(color_paths),
        "color_path_ids_continuous": ids == expected,
        "all_paths": len(root.findall(f".//{tag('path')}")),
        "live_text": len(root.findall(f".//{tag('text')}")),
        "rectangles": len(root.findall(f".//{tag('rect')}")),
        "layers": layers,
    }


def command_audit(args: argparse.Namespace) -> int:
    result = audit_svg(args.svg, args.artwork_id)
    print(json.dumps(result, indent=2))
    if args.strict_pure_vector:
        forbidden = result["images"] + result["masks"] + result["clip_paths"] + result["embedded_rasters"]
        if forbidden or not result["color_path_ids_continuous"]:
            return 1
    if args.require_live_text and result["live_text"] == 0:
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    remove = subparsers.add_parser(
        "remove-text-subpaths",
        help="Remove traced glyph subpaths while preserving paths that cross text regions",
    )
    remove.add_argument("--input", type=Path, required=True)
    remove.add_argument("--regions", type=Path, required=True)
    remove.add_argument("--output", type=Path, required=True)
    remove.add_argument("--artwork-id", default="editable-vector-artwork")
    remove.add_argument("--tolerance", type=float, default=2.0)
    remove.add_argument("--drop-page-background", action="store_true")
    remove.set_defaults(func=command_remove_text)

    hybrid = subparsers.add_parser(
        "hybridize",
        help="Use high-scan detail paths with a stable low-scan outline tail",
    )
    hybrid.add_argument("--detail", type=Path, required=True)
    hybrid.add_argument("--outline", type=Path, required=True)
    hybrid.add_argument("--output", type=Path, required=True)
    hybrid.add_argument("--artwork-id", default="editable-vector-artwork")
    hybrid.add_argument("--remove-detail-tail", type=int, default=1)
    hybrid.add_argument("--append-outline-tail", type=int, default=1)
    hybrid.set_defaults(func=command_hybridize)

    audit = subparsers.add_parser("audit", help="Audit SVG purity and editability")
    audit.add_argument("--svg", type=Path, required=True)
    audit.add_argument("--artwork-id", default="editable-vector-artwork")
    audit.add_argument("--strict-pure-vector", action="store_true")
    audit.add_argument("--require-live-text", action="store_true")
    audit.set_defaults(func=command_audit)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError, KeyError, ET.ParseError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
