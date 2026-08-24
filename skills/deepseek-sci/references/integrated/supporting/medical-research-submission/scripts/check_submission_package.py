#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_submission_package.py — 投稿包校验脚本（medical-research-submission 插件 S7 投稿门）

校验投稿包目录是否达到"可直接投稿"标准：
  1. 必需文件齐全（manuscript / cover_letter / checklist / 图表 / 参考文献）
  2. 图片格式与分辨率（位图 >=300 dpi；TIFF/PNG/JPEG 解析头部 DPI）
  3. 文件大小合理性（单文件 >20 MB 告警）
  4. 可选文件缺失告警（title page / highlights / COI / supplementary / 修回信）

用法：
  python check_submission_package.py <submission_dir> [--strict] [--json]

退出码：0 = 无 FAIL；1 = 存在 FAIL（--strict 时可选缺失也计 FAIL）。
纯标准库实现，无第三方依赖。
"""

import argparse
import json
import os
import re
import struct
import sys

DPI_THRESHOLD = 300
MAX_FILE_MB = 20

# ---------------------------------------------------------------- 名称匹配

def _has(name, *keys):
    n = name.lower()
    return any(k in n for k in keys)

def classify(path):
    """返回 (类别, 匹配到的关键词)。类别见 REQUIRED/OPTIONAL 键。"""
    name = os.path.basename(path)
    dirname = os.path.basename(os.path.dirname(path)).lower()
    n = name.lower()
    ext = os.path.splitext(n)[1]
    # 目录级识别优先（tables/ supplementary/ 等）
    if dirname in ("tables", "table"):
        return "tables"
    if dirname in ("supplementary", "supplement", "supplements", "appendix",
                   "appendices", "esm", "sdc", "online-only", "onlineonly"):
        return "supplementary"
    if _has(n, "cover", "covering") and _has(n, "letter", "ltr"):
        return "cover_letter"
    if _has(n, "title", "titlepage") and _has(n, "page"):
        return "title_page"
    if _has(n, "highlight"):
        return "highlights"
    if _has(n, "checklist") or _has(n, "strobe", "consort", "prisma",
                                      "tripod", "record", "stard", "arrive", "cheers"):
        return "checklist"
    if _has(n, "icmje", "coi", "conflict"):
        return "coi"
    if _has(n, "ethics", "irb", "approval"):
        return "ethics"
    if _has(n, "registr", "prospero", "clinicaltrials", "chictr"):
        return "registration"
    if _has(n, "response", "rebuttal", "point-by-point", "point by point"):
        return "response_letter"
    if _has(n, "etable", "efigure", "supplement", "appendix", "esm_", "sdc_",
              "online supplementary", "online only"):
        return "supplementary"
    if _has(n, "table"):
        return "tables"
    if _has(n, "manuscript", "main text", "maintext", "main_text", "ms_", "paper_"):
        return "manuscript"
    if ext in (".docx", ".doc", ".tex", ".rtf", ".pdf", ".md"):
        return "manuscript_fallback"
    if ext in (".bib", ".ris", ".enw", ".enl"):
        return "references"
    return None

def is_image(name):
    return os.path.splitext(name)[1].lower() in (".tif", ".tiff", ".png", ".jpg",
                                                  ".jpeg", ".eps", ".pdf")

# ---------------------------------------------------------------- DPI 解析

def _png_dpi(path):
    """PNG：解析 pHYs chunk（像素/米）。"""
    with open(path, "rb") as f:
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            return None
        while True:
            hdr = f.read(8)
            if len(hdr) < 8:
                return None
            length, ctype = struct.unpack(">I4s", hdr)
            data = f.read(length)
            f.read(4)  # crc
            if ctype == b"pHYs" and len(data) >= 9:
                x_ppm, y_ppm, unit = struct.unpack(">IIB", data[:9])
                if unit == 1 and x_ppm:
                    return x_ppm * 0.0254, y_ppm * 0.0254 if y_ppm else x_ppm * 0.0254
                return None
            if ctype == b"IEND":
                return None

def _jpeg_dpi(path):
    """JPEG：解析 APP0/JFIF 密度字段。"""
    with open(path, "rb") as f:
        head = f.read(2)
        if head != b"\xff\xd8":
            return None
        while True:
            marker = f.read(2)
            if len(marker) < 2:
                return None
            if marker[0] != 0xFF:
                return None
            m = marker[1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:  # 无长度段
                continue
            if m == 0xD9:  # EOI
                return None
            seg = f.read(2)
            if len(seg) < 2:
                return None
            seg_len = struct.unpack(">H", seg)[0]
            if seg_len < 2:
                return None
            body = f.read(seg_len - 2)
            # JFIF APP0 布局: "JFIF\0"(5) + 版本(2) + 单位(1) + Xdensity(2) + Ydensity(2) + 缩略图(2)
            if m == 0xE0 and body.startswith(b"JFIF\x00") and len(body) >= 12:
                units, xd, yd = body[7], struct.unpack(">H", body[8:10])[0], \
                                 struct.unpack(">H", body[10:12])[0]
                if units == 1:
                    return (xd, yd) if xd else None
                if units == 2:
                    return (xd * 2.54, yd * 2.54) if xd else None
                return None

def _tiff_dpi(path):
    """TIFF：解析第一个 IFD 的 282/283（X/YResolution RATIONAL）与 296（ResolutionUnit）。"""
    with open(path, "rb") as f:
        hdr = f.read(8)
        if len(hdr) < 8:
            return None
        endian = "<" if hdr[:2] == b"II" else ">" if hdr[:2] == b"MM" else None
        if endian is None or struct.unpack(endian + "H", hdr[2:4])[0] != 42:
            return None
        ifd_off = struct.unpack(endian + "I", hdr[4:8])[0]
        f.seek(ifd_off)
        count = struct.unpack(endian + "H", f.read(2))[0]
        entries = f.read(12 * count)
        res, unit = None, 2  # 默认 inch
        for i in range(count):
            tag, typ, cnt, val = struct.unpack(endian + "HHII", entries[i * 12:i * 12 + 12])
            if tag == 282 and typ == 5 and cnt == 1:
                f.seek(val)
                num, den = struct.unpack(endian + "II", f.read(8))
                res = num / den if den else None
            elif tag == 296 and typ == 3:
                unit = val & 0xFFFF
        if res is None:
            return None
        if unit == 2:
            return res, res
        if unit == 3:
            return res * 2.54, res * 2.54
        return None

def image_dpi(path):
    """返回 (dpi_x, dpi_y) 或 None（无法解析/矢量）。"""
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".png":
            return _png_dpi(path)
        if ext in (".jpg", ".jpeg"):
            return _jpeg_dpi(path)
        if ext in (".tif", ".tiff"):
            return _tiff_dpi(path)
    except (OSError, struct.error, ValueError):
        return None
    return None  # eps/pdf 矢量，不做 DPI 校验

# ---------------------------------------------------------------- 主校验

def scan(submission_dir):
    """扫描目录，返回 {类别: [文件路径]} 与图片列表。"""
    found = {}
    images = []
    fallback_ms = []
    figure_dirs = ("figures", "figs", "images", "figure", "fig")
    for root, dirs, files in os.walk(submission_dir):
        for fn in sorted(files):
            path = os.path.join(root, fn)
            cat = classify(fn)
            if cat == "manuscript_fallback":
                fallback_ms.append(path)
            elif cat:
                found.setdefault(cat, []).append(path)
            # 图片：位于 figures 类目录，或未被归类为其他角色（排除 checklist/coi 等 PDF）
            parent = os.path.basename(root).lower()
            if is_image(fn) and (parent in figure_dirs or (parent == os.path.basename(submission_dir).lower() and cat is None)):
                images.append(path)
    if "manuscript" not in found and fallback_ms:
        found["manuscript"] = [fallback_ms[0]]
    return found, images

def check_dir(submission_dir, strict=False, dpi_threshold=DPI_THRESHOLD):
    found, images = scan(submission_dir)
    items = []
    total = {"pass": 0, "warn": 0, "fail": 0}

    def add(cat, status, msg):
        total[status] += 1
        items.append({"category": cat, "status": status, "message": msg})

    # 必需项
    required = ["manuscript", "cover_letter", "checklist", "references"]
    for cat in required:
        files = found.get(cat, [])
        if files:
            fs = files[0]
            size = os.path.getsize(fs)
            size_txt = " (%d KB)" % (size // 1024)
            size_note = " [large file >%d MB]" % MAX_FILE_MB if size > MAX_FILE_MB * 1024 * 1024 else ""
            add(cat, "pass", "found: %s%s%s" % (os.path.basename(fs), size_txt, size_note))
            if size > MAX_FILE_MB * 1024 * 1024:
                add(cat + "_size", "warn", "file exceeds %d MB" % MAX_FILE_MB)
        else:
            add(cat, "fail", "MISSING required file")

    # 可选但建议项
    optional = ["title_page", "highlights", "coi", "ethics", "registration",
                "response_letter", "supplementary", "tables"]
    for cat in optional:
        files = found.get(cat, [])
        if files:
            add(cat, "pass", "found: %s" % os.path.basename(files[0]))
        else:
            add(cat, "fail" if strict else "warn",
                 "missing optional (recommended)" if strict else "not found (optional)")

    # 图表
    if images:
        add("figures", "pass", "found %d image file(s)" % len(images))
    else:
        add("figures", "fail", "MISSING: no figure image files")
    for img in images:
        dpi = image_dpi(img)
        base = os.path.basename(img)
        if dpi is None:
            ext = os.path.splitext(img)[1].lower()
            if ext in (".eps", ".pdf"):
                add("figure_dpi", "pass", "%s: vector format (no DPI check)" % base)
            else:
                add("figure_dpi", "warn",
                    "%s: DPI not parseable, verify >=%d dpi manually" % (base, dpi_threshold))
        else:
            dmin = min(dpi)
            # 容差 1 dpi：300 dpi 对应的 pHYs 为 11811 ppm，反算得 299.9994 dpi
            if dmin >= dpi_threshold - 1:
                add("figure_dpi", "pass", "%s: %d dpi" % (base, round(dmin)))
            else:
                add("figure_dpi", "fail" if strict else "warn",
                    "%s: %d dpi < %d dpi" % (base, round(dmin), dpi_threshold))

    # 汇总
    result = "FAIL" if total["fail"] else ("PASS" if total["warn"] == 0 else "PASS_WITH_WARNINGS")
    summary = {"pass": total["pass"], "warn": total["warn"], "fail": total["fail"],
               "result": result}
    return summary, items

def main():
    ap = argparse.ArgumentParser(description="Medical submission package validator")
    ap.add_argument("submission_dir", help="path to the submission/ folder")
    ap.add_argument("--strict", action="store_true",
                    help="treat missing optional files and low-DPI figures as FAIL")
    ap.add_argument("--json", action="store_true", help="machine-readable JSON output")
    ap.add_argument("--dpi", type=int, default=DPI_THRESHOLD, help="DPI threshold (default 300)")
    args = ap.parse_args()

    if not os.path.isdir(args.submission_dir):
        sys.stderr.write("ERROR: not a directory: %s\n" % args.submission_dir)
        return 2

    summary, items = check_dir(args.submission_dir, strict=args.strict,
                               dpi_threshold=args.dpi)

    if args.json:
        print(json.dumps({"summary": summary, "items": items}, ensure_ascii=False, indent=2))
    else:
        for it in items:
            print("[%s] %-14s %s" % (it["status"].upper(), it["category"], it["message"]))
        print("-" * 70)
        print("SUMMARY: PASS %d | WARN %d | FAIL %d  ->  %s"
              % (summary["pass"], summary["warn"], summary["fail"], summary["result"]))

    return 0 if summary["fail"] == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
