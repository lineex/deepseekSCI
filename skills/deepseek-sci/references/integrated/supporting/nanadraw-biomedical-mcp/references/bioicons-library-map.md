# Integrated supporting reference: nanadraw-biomedical-mcp/references/bioicons-library-map.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/bioicons-library-map.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# NanaDraw Bioicons Library Map

Read this reference before concluding that NanaDraw lacks a biomedical asset.
The bundled inventory contains 2,804 editable SVG icons in 37 categories at
`LOCAL_PATH`.

## Contents

1. Complete category inventory
2. Biomedical concept routing
3. Full-search protocol
4. Composite scientific objects
5. Match-quality decisions

## 1. Complete category inventory

| Category | Count | Primary use |
| --- | ---: | --- |
| `Amino-Acids` | 68 | Amino-acid structures and residue symbols |
| `Animals` | 384 | Model organisms, whole animals, developmental stages |
| `Blood_Immunology` | 205 | Blood cells, leukocytes, antibodies, immune mechanisms |
| `Cell_culture` | 53 | Culture vessels, plates, media, cell handling |
| `Cell_lines` | 9 | Named experimental cell-line symbols |
| `Cell_membrane` | 89 | Bilayers, membrane proteins, vesicles, surface processes |
| `Cell_types` | 28 | General canonical cell silhouettes |
| `Chemistry` | 91 | Chemical structures, reactions, laboratory chemistry |
| `Chemo-_and_Bioinformatics` | 24 | Sequence and cheminformatics concepts |
| `Computer_hardware` | 12 | Computers, storage, compute hardware |
| `Epigenetics` | 2 | Epigenetic regulation concepts |
| `Extracellular_matrix` | 2 | Matrix and extracellular scaffold |
| `General_items` | 176 | Generic arrows, containers, symbols, miscellaneous objects |
| `Genetics` | 85 | Inheritance, chromosomes, gene editing, model genetics |
| `Genomics` | 6 | Genomic analysis concepts |
| `Human_physiology` | 460 | Organs, vasculature, anatomy, disease states, physiological systems |
| `Imaging` | 10 | Imaging systems and acquisition concepts |
| `Intracellular_components` | 120 | Organelles, cytoskeleton, intracellular structures |
| `Lab_apparatus` | 165 | Instruments, tubes, pipettes, laboratory equipment |
| `Machine_Learning` | 31 | ML tools, architectures, and software symbols |
| `Microbiology` | 154 | Bacteria, fungi, culture equipment, microbial structures |
| `Molecular_Biology` | 1 | General molecular-biology object |
| `Molecular_modelling` | 17 | Molecular representations and modelling concepts |
| `Nanotechnology` | 4 | Nanoparticles and nanoscale engineering |
| `Neuroscience` | 1 | Neuroscience-specific object |
| `Nucleic_acids` | 96 | DNA, RNA, nucleotides, helices, sequence objects |
| `Oncology` | 37 | Tumor cells, cancer states, metastasis, oncology concepts |
| `Parasites` | 72 | Parasites and parasitic life-cycle stages |
| `People-Other` | 29 | People, patients, researchers, non-anatomical human figures |
| `Peptides` | 3 | Peptide structures |
| `Plants_Algae` | 96 | Plants, algae, botanical structures |
| `Procedures` | 30 | Experimental and clinical procedures |
| `Receptors_channels` | 66 | Membrane receptors, channels, pumps, ligand binding |
| `Safety_symbols` | 42 | Hazards and laboratory safety symbols |
| `Scientific_graphs` | 57 | Plot and chart templates |
| `Tissues` | 55 | Epithelia, tissue layers, histological structures |
| `Viruses` | 24 | Virions and virus-specific structures |

Counts come from `metadata.json`. Re-run the grounder with
`--list-categories` after library updates instead of relying on stale counts.

## 2. Biomedical concept routing

Use the first category as the primary route, then search every listed fallback
before generating a replacement.

| Requested entity | Preferred categories | Alias and filename probes |
| --- | --- | --- |
| T lymphocyte / CTL | `Blood_Immunology`, `Cell_types` | `t-lymphocyte`, `T cell`, `lymphocyte`, `CTL` |
| CAR T cell | `Blood_Immunology`, `Receptors_channels`, `Cell_membrane` | Search T cell and receptor separately; compose them |
| B lymphocyte | `Blood_Immunology`, `Cell_types` | `b-lymphocyte`, `B cell`, `lymphocyte` |
| Macrophage / monocyte | `Blood_Immunology`, `Cell_types` | `macrophage`, `monocyte`, `phagocyte` |
| Dendritic cell | `Blood_Immunology`, `Cell_types` | `dendritic-cell`, `antigen presenting cell` |
| Neutrophil / granulocyte | `Blood_Immunology`, `Cell_types` | `neutrophil`, `granulocyte`, `polymorphonuclear` |
| Red blood cell | `Blood_Immunology`, `Cell_types` | `erythrocyte`, `redbloodcell`, `red blood cell` |
| Endothelial cell | `Human_physiology`, `Tissues`, `Cell_types` | `capillary`, `capillaries`, `Continuous_capillary`, `endothelium` |
| Blood vessel / transport | `Human_physiology`, `Tissues` | `artery`, `vein`, `capillary`, `blood-flow`, `bloodstream` |
| Epithelium | `Tissues`, `Microbiology`, `Human_physiology` | `epithelium`, `Epithelial_cells`, `epidermis`, `gobelet` |
| Tumor / cancer cell | `Oncology`, `Blood_Immunology`, `Cell_lines` | `tumor`, `cancer_cell`, `cancerous-cell`, `malignant` |
| HER2 or another receptor | `Receptors_channels`, `Cell_membrane`, `Oncology` | Search receptor scaffold, then label the specific target |
| Mouse | `Animals` | `Mouse`, `mouse-gray`, `mouse-small`; exclude embryo, head, organ, and procedure variants for a whole animal |
| Other model organism | `Animals`, then `Procedures` | Species name, common name, developmental stage only when requested |
| Bacterium | `Microbiology` | Species name, `bacterium`, `rod`, `coccus`, Gram class |
| Fungi / yeast | `Microbiology`, `Genetics`, `Plants_Algae` | `Fungal_cells`, `Yeast`, `mycelium`, `conidia`, `germlings` |
| Virus | `Viruses`, `Microbiology` | Virus family, virion, capsid, envelope |
| Parasite | `Parasites`, `Microbiology` | Species and life-cycle stage |
| Organ | `Human_physiology`, `Tissues` | Organ name plus view, section, healthy/disease state |
| Organelle | `Intracellular_components`, `Cell_types` | Organelle name, membrane, cytoskeleton component |
| DNA / RNA / gene | `Nucleic_acids`, `Genetics`, `Genomics` | Molecule name, helix, chromosome, editing action |
| Protein / peptide / molecule | `Peptides`, `Amino-Acids`, `Chemistry`, `Molecular_modelling` | Molecular name, structure class, reaction role |
| Lab instrument | `Lab_apparatus`, `Cell_culture`, `Imaging`, `Microbiology` | Instrument name and container form |
| Nanoparticle / carrier | `Nanotechnology`, `Cell_membrane`, `Chemistry` | nanoparticle, vesicle, liposome, carrier |
| Scientific plot | `Scientific_graphs` | plot family: line, violin, heatmap, survival, bar |

## 3. Full-search protocol

For each required entity family:

1. Call `nanadraw_search_bioicons` with the scientific term.
2. Route the concept using the table above; search the primary category and all
   relevant fallbacks with aliases, singular/plural forms, and filename forms.
   The local grounder accepts common Chinese entity names and expands them to
   the English Bioicons vocabulary; keep the original Chinese label separately
   for the final figure.
3. Run `scripts/bioicons_asset_grounder.py` without a category filter so its
   concept profile can scan all 2,804 records. Use `--category` only to inspect a
   routed category in depth, never to hide unexplored categories.
4. Use `--exclude` for state, species, or view constraints such as `embryo`,
   `head`, or `cross section`.
5. Generate `--preview-dir`; inspect every top candidate's full silhouette at
   approximately final figure size. Names and scores are shortlist evidence,
   not selection evidence.
6. Record selected and rejected IDs with match quality, anatomy decision,
   author, license, source, and reuse mode.
7. Use standalone asset generation only after all routed categories and
   semantic aliases have been searched and each top candidate has a concrete
   rejection reason.

Example:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
LOCAL_PATH `
  "$skill\scripts\bioicons_asset_grounder.py" `
  --root LOCAL_PATH `
  --query "endothelial cell" `
  --query "red blood cell" `
  --query "CAR T cell" `
  --query mouse `
  --exclude embryo `
  --limit 8 `
  --output ASSET_SHORTLIST.json `
  --preview-dir ASSET_PREVIEWS
```

## 4. Composite scientific objects

Do not expect every scientific concept to exist as one icon. Compose these
objects from canonical parts while keeping each part editable:

- `CAR T cell`: T-lymphocyte + membrane receptor + binding domain + target label.
- `HER2-positive tumor`: tumor cell + repeated receptor scaffolds + `HER2` label.
- `vascular trafficking`: capillary/endothelium + erythrocytes + leukocyte +
  directional flow and transmigration arrows.
- `drug-loaded carrier`: vesicle or nanoparticle + payload molecules + membrane
  interaction or release connector.
- `engineered cell`: canonical cell + edited receptor, gene cassette, cargo, or
  surface chemistry rather than a generic decorated sphere.

The composition must preserve molecular topology. A receptor needs an
extracellular domain, membrane-spanning segment, and intracellular domain when
those parts matter to the mechanism.

## 5. Match-quality decisions

The grounder emits `exact`, `strong_semantic`, `semantic`, or `partial`, plus
`match_reasons` and category routing. Use the score only to order inspection.

- `direct_reuse`: recognizable identity, suitable silhouette and orientation.
- `contour_adaptation`: correct anatomy but incompatible palette or interior.
- `visual_grammar_reference`: useful anatomy only; redraw in native primitives.
- `reject`: wrong entity, wrong state, wrong species/view, malformed anatomy, or
  unreadable at final size.

A partial candidate is often valuable for a composite, but it must not silently
replace the requested entity. For example, a capillary is a strong source for
an endothelial layer, while an embryo with a generic `cell` token is unrelated.

### Mouse candidate families

- `Animals/Servier/mouse-gray`, `mouse-cyan`, and related palette variants use
  clean layered journal-style vectors and are usually the best starting point
  for a Nature-style mechanism figure. Select body state and color by preview.
- `Animals/DBCLS/Mouse` has a detailed textured appearance. Use it only when the
  rest of the figure supports that detail density.
- `Animals/Ben-Murrell/Mouse` is a strong black silhouette. Use it for compact
  cohort or model markers, not when facial, limb, paw, and fur anatomy need to
  remain visible.
- Reject `mouse-embryo*`, `SmilingMouseHead`, tissue-specific `mousekidney*`, and
  procedure scenes when the requested object is a whole adult laboratory mouse.

