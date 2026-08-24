#!/usr/bin/env python3
"""Regression checks for Bioicons concept routing and path resolution."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("bioicons_asset_grounder.py")
SPEC = importlib.util.spec_from_file_location("bioicons_asset_grounder", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not load {SCRIPT}")
grounder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = grounder
SPEC.loader.exec_module(grounder)


class BioiconsGrounderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(r"D:\software\NanaDraw")
        cls.queries = [
            "endothelial cell",
            "red blood cell",
            "T lymphocyte",
            "CAR T cell",
            "HER2 receptor",
            "tumor cell",
            "mouse",
            "fungi",
            "epithelium",
            "receptor",
            "blood vessel",
            "内皮细胞",
            "红细胞",
            "T淋巴细胞",
            "CAR T细胞",
            "HER2受体",
            "肿瘤细胞",
            "小鼠",
            "巨噬细胞",
            "显微镜",
        ]
        cls.data = grounder.build_shortlist(cls.root, cls.queries, limit=6)

    def names(self, query: str) -> list[str]:
        return [grounder.normalize(row["name"]) for row in self.data["results"][query]]

    def test_inventory_is_complete(self) -> None:
        self.assertEqual(self.data["library"]["category_count"], 37)
        self.assertEqual(self.data["library"]["icon_count"], 2804)

    def test_endothelium_routes_to_vasculature_not_embryos(self) -> None:
        names = self.names("endothelial cell")
        self.assertTrue(names)
        self.assertTrue(any("capillar" in name or "endothel" in name for name in names[:3]))
        self.assertFalse(any("embryo" in name or "zygote" in name for name in names))

    def test_red_blood_cell_does_not_resolve_to_b_cell(self) -> None:
        names = self.names("red blood cell")
        self.assertTrue(any("erythrocyte" in name or "red blood cell" in name for name in names[:3]))
        self.assertFalse(any(name.startswith("b cell") for name in names))

    def test_t_lymphocyte_prefers_t_specific_asset(self) -> None:
        names = self.names("T lymphocyte")
        self.assertIn("t lymphocyte", names[0])
        self.assertFalse(any("epitheli" in name for name in names))
        self.assertFalse(any("mast cell" in name or "receptor" in name for name in names))

    def test_engineered_cell_queries_return_composable_parts(self) -> None:
        car_names = self.names("CAR T cell")
        self.assertTrue(any("t lymphocyte" in name for name in car_names[:3]))
        self.assertTrue(any("receptor" in name for name in car_names))
        self.assertIn("composite", self.data["routing"]["CAR T cell"]["composition_hint"])
        her2_rows = self.data["results"]["HER2 receptor"]
        self.assertTrue(her2_rows)
        self.assertTrue(all(row["category"] in {"Receptors_channels", "Cell_membrane", "Oncology"} for row in her2_rows))
        self.assertIn("HER2", self.data["routing"]["HER2 receptor"]["composition_hint"])
        self.assertEqual(self.data["routing"]["CAR T细胞"]["concept_profile"], "car_t_cell")
        self.assertIn("composite", self.data["routing"]["CAR T细胞"]["composition_hint"])
        self.assertEqual(self.data["routing"]["HER2受体"]["concept_profile"], "her2_receptor")
        self.assertIn("HER2", self.data["routing"]["HER2受体"]["composition_hint"])

    def test_chinese_entity_queries_bridge_to_library_names(self) -> None:
        checks = {
            "内皮细胞": ("endothelial_cell", ("capillar", "endothel")),
            "红细胞": ("red_blood_cell", ("erythrocyte", "red blood cell")),
            "T淋巴细胞": ("t_lymphocyte", ("t lymphocyte",)),
            "肿瘤细胞": ("tumor_cell", ("tumor", "cancer")),
            "小鼠": ("mouse", ("mouse",)),
        }
        for query, (profile, expected_fragments) in checks.items():
            with self.subTest(query=query):
                self.assertEqual(self.data["routing"][query]["concept_profile"], profile)
                names = self.names(query)
                self.assertTrue(names)
                self.assertTrue(any(fragment in names[0] for fragment in expected_fragments), names)

    def test_generic_chinese_queries_use_family_routing(self) -> None:
        macrophage = self.data["results"]["巨噬细胞"][0]
        self.assertEqual(self.data["routing"]["巨噬细胞"]["family_profile"], "immune_cells")
        self.assertEqual(grounder.normalize(macrophage["name"]), "macrophage")
        self.assertEqual(macrophage["category"], "Blood_Immunology")
        microscope = self.data["results"]["显微镜"][0]
        self.assertEqual(self.data["routing"]["显微镜"]["family_profile"], "lab_equipment")
        self.assertEqual(grounder.normalize(microscope["name"]), "microscope")
        self.assertEqual(microscope["category"], "Lab_apparatus")

    def test_oncology_and_mouse_hard_routing(self) -> None:
        tumor_rows = self.data["results"]["tumor cell"]
        self.assertTrue(tumor_rows)
        self.assertTrue(all(row["category"] in {"Oncology", "Blood_Immunology", "Cell_lines", "Cell_types", "Human_physiology"} for row in tumor_rows))
        mouse_rows = self.data["results"]["mouse"]
        self.assertTrue(mouse_rows)
        self.assertTrue(all(row["category"] == "Animals" for row in mouse_rows))
        self.assertFalse(any(any(term in grounder.normalize(row["name"]) for term in ("embryo", "head", "kidney", "maze")) for row in mouse_rows))

    def test_representative_category_routing(self) -> None:
        self.assertEqual(self.data["results"]["fungi"][0]["category"], "Microbiology")
        self.assertIn(self.data["results"]["epithelium"][0]["category"], {"Tissues", "Microbiology", "Human_physiology"})
        self.assertEqual(self.data["results"]["receptor"][0]["category"], "Receptors_channels")
        self.assertEqual(self.data["results"]["blood vessel"][0]["category"], "Human_physiology")

    def test_every_shortlisted_svg_exists(self) -> None:
        for rows in self.data["results"].values():
            self.assertTrue(rows)
            for row in rows:
                self.assertTrue(row["exists"], row)
                self.assertTrue(Path(row["resolved_svg_path"]).is_file(), row)


if __name__ == "__main__":
    unittest.main(verbosity=2)
