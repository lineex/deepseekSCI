#!/usr/bin/env python3
"""Semantically search NanaDraw's complete bundled Bioicons library."""

from __future__ import annotations

import argparse
import base64
import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from html import escape
from pathlib import Path
from typing import Any, Iterable


SOURCE_URL = "https://github.com/duerrsimon/bioicons"
DEFAULT_ROOT = Path(r"D:\software\NanaDraw")

FUSED_TERMS = {
    "redbloodcell": "red blood cell",
    "bloodvessel": "blood vessel",
    "endothelialcell": "endothelial cell",
    "epithelialcell": "epithelial cell",
    "cancercell": "cancer cell",
    "tumorcell": "tumor cell",
    "tcell": "t cell",
    "bcell": "b cell",
    "mousekidney": "mouse kidney",
}

QUERY_TRANSLATIONS: dict[str, tuple[str, ...]] = {
    "内皮细胞": ("endothelial cell", "endothelium", "capillary"),
    "血管内皮": ("endothelium", "endothelial cell", "capillary"),
    "红细胞": ("red blood cell", "erythrocyte", "redbloodcell"),
    "红血球": ("red blood cell", "erythrocyte"),
    "t 淋巴细胞": ("t lymphocyte", "t cell"),
    "car t 细胞": ("car t cell", "t lymphocyte", "t cell receptor"),
    "嵌合抗原受体 t 细胞": ("car t cell", "t lymphocyte", "t cell receptor"),
    "肿瘤细胞": ("tumor cell", "cancer cell", "cancerous cell"),
    "癌细胞": ("cancer cell", "tumor cell"),
    "肿瘤": ("tumor", "cancer"),
    "小鼠": ("mouse", "laboratory mouse"),
    "实验小鼠": ("laboratory mouse", "mouse"),
    "真菌": ("fungi", "fungal cells", "yeast"),
    "酵母": ("yeast", "yeast cells"),
    "上皮细胞": ("epithelial cell", "epithelium"),
    "上皮": ("epithelium", "epithelial"),
    "受体": ("receptor", "membrane receptor"),
    "膜受体": ("membrane receptor", "receptor"),
    "her2 受体": ("her2 receptor", "receptor membrane", "simple receptor"),
    "血管": ("blood vessel", "vasculature", "artery", "vein", "capillary"),
    "毛细血管": ("capillary", "capillaries"),
    "动脉": ("artery", "arteries"),
    "静脉": ("vein", "veins"),
    "巨噬细胞": ("macrophage", "monocyte", "phagocyte"),
    "单核细胞": ("monocyte",),
    "中性粒细胞": ("neutrophil", "granulocyte"),
    "树突状细胞": ("dendritic cell", "antigen presenting cell"),
    "自然杀伤细胞": ("natural killer cell", "nk cell"),
    "血小板": ("platelet",),
    "白细胞": ("leukocyte", "immune cell"),
    "细菌": ("bacteria", "bacterium"),
    "病毒": ("virus", "virion"),
    "寄生虫": ("parasite",),
    "心脏": ("heart",),
    "肝脏": ("liver",),
    "肾脏": ("kidney",),
    "肺": ("lung",),
    "脾脏": ("spleen",),
    "胰腺": ("pancreas",),
    "肠道": ("intestine", "gut"),
    "显微镜": ("microscope",),
    "离心机": ("centrifuge",),
    "移液器": ("pipette",),
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "cell",
    "cells",
    "diagram",
    "generic",
    "human",
    "icon",
    "model",
    "new",
    "of",
    "simple",
    "the",
    "type",
}

LICENSE_PRIORS = {
    "cc-0": 4,
    "mit": 3,
    "bsd": 3,
    "cc-by-3.0": 1,
    "cc-by-4.0": 1,
    "cc-by-sa-3.0": 0,
    "cc-by-sa-4.0": 0,
}


@dataclass(frozen=True)
class ConceptProfile:
    name: str
    aliases: tuple[str, ...]
    partial_aliases: tuple[str, ...]
    preferred_categories: tuple[tuple[str, int], ...]
    allowed_categories: tuple[str, ...] = ()
    required_terms: tuple[str, ...] = ()
    excluded_terms: tuple[str, ...] = ()
    composition_hint: str | None = None


@dataclass(frozen=True)
class FamilyProfile:
    name: str
    triggers: tuple[str, ...]
    preferred_categories: tuple[tuple[str, int], ...]


CONCEPT_PROFILES = (
    ConceptProfile(
        name="endothelial_cell",
        aliases=(
            "endothelial cell",
            "endothelium",
            "endothelial",
            "capillary",
            "capillaries",
            "continuous capillary",
            "fenestrated capillary",
            "sinusoidal capillary",
            "microvascular endothelium",
        ),
        partial_aliases=("vascular endothelium", "vascularis", "microvessel"),
        preferred_categories=(("Human_physiology", 46), ("Tissues", 30), ("Cell_types", 12)),
        allowed_categories=("Human_physiology", "Tissues", "Cell_types", "Blood_Immunology"),
        required_terms=("endothel", "capillar", "vascularis", "microvessel"),
        excluded_terms=("embryo", "zygote", "oocyte", "blastocyst", "morula"),
        composition_hint=(
            "The library mainly represents endothelium as capillary or vessel structures; "
            "adapt the vessel wall contour when a single endothelial cell is required."
        ),
    ),
    ConceptProfile(
        name="red_blood_cell",
        aliases=("red blood cell", "erythrocyte", "erythrocytes", "redbloodcell", "red cell"),
        partial_aliases=("mature erythrocyte",),
        preferred_categories=(("Blood_Immunology", 46), ("Cell_types", 34)),
        allowed_categories=("Blood_Immunology", "Cell_types"),
        required_terms=("red blood cell", "erythrocyte"),
        excluded_terms=("erythroblast", "b cell", "t cell", "lymphocyte", "leukocyte"),
    ),
    ConceptProfile(
        name="t_lymphocyte",
        aliases=("t lymphocyte", "t cell", "cytotoxic t lymphocyte", "cytotoxic t cell", "ctl"),
        partial_aliases=("lymphocyte",),
        preferred_categories=(("Blood_Immunology", 48), ("Cell_types", 26)),
        allowed_categories=("Blood_Immunology", "Cell_types"),
        required_terms=("t lymphocyte", "t cell", "lymphocyte"),
        excluded_terms=("b lymphocyte", "b cell", "receptor", "epitheli", "gobelet", "embryo"),
    ),
    ConceptProfile(
        name="car_t_cell",
        aliases=("car t cell", "car t", "chimeric antigen receptor t cell", "t lymphocyte", "t cell"),
        partial_aliases=("lymphocyte", "t cell receptor"),
        preferred_categories=(("Blood_Immunology", 48), ("Cell_types", 26), ("Receptors_channels", 16)),
        allowed_categories=("Blood_Immunology", "Cell_types", "Receptors_channels", "Cell_membrane"),
        required_terms=("t lymphocyte", "t cell", "lymphocyte", "receptor"),
        excluded_terms=("b lymphocyte", "b cell", "epitheli", "embryo"),
        composition_hint=(
            "Build CAR T as a composite: a T-lymphocyte silhouette plus a membrane receptor asset "
            "and an explicit target-binding domain label."
        ),
    ),
    ConceptProfile(
        name="tumor_cell",
        aliases=("tumor cell", "tumour cell", "cancer cell", "cancerous cell", "tumor", "tumour"),
        partial_aliases=("malignant cell", "carcinoma cell", "neoplastic cell"),
        preferred_categories=(("Oncology", 48), ("Blood_Immunology", 24), ("Cell_lines", 18)),
        allowed_categories=("Oncology", "Blood_Immunology", "Cell_lines", "Cell_types", "Human_physiology"),
        required_terms=("tumor", "tumour", "cancer", "malignan", "carcinoma", "neoplas"),
    ),
    ConceptProfile(
        name="mouse",
        aliases=("mouse", "laboratory mouse", "mus musculus"),
        partial_aliases=("murine model",),
        preferred_categories=(("Animals", 52),),
        allowed_categories=("Animals",),
        required_terms=("mouse",),
        excluded_terms=("embryo", "head", "kidney", "maze", "test", "smiling"),
    ),
    ConceptProfile(
        name="fungi",
        aliases=("fungi", "fungus", "fungal cell", "fungal cells", "yeast", "yeast cells"),
        partial_aliases=("mycelium", "conidia", "germlings", "candida", "budding yeast", "fission yeast"),
        preferred_categories=(("Microbiology", 50), ("Genetics", 20), ("Plants_Algae", 12)),
        allowed_categories=("Microbiology", "Genetics", "Plants_Algae"),
        required_terms=("fungi", "fungus", "fungal", "yeast", "mycel", "conidia", "germling", "candida"),
    ),
    ConceptProfile(
        name="epithelium",
        aliases=("epithelium", "epithelial cell", "epithelial cells", "epithelial"),
        partial_aliases=("epidermis", "columnar cell", "goblet cell", "gobelet cell"),
        preferred_categories=(("Tissues", 48), ("Microbiology", 25), ("Human_physiology", 22)),
        allowed_categories=("Tissues", "Microbiology", "Human_physiology", "Cell_types"),
        required_terms=("epitheli", "epiderm", "columnar", "goblet", "gobelet"),
        excluded_terms=("endothel",),
    ),
    ConceptProfile(
        name="receptor",
        aliases=("receptor", "membrane receptor", "cell surface receptor", "transmembrane receptor"),
        partial_aliases=("receptor ligand", "t cell receptor", "channel receptor"),
        preferred_categories=(("Receptors_channels", 52), ("Cell_membrane", 28), ("Blood_Immunology", 12)),
        allowed_categories=("Receptors_channels", "Cell_membrane", "Blood_Immunology"),
        required_terms=("receptor",),
        excluded_terms=("photoreceptor cell",),
    ),
    ConceptProfile(
        name="blood_vessel",
        aliases=(
            "blood vessel",
            "blood vessels",
            "vasculature",
            "vascular",
            "artery",
            "arteries",
            "vein",
            "veins",
            "capillary",
            "capillaries",
        ),
        partial_aliases=("bloodstream", "blood flow", "venous system", "vascular tunic"),
        preferred_categories=(("Human_physiology", 52), ("Tissues", 20)),
        allowed_categories=("Human_physiology", "Tissues"),
        required_terms=("blood vessel", "vascul", "arter", "vein", "capillar", "bloodstream", "blood flow"),
    ),
    ConceptProfile(
        name="her2_receptor",
        aliases=("her2", "her2 receptor", "erbb2", "receptor"),
        partial_aliases=("transmembrane receptor", "simple receptor", "receptor membrane"),
        preferred_categories=(("Receptors_channels", 52), ("Cell_membrane", 26), ("Oncology", 12)),
        allowed_categories=("Receptors_channels", "Cell_membrane", "Oncology"),
        required_terms=("her2", "erbb2", "receptor"),
        composition_hint=(
            "Use a generic membrane receptor scaffold when no HER2-specific icon exists, then add "
            "the HER2 label and preserve extracellular, transmembrane, and intracellular domains."
        ),
    ),
)


FAMILY_PROFILES = (
    FamilyProfile(
        "immune_cells",
        (
            "immune cell",
            "macrophage",
            "monocyte",
            "neutrophil",
            "lymphocyte",
            "dendritic cell",
            "natural killer",
            "nk cell",
            "platelet",
            "leukocyte",
            "granulocyte",
        ),
        (("Blood_Immunology", 38), ("Cell_types", 22), ("Human_physiology", 8)),
    ),
    FamilyProfile(
        "animals",
        ("animal", "mouse", "rat", "rabbit", "zebrafish", "drosophila", "monkey", "pig", "dog"),
        (("Animals", 42), ("Procedures", 8)),
    ),
    FamilyProfile(
        "tissues",
        ("tissue", "epithelium", "endothelium", "stroma", "skin", "muscle", "matrix"),
        (("Tissues", 38), ("Human_physiology", 26), ("Extracellular_matrix", 16)),
    ),
    FamilyProfile(
        "organs",
        ("organ", "heart", "liver", "kidney", "lung", "brain", "spleen", "pancreas", "intestine"),
        (("Human_physiology", 42), ("Tissues", 18)),
    ),
    FamilyProfile(
        "microorganisms",
        ("microorganism", "bacteria", "bacterium", "fungi", "yeast", "virus", "parasite", "protozoa"),
        (("Microbiology", 40), ("Viruses", 34), ("Parasites", 30), ("Plants_Algae", 10)),
    ),
    FamilyProfile(
        "oncology",
        ("tumor", "tumour", "cancer", "oncology", "metastasis", "malignant", "carcinoma"),
        (("Oncology", 42), ("Cell_lines", 20), ("Blood_Immunology", 10)),
    ),
    FamilyProfile(
        "receptors_channels",
        ("receptor", "channel", "transporter", "pump", "ion channel", "ligand"),
        (("Receptors_channels", 44), ("Cell_membrane", 28)),
    ),
    FamilyProfile(
        "lab_equipment",
        ("microscope", "centrifuge", "pipette", "flask", "tube", "plate", "syringe", "apparatus"),
        (("Lab_apparatus", 44), ("Cell_culture", 28), ("Imaging", 18), ("Microbiology", 8)),
    ),
    FamilyProfile(
        "molecular_objects",
        ("dna", "rna", "gene", "protein", "peptide", "amino acid", "molecule", "nucleic acid", "chromosome"),
        (
            ("Nucleic_acids", 40),
            ("Genetics", 34),
            ("Intracellular_components", 22),
            ("Amino-Acids", 20),
            ("Peptides", 18),
            ("Chemistry", 14),
            ("Molecular_modelling", 12),
        ),
    ),
)


def normalize(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    value = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", value)
    value = re.sub(r"(?<=[A-Za-z0-9])(?=[\u4e00-\u9fff])", " ", value)
    value = re.sub(r"(?<=[\u4e00-\u9fff])(?=[A-Za-z0-9])", " ", value)
    value = value.casefold().replace("_", " ").replace("-", " ")
    value = " ".join(re.findall(r"[a-z0-9\u4e00-\u9fff]+", value))
    for fused, expanded in FUSED_TERMS.items():
        value = re.sub(rf"\b{re.escape(fused)}\b", expanded, value)
    return " ".join(value.split())


def _contains(text: str, term: str) -> bool:
    term_norm = normalize(term)
    if not term_norm:
        return False
    padded = f" {text} "
    if f" {term_norm} " in padded:
        return True
    if " " not in term_norm and len(term_norm) >= 5:
        return any(token.startswith(term_norm) for token in text.split())
    return False


def _significant_tokens(value: str) -> set[str]:
    tokens = set(normalize(value).split())
    reduced = {token for token in tokens if token not in STOPWORDS and (len(token) >= 2 or token in {"t", "b"})}
    return reduced or tokens


def _profile_terms(profile: ConceptProfile) -> tuple[str, ...]:
    return (profile.name.replace("_", " "), *profile.aliases, *profile.partial_aliases)


def translated_terms(query: str) -> list[str]:
    query_norm = normalize(query)
    matches: list[tuple[int, tuple[str, ...]]] = []
    for source, translations in QUERY_TRANSLATIONS.items():
        source_norm = normalize(source)
        if query_norm == source_norm or _contains(query_norm, source_norm):
            matches.append((len(source_norm), translations))
    if not matches:
        return []
    most_specific = max(length for length, _ in matches)
    rows = [
        normalize(item)
        for length, translations in matches
        if length == most_specific
        for item in translations
    ]
    return list(dict.fromkeys(item for item in rows if item))


def resolve_concept_profile(query: str) -> ConceptProfile | None:
    query_norms = [normalize(query), *translated_terms(query)]
    exact_matches: list[tuple[int, ConceptProfile]] = []
    contained_matches: list[tuple[int, ConceptProfile]] = []
    for profile in CONCEPT_PROFILES:
        for term in _profile_terms(profile):
            term_norm = normalize(term)
            for query_norm in query_norms:
                if query_norm == term_norm:
                    exact_matches.append((len(term_norm), profile))
                elif len(term_norm) >= 4 and _contains(query_norm, term_norm):
                    contained_matches.append((len(term_norm), profile))
    matches = exact_matches or contained_matches
    return max(matches, key=lambda row: row[0])[1] if matches else None


def resolve_family_profile(query: str) -> FamilyProfile | None:
    query_norm = " ".join((normalize(query), *translated_terms(query)))
    matches: list[tuple[int, FamilyProfile]] = []
    for profile in FAMILY_PROFILES:
        for trigger in profile.triggers:
            trigger_norm = normalize(trigger)
            if _contains(query_norm, trigger_norm):
                matches.append((len(trigger_norm), profile))
    return max(matches, key=lambda row: row[0])[1] if matches else None


def query_variants(query: str, profile: ConceptProfile | None) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = [(normalize(query), 0, "query")]
    rows.extend((term, 0, "translation") for term in translated_terms(query))
    if profile:
        rows.extend((normalize(alias), 0, "concept_alias") for alias in profile.aliases)
        rows.extend((normalize(alias), -24, "partial_alias") for alias in profile.partial_aliases)
    seen: set[str] = set()
    result: list[tuple[str, int, str]] = []
    for term, penalty, source in rows:
        if term and term not in seen:
            seen.add(term)
            result.append((term, penalty, source))
    return result


def _category_priors(
    profile: ConceptProfile | None,
    family: FamilyProfile | None,
) -> dict[str, int]:
    rows = profile.preferred_categories if profile else (family.preferred_categories if family else ())
    return {normalize(category): score for category, score in rows}


def _score_variant(name: str, variant: str) -> tuple[int, str] | None:
    if not variant:
        return None
    name_tokens = set(name.split())
    variant_tokens = _significant_tokens(variant)
    if name == variant:
        return 160, "exact_name"
    if _contains(name, variant):
        return 132, "phrase_in_name"
    if variant_tokens and variant_tokens <= name_tokens:
        return 112 + min(12, len(variant_tokens) * 3), "all_tokens_in_name"

    overlap = len(variant_tokens & name_tokens)
    if overlap:
        coverage = overlap / max(1, len(variant_tokens))
        precision = overlap / max(1, len(name_tokens))
        if coverage >= 0.5:
            return int(54 * coverage + 24 * precision + overlap * 5), "token_overlap"

    compact_variant = variant.replace(" ", "")
    compact_name = name.replace(" ", "")
    if len(compact_variant) >= 5 and len(compact_name) >= 5:
        ratio = SequenceMatcher(None, compact_variant, compact_name).ratio()
        if ratio >= 0.68:
            return int(65 * ratio), "fuzzy_name"
    return None


def score_icon(
    icon: dict[str, Any],
    query: str,
    profile: ConceptProfile | None,
    family: FamilyProfile | None,
    excluded_terms: Iterable[str],
) -> tuple[int, list[str], list[str]] | None:
    name = normalize(str(icon.get("name", "")))
    category = normalize(str(icon.get("category", "")))
    searchable = normalize(f"{icon.get('name', '')} {Path(str(icon.get('svg_path', ''))).stem}")

    if any(_contains(searchable, term) for term in excluded_terms):
        return None
    if profile and profile.excluded_terms and any(_contains(searchable, term) for term in profile.excluded_terms):
        return None
    if profile and profile.allowed_categories:
        allowed = {normalize(item) for item in profile.allowed_categories}
        if category not in allowed:
            return None
    if profile and profile.required_terms:
        if not any(_contains(searchable, term) for term in profile.required_terms):
            return None

    best = 0
    matched_aliases: list[str] = []
    reasons: list[str] = []
    for variant, penalty, source in query_variants(query, profile):
        scored = _score_variant(name, variant)
        if not scored:
            continue
        raw_score, reason = scored
        candidate = max(1, raw_score + penalty)
        if candidate > best:
            best = candidate
            matched_aliases = [variant]
            reasons = [f"{reason}:{variant}", f"variant_source:{source}"]
        elif candidate == best:
            matched_aliases.append(variant)
            reasons.append(f"{reason}:{variant}")

    if best <= 0:
        return None

    category_bonus = _category_priors(profile, family).get(category, 0)
    if category_bonus:
        best += category_bonus
        reasons.append(f"category_prior:{icon.get('category')}:+{category_bonus}")
    license_name = str(icon.get("license", "")).casefold()
    license_bonus = LICENSE_PRIORS.get(license_name, 0)
    if license_bonus:
        best += license_bonus
        reasons.append(f"license_prior:{license_name}:+{license_bonus}")

    return best, sorted(set(matched_aliases)), list(dict.fromkeys(reasons))


def load_metadata(root: Path) -> tuple[Path, dict[str, Any]]:
    metadata_path = root / "backend" / "static" / "bioicons" / "metadata.json"
    if not metadata_path.is_file():
        raise FileNotFoundError(f"Bioicons metadata not found: {metadata_path}")
    payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    if not isinstance(payload.get("icons"), list):
        raise ValueError(f"Invalid Bioicons metadata: {metadata_path}")
    return metadata_path, payload


def resolve_svg(root: Path, icon: dict[str, Any]) -> Path | None:
    svg_root = root / "backend" / "static" / "bioicons" / "svgs"
    relative = Path(str(icon.get("svg_path", "")))
    license_name = str(icon.get("license", ""))
    preferred = svg_root / license_name / relative
    if preferred.is_file():
        return preferred.resolve()
    candidates = sorted(svg_root.glob(f"*/{relative.as_posix()}"))
    return candidates[0].resolve() if candidates else None


def _match_quality(score: int, reasons: list[str]) -> str:
    if "variant_source:partial_alias" in reasons:
        return "partial"
    if any(reason.startswith("exact_name:") for reason in reasons):
        return "exact"
    if score >= 150:
        return "strong_semantic"
    if score >= 100:
        return "semantic"
    return "partial"


def result_row(
    root: Path,
    icon: dict[str, Any],
    score: int,
    matches: list[str],
    reasons: list[str],
) -> dict[str, Any]:
    path = resolve_svg(root, icon)
    return {
        "id": icon.get("id"),
        "name": icon.get("name"),
        "category": icon.get("category"),
        "author": icon.get("author"),
        "license": icon.get("license"),
        "svg_path": icon.get("svg_path"),
        "resolved_svg_path": str(path) if path else None,
        "exists": bool(path),
        "width": icon.get("w"),
        "height": icon.get("h"),
        "score": score,
        "match_quality": _match_quality(score, reasons),
        "matched_aliases": matches,
        "match_reasons": reasons,
        "source": SOURCE_URL,
    }


def _resolve_categories(payload: dict[str, Any], requested: Iterable[str]) -> set[str]:
    known = {normalize(row["name"]): row["name"] for row in payload.get("categories", [])}
    selected: set[str] = set()
    unknown: list[str] = []
    for item in requested:
        for part in item.split(","):
            category = normalize(part)
            if not category:
                continue
            if category not in known:
                unknown.append(part.strip())
            else:
                selected.add(category)
    if unknown:
        choices = ", ".join(row["name"] for row in payload.get("categories", []))
        raise ValueError(f"Unknown categories: {', '.join(unknown)}. Available: {choices}")
    return selected


def build_shortlist(
    root: Path,
    queries: list[str],
    limit: int,
    categories: Iterable[str] = (),
    excluded_terms: Iterable[str] = (),
) -> dict[str, Any]:
    metadata_path, payload = load_metadata(root)
    icons = payload["icons"]
    category_filter = _resolve_categories(payload, categories)
    user_excludes = tuple(excluded_terms)
    results: dict[str, list[dict[str, Any]]] = {}
    routing: dict[str, dict[str, Any]] = {}

    for query in queries:
        profile = resolve_concept_profile(query)
        family = resolve_family_profile(query)
        ranked: list[tuple[int, str, dict[str, Any], list[str], list[str]]] = []
        for icon in icons:
            if category_filter and normalize(str(icon.get("category", ""))) not in category_filter:
                continue
            scored = score_icon(icon, query, profile, family, user_excludes)
            if not scored:
                continue
            score, matches, reasons = scored
            ranked.append((score, normalize(str(icon.get("name", ""))), icon, matches, reasons))
        ranked.sort(key=lambda row: (-row[0], row[1], str(row[2].get("id", ""))))
        results[query] = [
            result_row(root, icon, score, matches, reasons)
            for score, _, icon, matches, reasons in ranked[:limit]
        ]
        priors = _category_priors(profile, family)
        routing[query] = {
            "concept_profile": profile.name if profile else None,
            "family_profile": family.name if family else None,
            "preferred_categories": [
                {"category": category, "priority": priority}
                for category, priority in (
                    profile.preferred_categories if profile else (family.preferred_categories if family else ())
                )
            ],
            "active_category_priors": priors,
            "composition_hint": profile.composition_hint if profile else None,
            "candidate_count_before_limit": len(ranked),
        }

    return {
        "root": str(root.resolve()),
        "metadata": str(metadata_path.resolve()),
        "library": {
            "category_count": len(payload.get("categories", [])),
            "icon_count": len(icons),
        },
        "queries": queries,
        "limit_per_query": limit,
        "category_filter": sorted(category_filter),
        "excluded_terms": list(user_excludes),
        "routing": routing,
        "results": results,
    }


def category_inventory(root: Path) -> dict[str, Any]:
    metadata_path, payload = load_metadata(root)
    categories = [
        {"name": row.get("name"), "count": int(row.get("count", 0))}
        for row in payload.get("categories", [])
    ]
    return {
        "root": str(root.resolve()),
        "metadata": str(metadata_path.resolve()),
        "category_count": len(categories),
        "icon_count": len(payload["icons"]),
        "categories": categories,
    }


def write_preview(preview_dir: Path, data: dict[str, Any]) -> Path:
    preview_dir.mkdir(parents=True, exist_ok=True)
    manifest = preview_dir / "shortlist.json"
    manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sections: list[str] = []
    for query, rows in data.get("results", {}).items():
        cards: list[str] = []
        for row in rows:
            path_text = row.get("resolved_svg_path")
            image_markup = '<div class="missing">SVG missing</div>'
            if path_text and Path(path_text).is_file():
                encoded = base64.b64encode(Path(path_text).read_bytes()).decode("ascii")
                image_markup = f'<img src="data:image/svg+xml;base64,{encoded}" alt="{escape(str(row.get("name")))}">'
            reasons = "<br>".join(escape(item) for item in row.get("match_reasons", []))
            cards.append(
                "<article class=\"card\">"
                f"<div class=\"art\">{image_markup}</div>"
                f"<h3>{escape(str(row.get('name')))}</h3>"
                f"<p>{escape(str(row.get('category')))} | {escape(str(row.get('author')))}</p>"
                f"<p>{escape(str(row.get('license')))} | score {row.get('score')} | "
                f"{escape(str(row.get('match_quality')))}</p>"
                f"<details><summary>Match reasons</summary><code>{reasons}</code></details>"
                f"<p class=\"path\">{escape(str(path_text))}</p>"
                "</article>"
            )
        hint = data.get("routing", {}).get(query, {}).get("composition_hint")
        hint_markup = f'<p class="hint">{escape(hint)}</p>' if hint else ""
        sections.append(
            f"<section><h2>{escape(query)}</h2>{hint_markup}<div class=\"grid\">{''.join(cards)}</div></section>"
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bioicons semantic shortlist</title>
<style>
body {{ margin: 0; font-family: Arial, sans-serif; color: #202124; background: #f5f6f7; }}
header, section {{ max-width: 1500px; margin: 0 auto; padding: 20px 24px; }}
h1 {{ margin: 0 0 6px; font-size: 25px; }} h2 {{ margin: 12px 0; font-size: 21px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 12px; }}
.card {{ min-width: 0; padding: 12px; border: 1px solid #d9dde2; background: white; }}
.art {{ display: grid; place-items: center; height: 190px; background: #fff; }}
.art img {{ max-width: 100%; max-height: 180px; }}
.card h3 {{ margin: 10px 0 6px; font-size: 16px; overflow-wrap: anywhere; }}
.card p {{ margin: 5px 0; font-size: 12px; line-height: 1.35; }}
.hint {{ border-left: 3px solid #247b78; padding: 8px 12px; background: #edf7f5; }}
.path {{ color: #5f6368; overflow-wrap: anywhere; }}
details {{ font-size: 12px; }} code {{ white-space: normal; overflow-wrap: anywhere; }}
.missing {{ color: #b3261e; }}
</style>
</head>
<body>
<header><h1>Bioicons semantic shortlist</h1>
<p>{data.get('library', {}).get('icon_count')} icons searched across {data.get('library', {}).get('category_count')} categories.</p>
</header>
{''.join(sections)}
</body>
</html>
"""
    index = preview_dir / "index.html"
    index.write_text(html, encoding="utf-8")
    return index.resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--query", action="append", help="Biomedical object query; repeat as needed")
    parser.add_argument("--category", action="append", default=[], help="Restrict search to a category; repeat as needed")
    parser.add_argument("--exclude", action="append", default=[], help="Exclude a name/path term; repeat as needed")
    parser.add_argument("--limit", type=int, default=6)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--preview-dir", type=Path, help="Write a self-contained visual candidate review page")
    parser.add_argument("--list-categories", action="store_true", help="Print the complete category inventory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be positive")
    if args.list_categories:
        data = category_inventory(args.root)
    else:
        if not args.query:
            raise SystemExit("At least one --query is required unless --list-categories is used")
        data = build_shortlist(
            args.root,
            args.query,
            args.limit,
            categories=args.category,
            excluded_terms=args.exclude,
        )

    preview_path = None
    if args.preview_dir and not args.list_categories:
        preview_path = write_preview(args.preview_dir, data)
        data["preview_index"] = str(preview_path)

    text = json.dumps(data, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        print(
            json.dumps(
                {
                    "output": str(args.output.resolve()),
                    "queries": args.query or [],
                    "limit": args.limit,
                    "preview_index": str(preview_path) if preview_path else None,
                }
            )
        )
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
