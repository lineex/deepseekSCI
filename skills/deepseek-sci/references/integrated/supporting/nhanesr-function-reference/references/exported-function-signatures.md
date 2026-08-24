# Integrated supporting reference: nhanesr-function-reference/references/exported-function-signatures.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/exported-function-signatures.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Exported Function Signatures

### `%=%`

```r
%=%(a, b)
```

### `DSD`

```r
DSD(data, years, prebiotic = FALSE, probiotic = FALSE, synbiotic = F, component = F, Year = F, join = "left")
```

### `DataDist`

```r
DataDist(..., data, q.display, q.effect = c(0.25, 0.75), adjto.cat = c("mode", "first"), n.unique = 10)
```

### `Drug`

```r
Drug(..., data = NULL, years, take_drug = "take_drug", DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = T, dup.take.drug = c("remove", "paste", "keep"), join = "left", Year = FALSE)
```

### `Factor`

```r
Factor(x)
```

### `Flavonoids_download`

```r
Flavonoids_download()
```

### `Frailty49`

```r
Frailty49()
```

### `Full_Join`

```r
Full_Join(..., by = "seqn", cat = TRUE, inspect = NULL)
```

### `Inner_Join`

```r
Inner_Join(..., by = "seqn", cat = TRUE, inspect = NULL)
```

### `Left_Join`

```r
Left_Join(..., by = "seqn", cat = TRUE, inspect = NULL)
```

### `Qnplot`

```r
Qnplot(..., xlab = NULL, ylab = NULL, skip = 0, linewidth = 0.9, axis.text.size = 10, axis.label.size = 12, legend.text.size = 9.5, legend.position = "right", strip.text.size = 10, file = NULL, width = par("din")[1], height = par("din")[2], unit = "in", dpi = 300)
```

### `RCS`

```r
RCS(..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.95, ref.zero = TRUE, log = TRUE)
```

### `Recode`

```r
Recode(x, ..., string = TRUE, cat = TRUE, to.numeric = FALSE, order = F)
```

### `Right_Join`

```r
Right_Join(..., by = "seqn", cat = TRUE, inspect = NULL)
```

### `add_col`

```r
add_col(data, colname = NULL, value = NULL, condition = NULL, position = NULL)
```

### `ageAdjust`

```r
ageAdjust(design, agecat = NULL, population = NULL, disease = NULL, mean_var = NULL, by = NULL, subset = NULL)
```

### `aggregate_max`

```r
aggregate_max(data, x, by, na.rm = T)
```

### `aggregate_mean`

```r
aggregate_mean(data, x, by, na.rm = T)
```

### `aggregate_min`

```r
aggregate_min(data, x, by, na.rm = T)
```

### `aggregate_sum`

```r
aggregate_sum(data, x, by, na.rm = T)
```

### `append<-`

```r
append<-(x, value)
```

### `bind_col`

```r
bind_col(df)
```

### `browse_rxq_Drug`

```r
browse_rxq_Drug()
```

### `browse_rxq_Rx`

```r
browse_rxq_Rx(years)
```

### `browser.fndds`

```r
browser.fndds()
```

### `browser.fped`

```r
browser.fped()
```

### `browser.survey`

```r
browser.survey()
```

### `bu`

```r
bu(x, rule)
```

### `bu_above.equal`

```r
bu_above.equal(x, n)
```

### `bu_lower.equal`

```r
bu_lower.equal(x, n)
```

### `build_codebook`

```r
build_codebook(progress = T)
```

### `build_varLabel`

```r
build_varLabel(progress = TRUE)
```

### `census_2000.All.ages`

```r
census_2000.All.ages()
```

### `census_2010.All.ages`

```r
census_2010.All.ages()
```

### `census_range`

```r
census_range(..., sum = FALSE)
```

### `census_range.2010`

```r
census_range.2010(..., sum = FALSE)
```

### `character2numeric`

```r
character2numeric(x)
```

### `check1`

```r
check1(x)
```

### `col.counts`

```r
col.counts(data)
```

### `col.max`

```r
col.max(data)
```

### `col.means`

```r
col.means(data, na.rm = TRUE)
```

### `col.sums`

```r
col.sums(data, na.rm = TRUE)
```

### `col_rename`

```r
col_rename(data, ...)
```

### `col_rename<-`

```r
col_rename<-(x, value)
```

### `config_items`

```r
config_items(items)
```

### `config_path`

```r
config_path(path)
```

### `config_temp`

```r
config_temp()
```

### `config_years`

```r
config_years(cat = T)
```

### `create_diag_MASLD.cap`

```r
create_diag_MASLD.cap(version = 2)
```

### `crude.Model.n`

```r
crude.Model.n(..., round = 2, xlsx = NULL, style = 1, character2integer = TRUE, quadratic = FALSE, browseXLSX = TRUE)
```

### `cut_headtail`

```r
cut_headtail(x, col, ..., cat = T)
```

### `db_Alcohol.drinks`

```r
db_Alcohol.drinks(data, years, Year = FALSE, join = "left")
```

### `db_DSD`

```r
db_DSD(..., data, supplement_name = TRUE, supplement_type = TRUE, ingredient_name = TRUE, ingredient_unit = TRUE, ingredient_category = TRUE, blend_flag = TRUE, blend_component_name = TRUE, blend_component_category = TRUE, Year = FALSE, join = "left")
```

### `db_EVD68`

```r
db_EVD68(data = NULL, all = FALSE, years, wt_y2, wt_y4, d68_frm, d68_frmq, d68_953, d68_953q, d68_087, d68_087q, Year = F, join = "left")
```

### `db_FoodCD`

```r
db_FoodCD(data, short = TRUE, long = TRUE, lower_cd = FALSE)
```

### `db_HemalBiochemistry`

```r
db_HemalBiochemistry(data, years, fast_glucose_mg.dl = FALSE, fast_glucose_mmol.L = FALSE, refrige_glucose_mg.dl = FALSE, refrige_glucose_mmol.L = FALSE, fast_insulin_uu.ml = FALSE, fast_insulin_pmol.L = FALSE, HbA1c = FALSE, Alt = FALSE, Ast = FALSE, bilirubin_total_mg.dl = FALSE, bilirubin_total_umol.L = FALSE, alkaline_phosphatase_u.L = FALSE, protein_total_g.dl = FALSE, protein_total_g.L = FALSE, albumin_g.L = FALSE, albumin_g.dl = FALSE, globulin_g.dl = FALSE, globulin_g.L = FALSE, gamma_glutamyl_transferase_13u.l_iu.l = FALSE, creatinine_mg.dl = FALSE, creatinine_umol.L = FALSE, uric_acid_mg.dl = FALSE, uric_acid_umol.L = FALSE, blood_urea_nitrogen_mg.dl = FALSE, blood_urea_nitrogen_mmol.L = FALSE, sodium_mmol.L = FALSE, phosphorus_mg.dl = FALSE, phosphorus_mmol.L = FALSE, calcium_total_mg.dl = FALSE, calcium_total_mmol.L = FALSE, calcium_albumin_corrected_mg.dl = FALSE, calcium_albumin_corrected_mmol.L = FALSE, potassium_mmol.L = FALSE, iron_ug.dl = FALSE, iron_umol.L = FALSE, chloride_mmol.L = FALSE, osmolality_mosm.kg = FALSE, bicarbonate_mmol.L = FALSE, fast_triglyceride_mg.dl = FALSE, fast_triglyceride_mmol.L = FALSE, refrige_triglycerides_mg.dl = FALSE, refrige_triglycerides_mmol.L = FALSE, fast_total_cholesterol_mg.dl = FALSE, fast_total_cholesterol_mmol.L = FALSE, refrige_total_cholesterol_mg.dl = FALSE, refrige_total_cholesterol_mmol.L = FALSE, hdl_cholesterol_mmol.L = FALSE, hdl_cholesterol_mg.dl = FALSE, hdl_cholesterol_direct_mg.dl = FALSE, hdl_cholesterol_direct_mmol.L = FALSE, ldl_cholesterol_mmol.L = FALSE, ldl_cholesterol_mg.dl = FALSE, creatine_phosphokinase_cpk_iu.L = FALSE, follicle_stimulating_hormone_iu.L = FALSE, follicle_stimulating_hormone_miu.ml = FALSE, luteinizing_hormone_iu.L = FALSE, luteinizing_hormone_miu.ml = FALSE, ldh_lactate_dehydrogenase_u.L = FALSE, C_reactive_protein_mg.dl = FALSE, hs_C_reactive_protein_mg.L = FALSE, Year = FALSE, join = "left", wtsaf2yr = FALSE, wtsaf4yr = FALSE, all = FALSE)
```

### `db_IgE`

```r
db_IgE(all = FALSE, respondent.sequence.number, sIgE_ku.l, sIgE_cmt, dust.farinae_ku.l, dust.farinae_cmt, dust.pteronyssinus_ku.l, dust.pteronyssin_cmt, cat_ku.l, cat_cmt, dog_ku.l, dog_cmt, cockroach_ku.l, cockroach_cmt, alternaria_ku.l, alternaria_cmt, peanut_ku.l, peanut_cmt, egg_ku.l, egg_cmt, milk_ku.l, milk_cmt, ragweed_ku.l, ragweed_cmt, rye.grass_ku.l, rye.grass_cmt, bermuda.grass_ku.l, bermuda.grass_cmt, oak_ku.l, oak_cmt, birch_ku.l, birch_cmt, shrimp_ku.l, shrimp_cmt, aspergillus_ku.l, aspergillus_cmt, thistle_ku.l, thistle_cmt, mouse_ku.l, mouse_cmt, rat_ku.l, rat_cmt, join = "left")
```

### `db_MCD`

```r
db_MCD(data, lower_cd = FALSE)
```

### `db_Menopause`

```r
db_Menopause(data, years, Year = FALSE, join = "left")
```

### `db_PbCd`

```r
db_PbCd(data, years, blood_cadmium_ug.l, blood_cadmium_umol.l, blood_cadmium_comment_code, blood_lead_ug.dl, blood_lead_umol.l, blood_lead_comment_code, blood_mercury_total_ug.l, blood_mercury_total_umol.l, blood_mercury_total_comment_code, blood_manganese_ug.l, blood_manganese_umol.l, blood_manganese_comment_code, blood_selenium_ug.l, blood_selenium_umol.l, blood_selenium_comment_code, weight = FALSE, Year = FALSE, join = "left")
```

### `db_alpha.rb`

```r
db_alpha.rb(data, join = "left", Year = F)
```

### `db_alpha.rsv`

```r
db_alpha.rsv(data, join = "left", Year = F)
```

### `db_aux`

```r
db_aux(data, years, self_reported_better_ear = FALSE, self_reported_better_ear2 = FALSE, excessive_cerumen_left_ear = FALSE, impacted_cerumen_left_ear = FALSE, otoscopy_left_ear = FALSE, collapsing_ear_canals_left_ear = FALSE, other_ear_exam_abnormality_left = FALSE, normal_otoscopy_right_ear = FALSE, excessive_cerumen_right_ear = FALSE, impacted_cerumen_right_ear = FALSE, collapsing_ear_canals_right_ear = FALSE, comment_other_ear_exam_abnormality_right = FALSE, tympanic_right_middle_ear_pressure_dapa = FALSE, tympanic_right_physical_volume_cc = FALSE, tympanic_right_width = FALSE, tympanic_right_compliance = FALSE, tympanic_left_middle_ear_pressure_dapa = FALSE, tympanic_left_physical_volume_cc = FALSE, tympanic_left_width = FALSE, tympanic_left_compliance = FALSE, which_ear_tested_first = FALSE, audio_test_mode = FALSE, frequency_switch_to_manual_mode_left = FALSE, frequency_switch_to_manual_mode_right = FALSE, right_threshold_1000hz_db = FALSE, right_threshold_500hz_db = FALSE, right_threshold_1000hz_2nd_read_db = FALSE, right_threshold_2000hz_db = FALSE, right_threshold_3000hz_db = FALSE, right_threshold_4000hz_db = FALSE, right_threshold_6000hz_db = FALSE, right_threshold_8000hz_db = FALSE, left_threshold_1000hz_db = FALSE, left_threshold_500hz_db = FALSE, left_threshold_1000hz_2nd_read_db = FALSE, left_threshold_2000hz_db = FALSE, left_threshold_3000hz_db = FALSE, left_threshold_4000hz_db = FALSE, left_threshold_6000hz_db = FALSE, left_threshold_8000hz_db = FALSE, right_retest_threshold_1000hz_db = FALSE, right_retest_threshold_500hz_db = FALSE, right_retest_threshold_1000hz_2nd_read = FALSE, right_retest_threshold_2000hz_db = FALSE, right_retest_threshold_3000hz_db = FALSE, right_retest_threshold_4000hz_db = FALSE, right_retest_threshold_6000hz_db = FALSE, right_retest_threshold_8000hz_db = FALSE, left_retest_threshold_1000hz_db = FALSE, left_retest_threshold_500hz_db = FALSE, left_retest_threshold_1000_2nd_read = FALSE, left_retest_threshold_2000hz_db = FALSE, left_retest_threshold_3000hz_db = FALSE, left_retest_threshold_4000hz_db = FALSE, left_retest_threshold_6000hz_db = FALSE, left_retest_threshold_8000hz_db = FALSE, left_ear_quality_code = FALSE, right_ear_quality_code = FALSE, tympanogram_type_right_ear = FALSE, tympanogram_type_left_ear = FALSE, weight = FALSE, cat = TRUE, Year = FALSE, join = "left")
```

### `db_auxar1`

```r
db_auxar1(data, years, left = FALSE, right = FALSE, khz1 = FALSE, khz2 = FALSE, right_1khz = FALSE, right_2khz = FALSE, left_1khz = FALSE, left_2khz = FALSE, weight = FALSE, Year = FALSE, join = "left")
```

### `db_auxar2`

```r
db_auxar2(data, years, ear_tested = FALSE, sound_stimulus_level = FALSE, detected = FALSE, time = FALSE, compliance = FALSE, Year = FALSE, join = "left")
```

### `db_auxtym1`

```r
db_auxtym1(data, years, left = FALSE, right = FALSE, weight = FALSE, Year = FALSE, join = "left")
```

### `db_auxtym2`

```r
db_auxtym2(data, years, ear_tested = FALSE, pressure = FALSE, admittance = FALSE, Year = FALSE, join = "left")
```

### `db_auxwbr`

```r
db_auxwbr(data, years, ear_tested = FALSE, frequency = FALSE, absorbance = FALSE, Year = FALSE, join = "left")
```

### `db_beta.rsv.braycurtis`

```r
db_beta.rsv.braycurtis(data, join = "left", Year = F)
```

### `db_beta.rsv.unwunifrac`

```r
db_beta.rsv.unwunifrac(data, join = "left", Year = F)
```

### `db_beta.rsv.wunifrac`

```r
db_beta.rsv.wunifrac(data, join = "left", Year = F)
```

### `db_blood.pressure`

```r
db_blood.pressure(data, years, bpx = TRUE, dar = TRUE, n = 4, Year = FALSE, join = "left")
```

### `db_bodyMeasure`

```r
db_bodyMeasure(data, years, head_circumference_cm, arm_circumference_cm, upper_arm_length_cm, triceps_skinfold_mm, subscapular_skinfold_mm, sagittal_abdominal_diameter_1st_cm, sagittal_abdominal_diameter_2nd_cm, sagittal_abdominal_diameter_3rd_cm, sagittal_abdominal_diameter_4th_cm, average_sagittal_abdominal_diameter_cm, waist_circumference_cm, hip_circumference_cm, thigh_circumference_cm, upper_leg_length_cm, maximal_calf_circumference_cm, height_cm, recumbent_length_cm, Weight_kg, BMI_kg.m2, BMI_Category_Children.Adolescents, Year = FALSE, join = "left")
```

### `db_carotenoid`

```r
db_carotenoid(data, years, day = 1, both2days = TRUE, fun = "mean", all.5 = TRUE, component = FALSE, ds = TRUE, Year = FALSE, join = "left")
```

### `db_cbc`

```r
db_cbc(data, years, wbc_1000cells.ul, Lymphocyte_percent, Monocyte_percent, Segmented_neutrophils_percent, Eosinophils_percent, Basophils_percent, lymphocyte_number_1000cells.ul, Monocyte_number_1000cells.ul, Segmented_neutrophils_number_1000cells.ul, Eosinophils_number_1000cells.ul, Basophils_number_1000cells.ul, Red_blood_cell_count_MillionCells.uL, hemoglobin_g.dl, hematocrit, Mean_cell_volume_fL, Mean_cell_hemoglobin_pg, Mean_cell_hemoglobin_concentration_g.dL, Red_cell_distribution_width, Platelet_count_1000cells.uL, Mean_platelet_volume_fL, Year = FALSE, join = "left")
```

### `db_cfq`

```r
db_cfq(data, years, all = F, cfq_status = FALSE, language = FALSE, cerad_completion_status = FALSE, cerad_reason_not_complete = FALSE, cerad_score_trial_1_recall = FALSE, cerad_score_trial_2_recall = FALSE, cerad_score_trial_3_recall = FALSE, cerad_score_delayed_recall = FALSE, cerad_intrusion_word_count_trial_1 = FALSE, cerad_intrusion_word_count_trial_2 = FALSE, cerad_intrusion_word_count_trial_3 = FALSE, cerad_intrusion_word_count_recall = FALSE, animal_fluency_sample_practice_pretest = FALSE, animal_fluency_reason_not_done = FALSE, animal_fluency_score_total = FALSE, digit_symbol_sample_practice_pretest = FALSE, digit_symbol_reason_not_done = FALSE, digit_symbol_score = FALSE, Year = FALSE, join = "left")
```

### `db_coffee`

```r
db_coffee(data, years, day = 1, fun = c("mean", "alone", "sum"), both2days = TRUE, unit = c("gram", "kcal", "cup"), caffeinate = FALSE, sweeten = FALSE, fat = FALSE, milk = FALSE, cappuccino = FALSE, cuban = FALSE, espresso = FALSE, frappuccino = FALSE, latte = FALSE, macchiato = FALSE, mexican = FALSE, mocha = FALSE, turkish = FALSE, Year = FALSE, join = "left", food.code = NULL)
```

### `db_coffee.time`

```r
db_coffee.time(data = NULL, years, day = 1, Year = F, join = "left")
```

### `db_demo`

```r
db_demo(data, years, ageyr, agemth, sex, eth1, eth2, eth3, military, country_of_birth, citizenship, time_in_US, edu, in_school, marital, household_size, family_size, annual_household_income, annual_family_income, poverty, status, exam_month, wtint2yr, wtint4yr, wtmec2yr, wtmec4yr, psu_strat = TRUE, Year = FALSE, join = "left", lower_cd = FALSE)
```

### `db_dnmepi`

```r
db_dnmepi(data, all = FALSE, xy_estimation, horvathage, hannumage, skinbloodage, phenoage, gdf15mort, b2mmort, cystatincmort, timp1mort, admmort, pai1mort, leptinmort, packyrsmort, crpmort, loga1cmort, grimagemort, grimage2mort, horvathtelo, yangcell, zhangage, linage, weidnerage, vidalbraloage, dunedinpoam, cd8tpp, cd4tpp, nkcell, bcell, monopp, neupp, wtdn4yr, join = "left")
```

### `db_dr.ProcessedMeat`

```r
db_dr.ProcessedMeat(data, all = FALSE, years, day = 1, Year = F, pf_meat, pf_curedmeat, cured_redmeat, total_redmeat, pf_poult, unproc_poultry, cured_poultry, nug_pat_fil, total_proc_poultry, total_poultry, red_and_cured_1, red_and_processed_2, join = "left")
```

### `db_dr.alcoh.beverages`

```r
db_dr.alcoh.beverages(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.apple`

```r
db_dr.apple(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.bananas`

```r
db_dr.bananas(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.fdcd`

```r
db_dr.fdcd(data, years, Year = FALSE, lower = T)
```

### `db_dr.iceCream`

```r
db_dr.iceCream(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.live.microbes`

```r
db_dr.live.microbes(data, years, grams_Lo, grams_Med, grams_Hi, Year, join = "left")
```

### `db_dr.milk`

```r
db_dr.milk(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.nuts`

```r
db_dr.nuts(data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left")
```

### `db_dr.ssb`

```r
db_dr.ssb(data, years, day = 1, kcal = F, grams = F, Year = FALSE, join = "left")
```

### `db_driff`

```r
db_driff(data, years, day = 1, both2days = FALSE, fun = "mean", NA20 = F, wtdrd1 = FALSE, wtdr2d = FALSE, wtdr4yr = FALSE, rstz = FALSE, breast_fed_infant = FALSE, day_of_week = FALSE, combination_food_number = FALSE, combination_food_type = FALSE, time_of_eating_occasion_hh.mm = FALSE, meal_name = FALSE, source_of_food = FALSE, eaten_at_home = FALSE, grams = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_sfat_g = FALSE, total_mfat_g = FALSE, total_pfat_g = FALSE, cholesterol_mg = FALSE, vitamin_E_as_alpha_tocopherol_mg = FALSE, added_alpha_tocopherol_vitamin_E_mg = FALSE, retinol_mcg = FALSE, vitamin_A_rae_mcg = FALSE, alpha_carotene_mcg = FALSE, beta_carotene_mcg = FALSE, beta_cryptoxanthin_mcg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_B1_mg = FALSE, riboflavin_vitamin_B2_mg = FALSE, niacin_mg = FALSE, vitamin_B6_mg = FALSE, total_folate_mcg = FALSE, folic_acid_mcg = FALSE, food_folate_mcg = FALSE, folate_dfe_mcg = FALSE, vitamin_B12_mcg = FALSE, added_vitamin_B12_mcg = FALSE, vitamin_C_mg = FALSE, vitamin_K_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, theobromine_mg = FALSE, alcohol_g = FALSE, moisture_g = FALSE, sfa_4.0_butanoic_g = FALSE, sfa_6.0_hexanoic_g = FALSE, sfa_8.0_octanoic_g = FALSE, sfa_10.0_decanoic_g = FALSE, sfa_12.0_dodecanoic_g = FALSE, sfa_14.0_tetradecanoic_g = FALSE, sfa_16.0_hexadecanoic_g = FALSE, sfa_18.0_octadecanoic_g = FALSE, mfa_16.1_hexadecenoic_g = FALSE, mfa_18.1_octadecenoic_g = FALSE, mfa_20.1_eicosenoic_g = FALSE, mfa_22.1_docosenoic_g = FALSE, pfa_18.2_octadecadienoic_g = FALSE, pfa_18.3_octadecatrienoic_g = FALSE, pfa_18.4_octadecatetraenoic_g = FALSE, pfa_20.4_eicosatetraenoic_g = FALSE, pfa_20.5_eicosapentaenoic_g = FALSE, pfa_22.5_docosapentaenoic_g = FALSE, pfa_22.6_docosahexaenoic_g = FALSE, total_choline_mg = FALSE, number_of_days = FALSE, vitamin_D_d2_d3_mcg = FALSE, Year = FALSE, join = "left", group_sum = FALSE)
```

### `db_drtot`

```r
db_drtot(data, years, day = 1, fun = c("mean", "sum", "alone"), wtdrd1 = FALSE, wtdr4yr = FALSE, wtdr2d = FALSE, rstz = FALSE, breast_fed_infant = FALSE, day_of_week = FALSE, foods_number = FALSE, diet_on_special = FALSE, diet_wllh = FALSE, diet_lowfat = FALSE, diet_lowsalt = FALSE, diet_lowsugar = FALSE, diet_lowfiber = FALSE, diet_highfiber = FALSE, diet_diabetic = FALSE, diet_weightgain = FALSE, diet_lowcarbohydrate = FALSE, diet_highprotein = FALSE, diet_glutenfree = FALSE, diet_kidney = FALSE, diet_otherspecial = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_sfat_g = FALSE, total_mfat_g = FALSE, total_pfat_g = FALSE, cholesterol_mg = FALSE, vitamin_A_rae_mcg = FALSE, retinol_mcg = FALSE, carotene_re.1999 = FALSE, alpha_carotene_mcg = FALSE, beta_carotene_mcg = FALSE, beta_cryptoxanthin_mcg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_B1_mg = FALSE, riboflavin_vitamin_B2_mg = FALSE, niacin_mg = FALSE, vitamin_B6_mg = FALSE, total_folate_mcg = FALSE, folic_acid_mcg = FALSE, food_folate_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, vitamin_B12_mcg = FALSE, added_vitamin_B12_mcg = FALSE, vitamin_C_mg = FALSE, vitamin_D_d2_d3_mcg = FALSE, vitamin_E_as_alpha_tocopherol_mg = FALSE, added_alpha_tocopherol_vitamin_E_mg = FALSE, vitamin_K_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, theobromine_mg = FALSE, alcohol_g = FALSE, moisture_g = FALSE, sfa_4.0_butanoic_g = FALSE, sfa_6.0_hexanoic_g = FALSE, sfa_8.0_g = FALSE, sfa_10.0_g = FALSE, sfa_12.0_g = FALSE, sfa_14.0_g = FALSE, sfa_16.0_g = FALSE, sfa_18.0_g = FALSE, mfa_16.1_g = FALSE, mfa_18.1_g = FALSE, mfa_20.1_g = FALSE, mfa_22.1_g = FALSE, pfa_18.2_g = FALSE, pfa_18.3_g = FALSE, pfa_18.4_g = FALSE, pfa_20.4_g = FALSE, pfa_20.5_g = FALSE, pfa_22.5_g = FALSE, pfa_22.6_g = FALSE, compare_to_usual = FALSE, water_total_plain_g = FALSE, water_total_tap_g = FALSE, water_total_bottled_g = FALSE, water_plain_carbonated_g = FALSE, water_tap_source = FALSE, salt_type = FALSE, salt_added_frequency = FALSE, salt_used_in_preparation = FALSE, salt_used_at_table_yesterday = FALSE, shellfish = FALSE, clams = FALSE, clams_times = FALSE, crabs = FALSE, crabs_times = FALSE, crayfish = FALSE, crayfish_times = FALSE, lobsters = FALSE, lobsters_times = FALSE, mussels = FALSE, mussels_times = FALSE, oysters = FALSE, oysters_times = FALSE, scallops = FALSE, scallops_times = FALSE, shrimp = FALSE, shrimp_times = FALSE, other_shellfish = FALSE, other_shellfish_times = FALSE, unknown_shellfish = FALSE, unknown_shellfish_times = FALSE, refused_shellfish = FALSE, fish = FALSE, breaded_fish = FALSE, breaded_fish_times = FALSE, tuna = FALSE, tuna_times = FALSE, bass = FALSE, bass_times = FALSE, catfish = FALSE, catfish_times = FALSE, cod = FALSE, cod_times = FALSE, flatfish = FALSE, flatfish_times = FALSE, haddock = FALSE, haddock_times = FALSE, mackerel = FALSE, mackerel_times = FALSE, perch = FALSE, perch_times = FALSE, pike = FALSE, pike_times = FALSE, pollock = FALSE, pollock_times = FALSE, porgy = FALSE, porgy_times = FALSE, salmon = FALSE, salmon_times = FALSE, sardines = FALSE, sardines_times = FALSE, sea_bass = FALSE, sea_bass_times = FALSE, shark = FALSE, shark_times = FALSE, swordfish = FALSE, swordfish_times = FALSE, trout = FALSE, trout_times = FALSE, walleye = FALSE, walleye_times = FALSE, other_fish = FALSE, other_fish_times = FALSE, unknown_fish = FALSE, unknown_fish_times = FALSE, refused_fish = FALSE, Year = FALSE, both2days = TRUE, join = "left")
```

### `db_ds.manganese`

```r
db_ds.manganese(data, years, Year = FALSE, join = "left")
```

### `db_ds.melatonin`

```r
db_ds.melatonin(data, years, Year = FALSE, join = "left")
```

### `db_ds.silicon`

```r
db_ds.silicon(data, years, Year = FALSE, join = "left")
```

### `db_ds.zinc`

```r
db_ds.zinc(data, years, Year = FALSE, join = "left")
```

### `db_dsids`

```r
db_dsids(data, years, day = 1, fun = c("mean", "sum", "alone"), both2days = TRUE, supplement_name = FALSE, wtdrd1 = FALSE, wtdr2d = FALSE, rstz = FALSE, day_of_week = FALSE, location_supplement_originally_recorded = FALSE, language = FALSE, antacid_containing_calcium.magnesium = FALSE, matching_code = FALSE, reported_serving_size.label_serving_size = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monounsaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, vitamin_b12_mcg = FALSE, vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, iodine_mcg = FALSE, Year = FALSE, join = "left")
```

### `db_dsids.30`

```r
db_dsids.30(data, years, supplement_name = FALSE, was_container_seen = FALSE, matching_code = FALSE, antacid_calcium_supplement_or_both = FALSE, how_long_supplement_taken_days = FALSE, days_supplement_taken_past_30_days = FALSE, quantity_of_supplement_taken_daily = FALSE, dosage_form = FALSE, reported_serving_size.label_serving_size = FALSE, antacid_reported_as_a_dietary_supplement = FALSE, energy_kcal = FALSE, carbohydrate_g = FALSE, protein_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monounsaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_ug = FALSE, lutein_zeaxanthin_ug = FALSE, thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_ug = FALSE, folate_dfe_ug = FALSE, total_choline_mg = FALSE, vitamin_b12_ug = FALSE, vitamin_c_mg = FALSE, vitamin_k_ug = FALSE, vitamin_d_d2_d3_ug = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_ug = FALSE, caffeine_mg = FALSE, iodine_ug = FALSE, reported_product_during_day_1 = FALSE, reported_product_during_day_2 = FALSE, took_product_on_own_or_doctor_advised = FALSE, for_good_bowel.colon_health = FALSE, for_prostate_health = FALSE, for_mental_health = FALSE, to_prevent_health_problems = FALSE, to_improve_my_overall_health = FALSE, for_teeth_prevent_cavities = FALSE, to_supplement_my_diet_food_not_enough = FALSE, to_stay_healthy = FALSE, to_prevent_colds_boost_immune_system = FALSE, for_heart_health_cholesterol = FALSE, for_eye_health = FALSE, for_healthy_joints_arthritis = FALSE, for_skin_health_dry_skin = FALSE, for_weight_loss = FALSE, for_bone_health = FALSE, to_get_more_energy = FALSE, for_pregnancy = FALSE, for_anemia_such_as_low_iron = FALSE, other_specify = FALSE, to_maintain_blood_sugar_diabetes = FALSE, for_healthy_hair_and_nails = FALSE, for_kidney_and_bladder_health = FALSE, for_respiratory_health_asthma = FALSE, for_allergies = FALSE, currently_breastfeeding = FALSE, to_improve_digestion = FALSE, for_menopause_hot_flashes = FALSE, for_muscle_related_issues = FALSE, to_improve_sleep = FALSE, for_nervous_system_health = FALSE, for_relaxation_decrease_stress = FALSE, for_liver_health_detoxification = FALSE, for_antioxidants = FALSE, for_word_of_mouth_advertisement = FALSE, for_thyroid_health_gout = FALSE, to_build_muscle.weight_gain = FALSE, for_low_levels_in_blood = FALSE, for_support_after_surgery = FALSE, for_headaches_and_dizziness = FALSE, to_build_muscle = FALSE, for_fluid.water_balance = FALSE, for_inflammation = FALSE, Year = FALSE, join = "left")
```

### `db_dstot`

```r
db_dstot(data, years, day = 1, fun = c("mean", "sum", "alone"), both2days = TRUE, wtdrd1 = FALSE, wtdr2d = FALSE, rstz = FALSE, number_of_days_of_intake = FALSE, day_of_week = FALSE, language = FALSE, main_respondent_for_this_interview = FALSE, helped_in_responding_for_this_interview = FALSE, any_dietary_supplements_taken = FALSE, number_of_dietary_supplements_reported = FALSE, any_antacids_taken = FALSE, number_of_antacids_reported = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monounsaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, vitamin_b12_mcg = FALSE, vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, number_of_days_bw_intake_and_hh_interview = FALSE, iodine_mcg = FALSE, Year = FALSE, join = "left")
```

### `db_dstot.30`

```r
db_dstot.30(data, years, any_dietary_supplements_taken = FALSE, total_number_of_dietary_supplements_taken = FALSE, any_antacids_taken = FALSE, total_number_of_antacids_taken = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monosaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, vitamin_b1_thiamin_mg = FALSE, vitamin_b2_riboflavin_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, vitamin_b12_mcg = FALSE, vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, iodine_mcg = FALSE, Year = FALSE, join = "left")
```

### `db_dxx`

```r
db_dxx(data, years, head_area_cm2 = FALSE, head_bmc_g = FALSE, head_bmd_g.cm2 = FALSE, head_fat_g = FALSE, head_lean_excl_bmc_g = FALSE, head_lean_incl_bmc_g = FALSE, head_total_g = FALSE, head_percent_fat = FALSE, left_arm_area_cm2 = FALSE, left_arm_bmc_g = FALSE, left_arm_bmd_g.cm2 = FALSE, left_arm_fat_g = FALSE, left_arm_lean_excl_bmc_g = FALSE, left_arm_lean_incl_bmc_g = FALSE, left_arm_total_g = FALSE, left_arm_percent_fat = FALSE, left_leg_area_cm2 = FALSE, left_leg_bmc_g = FALSE, left_leg_bmd_g.cm2 = FALSE, left_leg_fat_g = FALSE, left_leg_lean_excl_bmc_g = FALSE, left_leg_lean_incl_bmc_g = FALSE, left_leg_total_g = FALSE, left_leg_percent_fat = FALSE, right_arm_area_cm2 = FALSE, right_arm_bmc_g = FALSE, right_arm_bmd_g.cm2 = FALSE, right_arm_fat_g = FALSE, right_arm_lean_excl_bmc_g = FALSE, right_arm_lean_incl_bmc_g = FALSE, right_arm_total_g = FALSE, right_arm_percent_fat = FALSE, right_leg_area_cm2 = FALSE, right_leg_bmc_g = FALSE, right_leg_bmd_g.cm2 = FALSE, right_leg_fat_g = FALSE, right_leg_lean_excl_bmc_g = FALSE, right_leg_lean_incl_bmc_g = FALSE, right_leg_total_g = FALSE, right_leg_percent_fat = FALSE, left_ribs_area_cm2 = FALSE, left_ribs_bmc_g = FALSE, left_ribs_bmd_g.cm2 = FALSE, right_ribs_area_cm2 = FALSE, right_ribs_bmc_g = FALSE, right_ribs_bmd_g.cm2 = FALSE, thoracic_spine_area_cm2 = FALSE, thoracic_spine_bmc_g = FALSE, thoracic_spine_bmd_g.cm2 = FALSE, lumbar_spine_area_cm2 = FALSE, lumbar_spine_bmc_g = FALSE, lumbar_spine_bmd_g.cm2 = FALSE, pelvis_area_cm2 = FALSE, pelvis_bmc_g = FALSE, pelvis_bmd_g.cm2 = FALSE, trunk_bone_area_cm2 = FALSE, trunk_bmc_g = FALSE, trunk_bone_bmd_g.cm2 = FALSE, trunk_fat_g = FALSE, trunk_lean_excl_bmc_g = FALSE, trunk_lean_incl_bmc_g = FALSE, trunk_totalg = FALSE, trunk_percent_fat = FALSE, subtotal_area_cm2 = FALSE, subtotal_bmc_g = FALSE, subtotal_bmd_g.cm2 = FALSE, subtotal_fat_g = FALSE, subtotal_lean_excl_bmc_g = FALSE, subtotal_lean_incl_bmc_g = FALSE, subtotal_total_excl_head_g = FALSE, subtotal_percent_fat = FALSE, total_area_cm2 = FALSE, total_bmc_g = FALSE, total_bmd_g.cm2 = FALSE, total_fat_g = FALSE, total_lean_excl_bmc_g = FALSE, total_lean_incl_bmc_g = FALSE, total_lean_plus_fat_g = FALSE, total_percent_fat = FALSE, mult.fun = c("mean", "median", "unique"), Year = FALSE, join = "left")
```

### `db_dxxag`

```r
db_dxxag(data, years, android_fat_mass = FALSE, android_lean_mass = FALSE, android_total_mass = FALSE, gynoid_fat_mass = FALSE, gynoid_lean_mass = FALSE, gynoid_total_mass = FALSE, android_to_gynoid_ratio = FALSE, android_percent_fat = FALSE, gynoid_percent_fat = FALSE, subcutaneous_fat_area = FALSE, subcutaneous_fat_mass = FALSE, subcutaneous_fat_volume = FALSE, total_abdominal_fat_area = FALSE, total_abdominal_fat_mass = FALSE, total_abdominal_fat_volume = FALSE, visceral_adipose_tissue_area = FALSE, visceral_adipose_tissue_mass = FALSE, visceral_adipose_tissue_volume = FALSE, Year = FALSE, join = "left")
```

### `db_dxxfem`

```r
db_dxxfem(data, years, total_femur_area_cm2 = FALSE, total_femur_bmc_g = FALSE, total_femur_bmd_g.cm2 = FALSE, femoral_neck_area_cm2 = FALSE, femoral_neck_bmc_g = FALSE, femoral_neck_bmd_g.cm2 = FALSE, trochanter_area_cm2 = FALSE, trochanter_bmc_g = FALSE, trochanter_bmd_g.cm2 = FALSE, intertrochanter_area_cm2 = FALSE, intertrochanter_bmc_g = FALSE, intertrochanter_bmd_g.cm2 = FALSE, ward_triangle_area_cm2 = FALSE, ward_triangle_bmc_g = FALSE, ward_triangle_bmd_g.cm2 = FALSE, calculated_k_for_femur = FALSE, calculated_do_for_femur = FALSE, Year = FALSE, join = "left")
```

### `db_dxxspn`

```r
db_dxxspn(data, years, total_spine_area_cm2 = FALSE, total_spine_bmc_g = FALSE, total_spine_bmd_g.cm2 = FALSE, l1_area_cm2 = FALSE, l1_bmc_g = FALSE, l1_bmd_g.cm2 = FALSE, l2_area_cm2 = FALSE, l2_bmc_g = FALSE, l2_bmd_g.cm2 = FALSE, l3_area_cm2 = FALSE, l3_bmc_g = FALSE, l3_bmd_g.cm2 = FALSE, l4_area_cm2 = FALSE, l4_bmc_g = FALSE, l4_bmd_g.cm2 = FALSE, calculated_k_for_spine = FALSE, calculated_d0_for_spine = FALSE, total_trabecular_bone_score = FALSE, l1_tbs = FALSE, l2_tbs = FALSE, l3_tbs = FALSE, l4_tbs = FALSE, Year = FALSE, join = "left")
```

### `db_eating.occasion`

```r
db_eating.occasion(years, day = 1)
```

### `db_flavonoids`

```r
db_flavonoids(data, years, dietary = c("tot", "iff"), day = 1, fun = c("mean", "sum", "alone"), Daidzein_mg = FALSE, Genistein_mg = FALSE, Glycitein_mg = FALSE, Cyanidin_mg = FALSE, Petunidin_mg = FALSE, Delphinidin_mg = FALSE, Malvidin_mg = FALSE, Pelargonidin_mg = FALSE, Peonidin_mg = FALSE, Catechin_mg = FALSE, Epigallocatechin_mg = FALSE, Epicatechin_mg = FALSE, Epicatechin_3_gallate_mg = FALSE, Epigallocatechin_3_gallate_mg = FALSE, Theaflavin_mg = FALSE, Thearubigins_mg = FALSE, Eriodictyol_mg = FALSE, Hesperetin_mg = FALSE, Naringenin_mg = FALSE, Apigenin_mg = FALSE, Luteolin_mg = FALSE, Isorhamnetin_mg = FALSE, Kaempferol_mg = FALSE, Myricetin_mg = FALSE, Quercetin_mg = FALSE, Theaflavin_3_3_digallate_mg = FALSE, Theaflavin_3q_gallate_mg = FALSE, Theaflavin_3_gallate_mg = FALSE, Gallocatechin_mg = FALSE, Subtotal_Catechins_mg = FALSE, Total_Isoflavones_mg = FALSE, Total_Anthocyanidins_mg = FALSE, Total_Flavan_3_ols_mg = FALSE, Total_Flavanones_mg = FALSE, Total_Flavones_mg = FALSE, Total_Flavonols_mg = FALSE, Total_Sum_of_all_29_flavonoids_mg = FALSE, both2days = TRUE, join = "left", Year = FALSE)
```

### `db_flxcln`

```r
db_flxcln(data, years, central_incisor = FALSE, lateral_incisor = FALSE, cuspid = FALSE, bicuspid1 = FALSE, bicuspid2 = FALSE, molar1 = FALSE, molar2 = FALSE, Year = FALSE, join = "left", lower_cd = TRUE)
```

### `db_fndds`

```r
db_fndds(data, years, files, Year = FALSE, join = "left", nrow = Inf)
```

### `db_fped`

```r
db_fped(data, years, day = c("1", "2"), dietary = c("tot", "iff"), version = c("2015", "2010"), fun = c("sum", "mean"), f_citmlb = FALSE, f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, v_redor_tomato = FALSE, v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, seaplant = FALSE, addsugc = FALSE, solfatc = FALSE, vtotalleg = FALSE, vdrkgrleg = FALSE, pfallprotleg = FALSE, pfseaplantleg = FALSE, Year = F, join = "left")
```

### `db_hormone`

```r
db_hormone(data, years, testosterone_ng.dl = FALSE, free_testosterone_ng.dl = FALSE, bioavailable_testosterone_ng.dl = FALSE, sex_hormone_binding_globulin_nmol.l = FALSE, estradiol_pg.ml = FALSE, androstanedione_glucuronide_ng.ml = FALSE, Year = FALSE, join = "left")
```

### `db_mango`

```r
db_mango(data, years, day = 1, fun = c("mean", "alone", "sum"), both2days = TRUE, food.code = NULL, Year = FALSE, join = "left")
```

### `db_mort`

```r
db_mort(data, years, varLabel = TRUE, codebook = TRUE, Year = FALSE, join = "left")
```

### `db_muscle.strength`

```r
db_muscle.strength(data, years, grip_test_status = TRUE, ever_had_surgery_on_hands_or_wrists = TRUE, recent_pain_aching_stiffness_right_hand = TRUE, recent_pain_aching_stiffness_left_hand = TRUE, dominant_hand = FALSE, index_finger_90_degree = FALSE, testing_position = FALSE, hassigned_for_practice_trial = FALSE, begin_test_hand = FALSE, gs_t1_h1.kg = FALSE, gs_t1_h1_effort = FALSE, gs_t1_h2.kg = FALSE, gs_t1_h2_effort = FALSE, gs_t2_h1.kg = FALSE, gs_t2_h1_effort = FALSE, gs_t2_h2.kg = FALSE, gs_t2_h2_effort = FALSE, gs_t3_h1.kg = FALSE, gs_t3_h1_effort = FALSE, gs_t3_h2.kg = FALSE, gs_t3_h2_effort = FALSE, combined_grip_strength_kg = FALSE, Year = FALSE, join = "left")
```

### `db_nova`

```r
db_nova(data = NULL, all = FALSE, day = 1, years, unprocessed_minimal.grams, ingredients.grams, processed.grams, ultra_processed.grams, unprocessed_minimal.kcal, ingredients.kcal, processed.kcal, ultra_processed.kcal, Year = F, join = "left")
```

### `db_ogtt`

```r
db_ogtt(data, years, ogtt_subsample_2_year_mec_weight = FALSE, two_hour_glucose_ogtt_mg.dl = FALSE, two_hour_glucose_ogtt_mmol.l = FALSE, total_length_of_food_fast_hours = FALSE, total_length_of_food_fast_minutes = FALSE, glucose_challenge_administer_time_in_min = FALSE, time_from_fast_glucose_challenge_min = FALSE, time_from_fasting_glucose_ogtt_min = FALSE, time_from_glucose_challenge_ogtt_min = FALSE, amount_of_glucose_challenge_drank = FALSE, incomplete_ogtt_comment_code = FALSE, Year = FALSE, join = "left")
```

### `db_ohxden`

```r
db_ohxden(data, years, exam_status = FALSE, dental_implant = FALSE, dental_restoration = FALSE, dental_sealant = FALSE, root_cary = FALSE, other_root_lesion = FALSE, root_restoration = FALSE, other_root_restoration = FALSE, dental_decay = FALSE, edentulous = FALSE, tooth_condition = FALSE, coronal_cary_tooth = FALSE, coronal_cary_surface = FALSE, coronal_caries_2nd_restoration_sc = FALSE, coronal_caries_2nd_restoration_tc = FALSE, sealants = FALSE, foc = FALSE, label = FALSE, Year = FALSE, join = "left")
```

### `db_sandwiches`

```r
db_sandwiches(data, years, day = 1, fun = "mean", both2days = TRUE, unit = "gram", Year = FALSE, join = "left")
```

### `db_slq`

```r
db_slq(data, years, how_long_to_fall_asleep_minutes = FALSE, how_much_sleep_do_you_get_hours = FALSE, ever_told_doctor_had_trouble_sleeping = FALSE, ever_told_by_doctor_have_sleep_disorder = FALSE, sleep_disorder_sleep_apnea = FALSE, sleep_disorder_insomnia = FALSE, sleep_disorder_restless_legs = FALSE, sleep_disorder_other = FALSE, how_often_do_you_snore = FALSE, how_often_do_you_snort_or_stop_breathing = FALSE, how_often_have_trouble_falling_asleep = FALSE, how_often_wake_up_during_night = FALSE, how_often_wake_up_too_early_in_morning = FALSE, how_often_feel_unrested_during_the_day = FALSE, how_often_feel_overly_sleepy_during_day = FALSE, how_often_did_you_not_get_enough_sleep = FALSE, how_often_take_pills_to_help_you_sleep = FALSE, how_often_have_leg_jerks_while_sleeping = FALSE, how_often_have_legs_cramp_while_sleeping = FALSE, difficulty_concentrating_when_tired = FALSE, difficulty_remembering_when_tired = FALSE, difficulty_eating_when_tired = FALSE, difficulty_with_a_hobby_when_tired = FALSE, difficulty_getting_things_done = FALSE, difficulty_with_finance_when_tired = FALSE, difficulty_at_work_because_tired = FALSE, difficulty_on_phone_when_tired = FALSE, usual_sleep_time_on_weekdays_or_workdays = FALSE, usual_wake_time_on_weekdays_or_workdays = FALSE, sleep_hours_weekdays_or_workdays = FALSE, usual_sleep_time_on_weekends = FALSE, usual_wake_time_on_weekends = FALSE, sleep_hours_weekends = FALSE, Year = FALSE, join = "left")
```

### `db_sprint`

```r
db_sprint(data, years, Year = FALSE, join = "left")
```

### `db_spx`

```r
db_spx(data, years, test_status_first, test_comment_first, fvc_baseline_ml, extrapolated_volume_baseline_ml, fev_0.5_baseline_ml, fev_0.75_baseline_ml, fev_1_baseline_ml, fev_3_baseline_ml, fev_6_baseline_ml, pef_baseline_ml.s, fef_25.75_baseline_ml.s, forced_expiratory_time_baseline_s, fvc_quality_attribute_baseline, fev1_quality_attribute_baseline, number_of_acceptable_curves_baseline, effort_quality_attribute_baseline, selected_for_bronchodilator, spirometry_second_test_status, spirometry_second_test_comment, fvc_2nd_ml, extrapolated_volume_2nd_ml, fev_0.5_2nd_ml, fev_0.75_2nd_ml, fev_1_2nd_ml, fev_3_2nd_ml, fev_6_2nd_ml, pef_2nd_ml.s, fef_25.75_2nd_ml.s, forced_expiratory_time_2nd_s, fvc_quality_attribute_2nd, fev1_quality_attribute_2nd, number_of_acceptable_curves_2nd, effort_quality_attribute_2nd, Year = FALSE, join = "left")
```

### `db_tea`

```r
db_tea(data, years, day = 1, fun = c("mean", "alone", "sum"), unit = c("gram", "kcal", "cup"), sweeten = FALSE, caffeinate = FALSE, green = FALSE, black = FALSE, oolong = FALSE, iced = FALSE, hot = FALSE, normT = FALSE, leaf = FALSE, instant = FALSE, bottle = FALSE, both2days = TRUE, food.code = NULL, Year = FALSE, join = "left")
```

### `db_urine.alb.cr`

```r
db_urine.alb.cr(data, years, albumin_urine_mg.l = FALSE, albumin_urine_ug.ml = FALSE, creatinine_urine_mg.dl = FALSE, creatinine_urine_umol.l = FALSE, uACR_mg.g = FALSE, Year = FALSE, join = "left")
```

### `design4matchit`

```r
design4matchit(design)
```

### `dex_ABPI`

```r
dex_ABPI(data, years, left_abpi = TRUE, right_abpi = TRUE, Year = FALSE, join = "left")
```

### `dex_ABSI`

```r
dex_ABSI(data, years, Year = FALSE, join = "left")
```

### `dex_AHA.PREVENT`

```r
dex_AHA.PREVENT(data, years, CVD_10yr.risk = F, ASCVD_10yr.risk = F, HF_10yr.risk = F, component = F, Year = F, join = "left")
```

### `dex_AIP`

```r
dex_AIP(data = NULL, years, weight = FALSE, Year = FALSE, join = "left", cat = TRUE)
```

### `dex_ASCVD.h10yr`

```r
dex_ASCVD.h10yr(data, years, age = "[40,79]", restrict.Race = TRUE, component = FALSE, weight = FALSE, Year = FALSE, join = "left")
```

### `dex_BARD`

```r
dex_BARD(data, years, Year = FALSE, join = "left")
```

### `dex_BRI`

```r
dex_BRI(data, years, Year = FALSE, join = "left")
```

### `dex_BiologicalAge`

```r
dex_BiologicalAge(data, biomarkers = NULL, by = NULL)
```

### `dex_CALLY`

```r
dex_CALLY(data, years, all = FALSE, CALLY = T, crp, alb, lym, Year = F, join = "left")
```

### `dex_CCI`

```r
dex_CCI(data, years, cci_number = FALSE, Year = FALSE, join = "left")
```

### `dex_CDAI`

```r
dex_CDAI(data, years, day = 1, both2days = T, component = FALSE, Year = FALSE, join = "left", round = 3)
```

### `dex_CMDS`

```r
dex_CMDS(data, years, weight = FALSE, Year = FALSE, join = "left")
```

### `dex_CMI`

```r
dex_CMI(data, years, CMI, tg_mmol.L, hdl_mmol.L, WHtR, Year = FALSE, join = "left")
```

### `dex_CONUT`

```r
dex_CONUT(data, years, Year = FALSE, join = "left")
```

### `dex_DASH.Mellen`

```r
dex_DASH.Mellen(data, years, day = 1, both2days = T, component = F, Year = FALSE, join = "left")
```

### `dex_DII`

```r
dex_DII(data, years, day = 1, rawComponet = FALSE, both2days = F, cat = TRUE, Year = FALSE, join = "left")
```

### `dex_DI_GM`

```r
dex_DI_GM(data, years, day = 1, score = F, component = F, Year = FALSE, join = "left")
```

### `dex_FIB.4`

```r
dex_FIB.4(data, years, Year = FALSE, join = "left")
```

### `dex_FLI`

```r
dex_FLI(data, years, Year = FALSE, join = "left")
```

### `dex_FS`

```r
dex_FS(data, years, Year = FALSE, join = "left", weight = FALSE)
```

### `dex_FSI`

```r
dex_FSI(data, years, Year = FALSE, join = "left", weight = FALSE)
```

### `dex_Frailty`

```r
dex_Frailty(data, years, component = FALSE)
```

### `dex_GNRI`

```r
dex_GNRI(data, years, cut, method = c("22", "105", "wlo"))
```

### `dex_GPS`

```r
dex_GPS(data, years, Year = FALSE, join = "left")
```

### `dex_HEI`

```r
dex_HEI(data, years, version = c("2015", "2010"), method = c("ssum", "pratio"), dietary = c("tot", "iff"), day = 1, both2days = F, varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, seed = NULL)
```

### `dex_HOMA`

```r
dex_HOMA(data, years, IR = TRUE, IS = TRUE, beta = TRUE, fglu = FALSE, finsulin = FALSE, Year = FALSE, join = "left")
```

### `dex_HSI`

```r
dex_HSI(data, years, Year = FALSE, join = "left")
```

### `dex_HeartAge`

```r
dex_HeartAge(data, years, CVD.10yr.risk = FALSE, component = FALSE, points_var = FALSE, Year = FALSE, join = "left")
```

### `dex_LAP`

```r
dex_LAP(data, years, Year = FALSE, join = "left")
```

### `dex_LC9`

```r
dex_LC9(data, years, day = 1, componet = FALSE, Year = FALSE, join = "left")
```

### `dex_LE8`

```r
dex_LE8(data, years, day = 1, componet = FALSE, Year = FALSE, join = "left")
```

### `dex_LS7`

```r
dex_LS7(data, years, count = FALSE, component_score = FALSE, component_raw = FALSE, hei_version = 2010, Year = FALSE, join = "left")
```

### `dex_MAO`

```r
dex_MAO(data, years, Year = FALSE, yes1 = FALSE, join = "left")
```

### `dex_METS.IR`

```r
dex_METS.IR(data, years, Year = FALSE, join = "left")
```

### `dex_METS.VF`

```r
dex_METS.VF(data, years, Year = FALSE, join = "left")
```

### `dex_MHO`

```r
dex_MHO(data, years, Year = FALSE, yes1 = FALSE, join = "left")
```

### `dex_MMII`

```r
dex_MMII(data = NULL, years, MMII = T, component = F, Year = F, join = "left")
```

### `dex_MQI`

```r
dex_MQI(data, years, MQI.total = TRUE, MQI.app = FALSE, MQI.arm = FALSE, ASM = FALSE, ASMI = FALSE, Year = FALSE, QC = TRUE, GF.dominant = FALSE, join = "left")
```

### `dex_MgDS`

```r
dex_MgDS(data, years, component = FALSE, Year = FALSE, join = "left")
```

### `dex_Muscle.strength`

```r
dex_Muscle.strength(data, years, activity = FALSE, times = FALSE, MET = FALSE, week = TRUE, Year = FALSE, join = "left")
```

### `dex_NAFLD.LFS`

```r
dex_NAFLD.LFS(data, years, Year = FALSE, Mets = c("IDF2006", "ATP", "IDF2009", "Harm"), join = "left", cat = TRUE, component = FALSE)
```

### `dex_NFS`

```r
dex_NFS(data, years, Year = FALSE, join = "left", weight = FALSE)
```

### `dex_NLR`

```r
dex_NLR(data = NULL, all = FALSE, years, NLR, Year = F, join = "left")
```

### `dex_NPS`

```r
dex_NPS(data, years, Year = FALSE, join = "left")
```

### `dex_OBS`

```r
dex_OBS(data, years, day = c(1, 2), OBS.dietary = FALSE, OBS.lifestyle = FALSE, component = FALSE, score = FALSE, Year = FALSE, join = "left", cat = T)
```

### `dex_PAiaf`

```r
dex_PAiaf(data, years, activity = FALSE, level = FALSE, times = FALSE, duration = FALSE, mets = FALSE, weight_type = FALSE, PA_iaf = FALSE, Year = FALSE, week = FALSE, join = "left")
```

### `dex_PLF`

```r
dex_PLF(data, years, Year = FALSE, join = "left")
```

### `dex_PLR`

```r
dex_PLR(data = NULL, all = FALSE, years, PLR = T, Year = F, join = "left")
```

### `dex_PRAL.NEAP`

```r
dex_PRAL.NEAP(data, years, day = 1, both2days = TRUE, fun = c("mean", "sum", "alone"), Year = FALSE, join = "left", component = FALSE)
```

### `dex_PhysicalActivity`

```r
dex_PhysicalActivity(data, years, all.5 = FALSE, walk_bicycle = FALSE, Tasks.HomeYard = FALSE, Muscle.strength = FALSE, WorkActivity = FALSE, RecreationalActivity = FALSE, activity = FALSE, time = FALSE, MET = FALSE, week = TRUE, direction = c("m", "v", "no"), total_time, total_MET, component = FALSE, Year = FALSE, join = "left")
```

### `dex_RecreationalActivity`

```r
dex_RecreationalActivity(data, years, activity = FALSE, time = FALSE, MET = FALSE, direction = c("m", "v", "no"), Year = FALSE, join = "left")
```

### `dex_SARC.F`

```r
dex_SARC.F(data, years, component = F, Year = FALSE, join = "left")
```

### `dex_SDoH`

```r
dex_SDoH(data, years, score = F, component = F, Year = F, join = "left")
```

### `dex_SHR`

```r
dex_SHR(data = NULL, years, SHR = T, glucose_mg.dL = F, HbA1c = F, Year = F, join = "left")
```

### `dex_SII`

```r
dex_SII(data, years, Year = FALSE, join = "left")
```

### `dex_Tasks.HomeYard`

```r
dex_Tasks.HomeYard(data, years, activity = FALSE, time = FALSE, MET = FALSE, week = TRUE, direction = c("m", "v", "no"), Year = FALSE, join = "left")
```

### `dex_TyG`

```r
dex_TyG(data, years, Year = FALSE, join = "left")
```

### `dex_VAI`

```r
dex_VAI(data, years)
```

### `dex_VAT`

```r
dex_VAT(data, years, Year = FALSE, join = "left")
```

### `dex_WHR`

```r
dex_WHR(data, years, Year = FALSE, join = "left")
```

### `dex_WHtR`

```r
dex_WHtR(data, years, Year = FALSE, join = "left")
```

### `dex_WorkActivity`

```r
dex_WorkActivity(data, years, activity = FALSE, time = FALSE, MET = FALSE, direction = c("m", "v", "no"), Year = FALSE, join = "left")
```

### `dex_YJP`

```r
dex_YJP(data, years, cut = 4, Year = FALSE, cat = TRUE, join = "left")
```

### `dex_ZJU`

```r
dex_ZJU(data, years, Year = FALSE, join = "left")
```

### `dex_body.fat.percentage`

```r
dex_body.fat.percentage(data, years, Year = FALSE, join = "left")
```

### `dex_eGDR`

```r
dex_eGDR(data = NULL, all = FALSE, years, eGDR = T, Year = F, join = "left")
```

### `dex_eGFR`

```r
dex_eGFR(data, years, method = "CKD_EPI_Scr_2009", Year = FALSE, join = "left")
```

### `dex_ePWV`

```r
dex_ePWV(data, years, Year = FALSE, join = "left", component = F)
```

### `dex_fasting.time`

```r
dex_fasting.time(data = NULL, years, day = 1, fasting.time = T, Year = F, join = "left")
```

### `dex_fat.mass`

```r
dex_fat.mass(data, years, Year = FALSE, join = "left")
```

### `dex_fii`

```r
dex_fii(data = NULL, all = FALSE, day = 1, years, Year = F, join = "left")
```

### `dex_lean.mass`

```r
dex_lean.mass(data, years, Year = FALSE, join = "left")
```

### `dex_phenoAge`

```r
dex_phenoAge(data, years, component = FALSE, Year = FALSE, join = "left")
```

### `dex_ulb`

```r
dex_ulb(data, years, component = FALSE, weight = FALSE, Year = FALSE, join = "left")
```

### `dex_usFLI`

```r
dex_usFLI(data, years, Year = FALSE, join = "left")
```

### `dex_walk_bicycle`

```r
dex_walk_bicycle(data, years, activity = FALSE, time = FALSE, MET = FALSE, week = TRUE, direction = c("m", "v", "no"), Year = FALSE, join = "left")
```

### `diag_ACO`

```r
diag_ACO(data, years, Year = FALSE, join = "left")
```

### `diag_ASCVD`

```r
diag_ASCVD(data, years, early_ASCVD = FALSE, early_male = 55, early_female = 60, Year = FALSE, join = "left")
```

### `diag_Anemia`

```r
diag_Anemia(data, years, Year = FALSE, join = "left")
```

### `diag_Asthma`

```r
diag_Asthma(data, years, told = TRUE, drug = TRUE, cat = TRUE, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_CKD`

```r
diag_CKD(data, years, ckd = c("A2", "G3a"), show_CKD = TRUE, show_prognosis = TRUE, show_ACR = FALSE, show_eGFR = FALSE, eGFR_method = "CKD_EPI_Scr_2009", yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_CKM`

```r
diag_CKM(data, years, component = F, Year = F, join = "left")
```

### `diag_COPD`

```r
diag_COPD(data, years, told = T, emphysema = TRUE, spx = TRUE, drug = TRUE, cat = TRUE, Year = FALSE, yes1 = FALSE, join = "left")
```

### `diag_CVD`

```r
diag_CVD(data, years, Year = FALSE, join = "left")
```

### `diag_DM`

```r
diag_DM(data, years, told = TRUE, HbA1c = TRUE, fast_glu = TRUE, OGTT2 = TRUE, rand_glu = TRUE, drug = TRUE, DM1 = FALSE, cat = TRUE, Year = FALSE, join = "left", exclude_Pregnant = TRUE)
```

### `diag_Familial.Hypercholesterolemia`

```r
diag_Familial.Hypercholesterolemia(data, years, class = TRUE, score = FALSE, Year = FALSE, join = "left")
```

### `diag_Fibrillation`

```r
diag_Fibrillation(data, years, Year = FALSE, join = "left")
```

### `diag_Hyperlipidemia`

```r
diag_Hyperlipidemia(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_Hypertension`

```r
diag_Hypertension(data, years, told = TRUE, drug = TRUE, bpx = TRUE, method = c("mean", "times"), systolic = 140, diastolic = 90, n = 3, component = FALSE, yes1 = FALSE, cat = TRUE, Year = FALSE, join = "left")
```

### `diag_MAFLD`

```r
diag_MAFLD(data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, CAP.cutoff = 248, above.equal = FALSE, cat = TRUE, Year = FALSE, join = "left")
```

### `diag_MAFLD.FLI`

```r
diag_MAFLD.FLI(data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, cutoff.FLI = NULL, cat = TRUE, Year = FALSE, join = "left")
```

### `diag_MAFLD.usFLI`

```r
diag_MAFLD.usFLI(data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, cutoff.usFLI = NULL, cat = TRUE, Year = FALSE, join = "left")
```

### `diag_MASLD.FLI`

```r
diag_MASLD.FLI(data, years, cutoff.FLI = NULL, Year = FALSE, join = "left")
```

### `diag_MASLD.cap`

```r
diag_MASLD.cap(data, years, cutoff.cap = 248, Year = FALSE, join = "left")
```

### `diag_MASLD.usFLI`

```r
diag_MASLD.usFLI(data, years, cutoff.usFLI = 30, Year = FALSE, join = "left")
```

### `diag_MetS`

```r
diag_MetS(data, years, methods = c("ATP", "IDF2006", "IDF2009", "Harm"), component = FALSE, yes1 = FALSE, join = "left", Year = FALSE, cat = TRUE)
```

### `diag_NAFLD`

```r
diag_NAFLD(data, years, cap.cutoff = 248, colname = "Nonalcoholic.fatty.liver.disease", Year = FALSE, join = "left")
```

### `diag_OSAS.3`

```r
diag_OSAS.3(data, years, Year = FALSE, join = "left", component = F)
```

### `diag_OSAS.3a`

```r
diag_OSAS.3a(data, years, Year = FALSE, join = "left", component = F)
```

### `diag_OSAS.3ha`

```r
diag_OSAS.3ha(data, years, Year = FALSE, join = "left", component = F)
```

### `diag_OSAS.MAP`

```r
diag_OSAS.MAP(data, years, Year = FALSE, join = "left", component = F)
```

### `diag_Overactive.bladder`

```r
diag_Overactive.bladder(data, years, Year = FALSE, join = "left")
```

### `diag_PAD`

```r
diag_PAD(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_PHQ9`

```r
diag_PHQ9(data, years, cut, na0 = FALSE, score = FALSE, dpq = FALSE, varLabel = FALSE, cat = T)
```

### `diag_Parkinson`

```r
diag_Parkinson(data, years, Year = FALSE, yes1 = FALSE, join = "left")
```

### `diag_Pregnant`

```r
diag_Pregnant(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_RMetS`

```r
diag_RMetS(data, years, component = F, Year = FALSE, join = "left")
```

### `diag_Resistant.hypertension`

```r
diag_Resistant.hypertension(data, years, systolic = 140, diastolic = 90, Year = FALSE, join = "left")
```

### `diag_Retinal.Emboli`

```r
diag_Retinal.Emboli(data, years, Year = FALSE, join = "left")
```

### `diag_alcohol.associated.liver.disease`

```r
diag_alcohol.associated.liver.disease(data, years, yes1 = FALSE, colname = "alcohol.associated.liver.disease", Year = FALSE, join = "left")
```

### `diag_alcohol.user`

```r
diag_alcohol.user(data, years, mild = c(1, 2), moderate = c(2, 3), heavy = c(3, 4), binge = TRUE, Year = FALSE, join = "left")
```

### `diag_angina`

```r
diag_angina(data, years, angina = TRUE, angina.Age = FALSE, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_arthritis`

```r
diag_arthritis(data, years, arthritis = FALSE, arghritis_age = FALSE, arghritis_type = FALSE, rheumatoid_arthritis, psoriatic_arthritis, osteoarthritis_or_degenerative_arthritis, Year = FALSE, join = "left")
```

### `diag_atopic`

```r
diag_atopic(data, cut.off = 0.35, component = F, Year = F)
```

### `diag_binge`

```r
diag_binge(data, years, month = TRUE, Year = FALSE, join = "left")
```

### `diag_congestive.heart.failure`

```r
diag_congestive.heart.failure(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_coronary.heart.disease`

```r
diag_coronary.heart.disease(data, years, coronary.heart.disease = TRUE, coronary.heart.disease.Age = FALSE, Year = FALSE, join = "left")
```

### `diag_epilepsy`

```r
diag_epilepsy(data, years, yes1 = FALSE, take_drug = FALSE, DrugNumber = FALSE, drugname = FALSE, remove.other = TRUE, dup.take.drug = c("paste", "remove", "keep"), Year = FALSE, join = "left")
```

### `diag_heart.attack`

```r
diag_heart.attack(data, years, heart.attack = TRUE, heart.attack.Age = FALSE, Year = FALSE, join = "left")
```

### `diag_hypoparathyroidism`

```r
diag_hypoparathyroidism(data, years, Year = FALSE, join = "left")
```

### `diag_icd10`

```r
diag_icd10(..., data, years, Year = FALSE, join = "left", colname = "target", yes1 = FALSE, icd10 = FALSE)
```

### `diag_infertility`

```r
diag_infertility(data, years, infertility_care = FALSE, Year = FALSE, join = "left")
```

### `diag_mFried.frailty`

```r
diag_mFried.frailty(data = NULL, all = FALSE, years, Fried.frailty, Fried.frailty_count, weakness, low.pa, exhaustion, slow.walking.speed, weight.change, Year = F, join = "left")
```

### `diag_osteoporosis`

```r
diag_osteoporosis(data, years, fem.neck.mean = 0.86, fem.neck.sd = 0.12, lum.mean = 1.064, lum.sd = 0.106, Tscore = FALSE, Year = FALSE, join = "left")
```

### `diag_periodontitis`

```r
diag_periodontitis(data, years, Year = FALSE, join = "left")
```

### `diag_periodontitis_CDC.AAP`

```r
diag_periodontitis_CDC.AAP(data, years, Year = FALSE, join = "left")
```

### `diag_preDM`

```r
diag_preDM(data, years, Year = FALSE, cat = TRUE, join = "left")
```

### `diag_sarcopenia`

```r
diag_sarcopenia(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_sarcopenia_low.muscle`

```r
diag_sarcopenia_low.muscle(data, years, yes1 = FALSE, Year = FALSE, join = "left")
```

### `diag_smoke`

```r
diag_smoke(data, years, smoke = T, start_age = F, quit_years = F, smoking_years = F, pack_years = F, cigarettes_per_day_when_quit = F, avg_cigarettes_per_day_past_30_days = F, anyone.smoke.in.home = F, days.used.nicotine.stop.smoking.aid_past5days = F, never = "never", former = "former", now = "now", Year = FALSE, join = "left")
```

### `diag_stroke`

```r
diag_stroke(data, years, stroke = TRUE, stroke.Age = FALSE, Year = FALSE, join = "left")
```

### `diag_viral.hepatitis`

```r
diag_viral.hepatitis(data, years, HBV = TRUE, HCV = TRUE, Year = FALSE, yes1 = FALSE, colname = "viral.hepatitis", join = "left")
```

### `diag_youth.hypertension`

```r
diag_youth.hypertension(data, years, levels = c("90th", "50th", "95th", "95th+"), Year = FALSE, join = "left")
```

### `diag_youth.obesity`

```r
diag_youth.obesity(data, years, Year = FALSE, join = "left")
```

### `digit2character`

```r
digit2character(x, round = 2)
```

### `digit2character<-`

```r
digit2character<-(x, value)
```

### `digit2numeric`

```r
digit2numeric(x, round = 2)
```

### `digit2numeric<-`

```r
digit2numeric<-(x, value)
```

### `dii`

```r
dii(component, x)
```

### `distinct`

```r
distinct(.data, ..., .keep_all = FALSE)
```

### `drop_col`

```r
drop_col(x, ...)
```

### `drop_col<-`

```r
drop_col<-(x, value)
```

### `drop_row`

```r
drop_row(x, ...)
```

### `drop_row<-`

```r
drop_row<-(x, value)
```

### `drop_row_high_percent`

```r
drop_row_high_percent(d, ..., percent = 97.5)
```

### `drop_row_low_percent`

```r
drop_row_low_percent(d, ..., percent = 2.5)
```

### `drug_anti.Diabetic`

```r
drug_anti.Diabetic(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_anti.Hyperlipidemic`

```r
drug_anti.Hyperlipidemic(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_anti.Hypertensive`

```r
drug_anti.Hypertensive(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_anti.infectives`

```r
drug_anti.infectives(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_anti.parkinson`

```r
drug_anti.parkinson(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code, other.code, no.code, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_fibrates`

```r
drug_fibrates(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_niacin`

```r
drug_niacin(data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, dup.take.drug = "remove", join = "left", Year = FALSE)
```

### `drug_search`

```r
drug_search(..., years = NULL)
```

### `each_id_first_row`

```r
each_id_first_row(data = NULL, ...)
```

### `each_id_last_row`

```r
each_id_last_row(data = NULL, ...)
```

### `fndds_AddFoodDesc`

```r
fndds_AddFoodDesc(..., data, years, start = NULL, Year = FALSE, join = "left")
```

### `fndds_DerivDesc`

```r
fndds_DerivDesc(data, years, Year = FALSE, join = "left")
```

### `fndds_FNDDSIngred`

```r
fndds_FNDDSIngred(data, years, Year = FALSE, join = "left")
```

### `fndds_FNDDSNutVal`

```r
fndds_FNDDSNutVal(data, years, Year = FALSE, join = "left")
```

### `fndds_FoodPortionDesc`

```r
fndds_FoodPortionDesc(data, years, Year = FALSE, join = "left")
```

### `fndds_FoodSubcodeLinks`

```r
fndds_FoodSubcodeLinks(data, years, Year = FALSE, join = "left")
```

### `fndds_FoodWeights`

```r
fndds_FoodWeights(data, years, Year = FALSE, join = "left")
```

### `fndds_IngredNutVal`

```r
fndds_IngredNutVal(data, years, Year = FALSE, join = "left")
```

### `fndds_MainFoodDesc`

```r
fndds_MainFoodDesc(..., data, years, start = NULL, Year = FALSE, abbr = TRUE, fortify = TRUE, wweia = TRUE, join = "left")
```

### `fndds_MoistAdjust`

```r
fndds_MoistAdjust(data, years, Year = FALSE, join = "left")
```

### `fndds_NutDesc`

```r
fndds_NutDesc(data, years, Year = FALSE, join = "left")
```

### `fndds_SubcodeDesc`

```r
fndds_SubcodeDesc(data, years, Year = FALSE, join = "left")
```

### `fndds_comp.food.Desc`

```r
fndds_comp.food.Desc(..., data, years, start = NULL, Year = FALSE, abbr = TRUE, fortify = TRUE, wweia = TRUE, add = TRUE, join = "left")
```

### `fndds_comp.food.Portion.Weight`

```r
fndds_comp.food.Portion.Weight(..., data, years, start = NULL, Year = FALSE, join = "left")
```

### `fndds_comp.nutrients`

```r
fndds_comp.nutrients(..., data, years, Year = FALSE, join = "left")
```

### `fndds_download`

```r
fndds_download()
```

### `fndds_file_colnames`

```r
fndds_file_colnames(files = NULL, years, view = TRUE)
```

### `fndds_file_names`

```r
fndds_file_names(view = TRUE)
```

### `fndds_food.code`

```r
fndds_food.code(years, cat = TRUE)
```

### `fndds_tsv`

```r
fndds_tsv(..., years, cat = TRUE)
```

### `food.code_used`

```r
food.code_used(d)
```

### `forestplot`

```r
forestplot(x, ...)
```

### `fped_download`

```r
fped_download()
```

### `fped_occasion`

```r
fped_occasion(data, years, day = 1, fun = c("sum", "mean"), occasion = c("Breakfast", "Lunch", "Dinner"), f_citmlb = FALSE, f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, v_redor_tomato = FALSE, v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, Year = FALSE, join = "left", cat = TRUE)
```

### `fped_read`

```r
fped_read(years, day = c("1", "2"), dietary = c("tot", "iff"), version = c("2010", "2015"), fun = c("sum", "mean"), cat = FALSE)
```

### `freq_count`

```r
freq_count(design, x, by = NULL, value = FALSE, per = FALSE, remove.name = FALSE, remove.suffix = FALSE, round = 2, file = NULL)
```

### `freq_mean`

```r
freq_mean(design, x, by = NULL, value = FALSE, sd = FALSE, low.high = FALSE, ci = FALSE, meanPMsd = FALSE, meanSQsd = FALSE, round = 2, na.rm = TRUE)
```

### `getChangepoints`

```r
getChangepoints(r, range = NULL)
```

### `getKnot`

```r
getKnot(fit)
```

### `getReference`

```r
getReference(r)
```

### `get_config_items`

```r
get_config_items()
```

### `get_config_path`

```r
get_config_path(slash = FALSE)
```

### `get_config_years`

```r
get_config_years(range = TRUE)
```

### `get_mort_path`

```r
get_mort_path()
```

### `group_mean`

```r
group_mean(d, vars = NULL, bys = NULL)
```

### `highlight`

```r
highlight(x, ..., colors = NULL)
```

### `html_URL`

```r
html_URL(x, href = NULL, name = NULL, target = "new")
```

### `ifel`

```r
ifel(...)
```

### `inset_both_frame`

```r
inset_both_frame()
```

### `inset_both_square`

```r
inset_both_square()
```

### `inset_exact_match`

```r
inset_exact_match()
```

### `inset_left_frame`

```r
inset_left_frame()
```

### `inset_left_square`

```r
inset_left_square()
```

### `inset_right_frame`

```r
inset_right_frame()
```

### `inset_right_square`

```r
inset_right_square()
```

### `ip_analysis`

```r
ip_analysis(fit, ip = NULL, round = 3, xlsx = NULL)
```

### `live_microbes_table`

```r
live_microbes_table()
```

### `look`

```r
look(x, ..., ignore.case = FALSE)
```

### `lookl`

```r
lookl(x, ..., ignore.case = TRUE, NA2false = FALSE)
```

### `matchit4design`

```r
matchit4design(design, matchit)
```

### `md.pattern`

```r
md.pattern(data)
```

### `md.value`

```r
md.value(data)
```

### `mdb_files`

```r
mdb_files(mdb)
```

### `missForest2`

```r
missForest2(d, ntree = 5, seed = 1)
```

### `missValue`

```r
missValue(data, ...)
```

### `mort_download`

```r
mort_download()
```

### `mort_read`

```r
mort_read(years, varLabel = FALSE, codebook = TRUE)
```

### `multibyteString`

```r
multibyteString(tsv)
```

### `newVb`

```r
newVb(df, ...)
```

### `nhanesR_startup_check`

```r
nhanesR_startup_check()
```

### `nhs.pubmed`

```r
nhs.pubmed(...)
```

### `nhs.pubmed_title`

```r
nhs.pubmed_title(...)
```

### `nhs_Connect`

```r
nhs_Connect(user = "postgres", password = "pg", dbname = "nhanes", host = "localhost", port = 5432, ...)
```

### `nhs_DOC`

```r
nhs_DOC(tsv)
```

### `nhs_Upload`

```r
nhs_Upload(files, conn)
```

### `nhs_brief`

```r
nhs_brief(...)
```

### `nhs_browse`

```r
nhs_browse(years, items, open = TRUE)
```

### `nhs_check`

```r
nhs_check(years, items)
```

### `nhs_codebook`

```r
nhs_codebook(..., tolower = FALSE)
```

### `nhs_colnames`

```r
nhs_colnames(..., brief = FALSE)
```

### `nhs_copy`

```r
nhs_copy(dir)
```

### `nhs_docFile_pc`

```r
nhs_docFile_pc(..., items, years, open = FALSE)
```

### `nhs_download`

```r
nhs_download(years, items, files, xpt = TRUE, tsv = TRUE, varLabel = TRUE, codebook = TRUE, update = TRUE, filetable = NULL, cat = TRUE, redown = TRUE, updatekeyword = NULL)
```

### `nhs_file_table`

```r
nhs_file_table(year, items, datafilename, docFilename, datafile, published, docURL, dataURL)
```

### `nhs_files_pc`

```r
nhs_files_pc(pattern = NULL, items, years, exclude = NULL, file_ext = NULL, cat = TRUE)
```

### `nhs_files_web`

```r
nhs_files_web(years, items, cat = TRUE)
```

### `nhs_html`

```r
nhs_html(x, browse = TRUE)
```

### `nhs_html_download`

```r
nhs_html_download(tsv = NULL, download = FALSE, distribute = FALSE)
```

### `nhs_items_pc`

```r
nhs_items_pc(years)
```

### `nhs_items_web`

```r
nhs_items_web(years, cat = TRUE)
```

### `nhs_news`

```r
nhs_news(browse = FALSE)
```

### `nhs_pg`

```r
nhs_pg(..., varLabel = TRUE, codebook = TRUE, nrows = Inf, lowercd = FALSE, force_rbind = FALSE, conn)
```

### `nhs_read`

```r
nhs_read(..., varLabel = FALSE, codebook = TRUE, lower_cd = FALSE, Year = TRUE, nrows = Inf, cat = TRUE, refuse_dontknow_toNA = TRUE, psu_strat = TRUE, join = c("full", "inner", "left", "right", "semi", "anti", "nest"))
```

### `nhs_search`

```r
nhs_search(..., cat = TRUE, fileds = NULL)
```

### `nhs_target`

```r
nhs_target(...)
```

### `nhs_tsv`

```r
nhs_tsv(..., items, years, ex_years = NULL, cat = TRUE)
```

### `nhs_update`

```r
nhs_update(path = NULL)
```

### `nhs_varLabel`

```r
nhs_varLabel(..., tolower = FALSE)
```

### `nhs_view`

```r
nhs_view(x, ...)
```

### `nhs_wt`

```r
nhs_wt(data, yr2, yr4, wtname = "cwt")
```

### `nhs_year_pc`

```r
nhs_year_pc(range = TRUE)
```

### `nhs_years_web`

```r
nhs_years_web(range = TRUE)
```

### `optimal_nKnots`

```r
optimal_nKnots(fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F)
```

### `p4interaction`

```r
p4interaction(fit, adjust = NULL, df = Inf)
```

### `p4trend`

```r
p4trend(fit, x = NULL, character2integer = TRUE, quadratic = FALSE, round = 3)
```

### `paste_dataframe`

```r
paste_dataframe(...)
```

### `person_years`

```r
person_years(data, outcome = NULL, year = NULL, by = NULL, per1000 = FALSE, round = 3)
```

### `prepare_items`

```r
prepare_items(items)
```

### `prepare_years`

```r
prepare_years(years, range = TRUE)
```

### `prevalence_byYear`

```r
prevalence_byYear(object, y = NULL, stratum = NULL, adjust = NULL, round = 2, xlsx = NULL)
```

### `quant`

```r
quant(x, n, round = 3, cat = TRUE, Q = FALSE)
```

### `quant.median`

```r
quant.median(x, n, round = 3, cat = TRUE)
```

### `re_order`

```r
re_order(data, ...)
```

### `reg_check`

```r
reg_check(...)
```

### `reg_table`

```r
reg_table(fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL)
```

### `rename`

```r
rename(.data, ...)
```

### `row.counts`

```r
row.counts(data)
```

### `row.max`

```r
row.max(x, na.rm = T)
```

### `row.means`

```r
row.means(data, na.rm = TRUE)
```

### `row.min`

```r
row.min(x, na.rm = T)
```

### `row.sums`

```r
row.sums(data, na.rm = TRUE)
```

### `row_names`

```r
row_names(data, names)
```

### `select`

```r
select(.data, ...)
```

### `select_col`

```r
select_col(x, ...)
```

### `select_col<-`

```r
select_col<-(x, value)
```

### `select_row`

```r
select_row(x, ...)
```

### `select_row<-`

```r
select_row<-(x, value)
```

### `setReference`

```r
setReference(x, value)
```

### `stratum_model`

```r
stratum_model(object, time = NULL, y, x, stratum = NULL, adjust = NULL, p = TRUE, round = 3, view = TRUE, xlsx = NULL, interaction = TRUE)
```

### `subsetdesign2df`

```r
subsetdesign2df(design, ...)
```

### `svy_barplot`

```r
svy_barplot(x, beside = TRUE, ...)
```

### `svy_count`

```r
svy_count(design, x, by = NULL, value = FALSE, per = FALSE, se = FALSE, low.high = FALSE, ci = FALSE, perSQse = FALSE, valueSQper = FALSE, direction = c("h", "v"), na.rm = TRUE, remove.name = FALSE, remove.suffix = FALSE, round = 2)
```

### `svy_coxplot`

```r
svy_coxplot(model, ..., ci = FALSE, legend.title = NULL, legend.name = NULL)
```

### `svy_design`

```r
svy_design(data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra")
```

### `svy_kmplot`

```r
svy_kmplot(x, ...)
```

### `svy_mean`

```r
svy_mean(design, x, by = NULL, value = FALSE, se = FALSE, low.high = FALSE, ci = FALSE, meanPMse = FALSE, meanSQse = FALSE, geometric = FALSE, round = 2, remove.suffix = FALSE, na.rm = TRUE)
```

### `svy_missValue`

```r
svy_missValue(design, plot = TRUE)
```

### `svy_population`

```r
svy_population(design, by = NULL)
```

### `svy_quantile`

```r
svy_quantile(design, x, by = NULL, quantile = FALSE, q0.25 = FALSE, q0.5 = FALSE, q0.75 = FALSE, round = 2, remove.prefix = FALSE, remove.suffix = FALSE, na.rm = TRUE)
```

### `svy_roc`

```r
svy_roc(design, score, class, rescale = TRUE)
```

### `svy_roc_plot`

```r
svy_roc_plot(..., color = NULL, lwd = 1.05, legend.title = NULL, legend.names = NULL)
```

### `svy_tableone`

```r
svy_tableone(design, cv = NULL, cv.nn = NULL, gv = NULL, by = NULL, c_meanSQse = FALSE, c_meanPMse = FALSE, c_ci = FALSE, c_geometric = FALSE, g_N = FALSE, g_percent = FALSE, g_perSQse = FALSE, g_NSQper = FALSE, g_nSQper = FALSE, g_ci = FALSE, g_direction = "v", total = FALSE, round = 2, view = T, xlsx = NULL, pvalue = TRUE)
```

### `svy_uv.cox`

```r
svy_uv.cox(design, time, status, x, adjust = NULL, round = 2, view = T, xlsx = NULL)
```

### `svy_uv.glm`

```r
svy_uv.glm(design, y, x, adjust = NULL, round = 2, view = T, xlsx = NULL)
```

### `svy_uv.logit`

```r
svy_uv.logit(design, y, x, adjust = NULL, round = 2, family = quasibinomial, view = T, xlsx = NULL)
```

### `to_NA`

```r
to_NA(x, dont_know = TRUE, refused = TRUE)
```

### `to_numeric`

```r
to_numeric(x)
```

### `to_numeric<-`

```r
to_numeric<-(x, value)
```

### `transfer_fndds`

```r
transfer_fndds()
```

### `updateKnot`

```r
updateKnot(fit, k, data = NULL)
```

### `value.numbar`

```r
value.numbar(data)
```

### `varExtracted`

```r
varExtracted(x)
```

### `var_labels`

```r
var_labels(df, order = FALSE)
```

### `write.yier`

```r
write.yier(df, file = NULL, project = NULL, row.names = FALSE, root = "c")
```

### `youth.obesity`

```r
youth.obesity(data, age = "age", sex = "sex", bmi = "bmi")
```


