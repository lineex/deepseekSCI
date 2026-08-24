# Integrated supporting reference: mimicr-agent/references/mimicr-core-functions.md

> Embedded source: `embedded-source/mimicr-agent/references/mimicr-core-functions.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# mimicR430 Core Function Parameters

## config_path
Title: config path for mimic database
Description: config path for mimic database
Category: `setup_discovery`
Usage: `config_path(path)`
Standard call: `config_path(path = normalizePath(Sys.getenv("MIMIC_DB_ROOT", unset = "LOCAL_PATH"), winslash = "/", mustWork = FALSE))`
- `path`: required; standard `normalizePath(Sys.getenv("MIMIC_DB_ROOT", unset = "LOCAL_PATH"), winslash = "/", mustWork = FALSE)`. path of mimic database Prefer MIMIC_DB_ROOT so the database location is configured once per machine.

## get_path
Title: path of mimic
Description: path of mimic
Category: `setup_discovery`
Usage: `get_path()`
Standard call: `get_path()`

## mimic_start
Title: start study
Description: start study
Category: `setup_discovery`
Usage: `mimic_start()`
Standard call: `mimic_start()`

## dics
Title: mimic数据库查询词典
Description: mimic数据库查询词典
Category: `setup_discovery`
Usage: `dics(...)`
Standard call: `dics()`
- `...`: optional. 关键词 Pass extra expressions explicitly.

## lookl
Title: match
Description: match
Category: `setup_discovery`
Usage: `lookl(x, ..., ignore.case = TRUE, NA2false = FALSE)`
Standard call: `lookl(x = NULL, ignore.case = TRUE, NA2false = FALSE)`
- `x`: required; standard `NULL`. vector Required but not inferable from metadata alone; confirm before execution.
- `...`: optional. key Pass extra expressions explicitly.
- `ignore.case`: optional; default `TRUE`; standard `TRUE`. logical, TRUE is default Preserve the package default.
- `NA2false`: optional; default `FALSE`; standard `FALSE`. logical. FALSE is default Preserve the package default.

## db_patients
Title: patients
Description: patients
Category: `raw_extract`
Usage: `db_patients( all = FALSE, subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod )`
Standard call: `db_patients(all = FALSE, subject_id = FALSE, gender = FALSE, anchor_age = FALSE, anchor_year = FALSE, anchor_year_group = FALSE, dod = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gender`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `anchor_age`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `anchor_year`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `anchor_year_group`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dod`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## db_admissions
Title: admissions
Description: admissions
Category: `raw_extract`
Usage: `db_admissions( all = FALSE, subject_id, hadm_id, admission_location, admittime, admission_type, admit_provider_id, hospital_expire_flag, deathtime, dischtime, discharge_location, insurance, language, marital_status, race, edregtime, edouttime )`
Standard call: `db_admissions(all = FALSE, subject_id = FALSE, hadm_id = FALSE, admission_location = FALSE, admittime = FALSE, admission_type = FALSE, admit_provider_id = NULL, hospital_expire_flag = FALSE, deathtime = FALSE, dischtime = FALSE, discharge_location = FALSE, insurance = FALSE, language = FALSE, marital_status = FALSE, race = FALSE, edregtime = FALSE, edouttime = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `hadm_id`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `admission_location`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `admittime`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `admission_type`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `admit_provider_id`: required; standard `NULL`.  Required but not inferable from metadata alone; confirm before execution.
- `hospital_expire_flag`: required; standard `FALSE`. a patient died during their hospitalization ? logical or character Use FALSE unless the protocol requires otherwise.
- `deathtime`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `dischtime`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `discharge_location`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `insurance`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `language`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `marital_status`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `race`: required; standard `FALSE`. logical or character Use FALSE unless the protocol requires otherwise.
- `edregtime`: required; standard `FALSE`. emergency department register time, logical or character Use FALSE unless the protocol requires otherwise.
- `edouttime`: required; standard `FALSE`. emergency department out time, logical or character Use FALSE unless the protocol requires otherwise.

## db_icustays
Title: icustays
Description: icustays
Category: `raw_extract`
Usage: `db_icustays( all = FALSE, subject_id = T, hadm_id = T, stay_id = T, first_careunit, last_careunit, intime, outtime, los )`
Standard call: `db_icustays(all = FALSE, subject_id = T, hadm_id = T, stay_id = T, first_careunit = FALSE, last_careunit = FALSE, intime = FALSE, outtime = FALSE, los = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `first_careunit`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `last_careunit`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `intime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `outtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `los`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## db_diagnoses_d.hadm
Title: 提取诊断数据
Description: 提取诊断数据
Category: `raw_extract`
Usage: `db_diagnoses_d.hadm( ..., icd9_start = NULL, icd10_start = NULL, icd9_between = NULL, icd10_between = NULL, xlsx = NULL, Newname = NULL, all = FALSE, subject_id, hadm_id, long_title, code_yn, code_10, drop_no = F, view = T, file = NULL )`
Standard call: `db_diagnoses_d.hadm(icd9_start = NULL, icd10_start = NULL, icd9_between = NULL, icd10_between = NULL, xlsx = NULL, Newname = NULL, all = FALSE, subject_id = FALSE, hadm_id = FALSE, long_title = FALSE, code_yn = FALSE, code_10 = FALSE, drop_no = F, view = T, file = NULL)`
- `...`: optional. 词典查询关键词 Pass extra expressions explicitly.
- `icd9_start`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd10_start`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd9_between`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd10_between`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `xlsx`: optional; default `NULL`; standard `NULL`. 使用excel查询 Preserve the package default.
- `Newname`: optional; default `NULL`; standard `NULL`. 诊断新名称 Preserve the package default.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `long_title`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `code_yn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `code_10`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drop_no`: optional; default `F`; standard `F`. 是否删除no Preserve the package default.
- `view`: optional; default `T`; standard `T`. 是否查看词典结果 Preserve the package default.
- `file`: optional; default `NULL`; standard `NULL`.  Preserve the package default.

## db_procedures_d.hadm
Title: 提取操作/手术数据
Description: 提取操作/手术数据
Category: `raw_extract`
Usage: `db_procedures_d.hadm( ..., icd9_start = NULL, icd10_start = NULL, icd9_between = NULL, icd10_between = NULL, xlsx = NULL, Newname = NULL, all = FALSE, subject_id, hadm_id, chartdate = F, long_title, code_yn, code_10, drop_no = F, view = T, file = NULL )`
Standard call: `db_procedures_d.hadm(icd9_start = NULL, icd10_start = NULL, icd9_between = NULL, icd10_between = NULL, xlsx = NULL, Newname = NULL, all = FALSE, subject_id = FALSE, hadm_id = FALSE, chartdate = F, long_title = FALSE, code_yn = FALSE, code_10 = FALSE, drop_no = F, view = T, file = NULL)`
- `...`: optional. 词典查询关键词 Pass extra expressions explicitly.
- `icd9_start`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd10_start`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd9_between`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `icd10_between`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `xlsx`: optional; default `NULL`; standard `NULL`. 使用excel查询 Preserve the package default.
- `Newname`: optional; default `NULL`; standard `NULL`. 诊断新名称 Preserve the package default.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `chartdate`: optional; default `F`; standard `F`.  Preserve the package default.
- `long_title`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `code_yn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `code_10`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drop_no`: optional; default `F`; standard `F`. 是否删除no Preserve the package default.
- `view`: optional; default `T`; standard `T`. 是否查看词典结果 Preserve the package default.
- `file`: optional; default `NULL`; standard `NULL`.  Preserve the package default.

## db_lab_D.subj.t
Title: labevents
Description: labevents
Category: `raw_extract`
Usage: `db_lab_D.subj.t( ..., all = FALSE, subject_id, hadm_id, specimen_id, itemid, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag, priority, comments, view = T )`
Standard call: `db_lab_D.subj.t(all = FALSE, subject_id = FALSE, hadm_id = FALSE, specimen_id = FALSE, itemid = FALSE, charttime = FALSE, storetime = FALSE, value = FALSE, valuenum = FALSE, valueuom = FALSE, ref_range_lower = FALSE, ref_range_upper = FALSE, flag = FALSE, priority = FALSE, comments = FALSE, view = T)`
- `...`: optional.  Pass extra expressions explicitly.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `specimen_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `itemid`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `charttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `storetime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `value`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `valuenum`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `valueuom`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ref_range_lower`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ref_range_upper`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `flag`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `priority`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `comments`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `view`: optional; default `T`; standard `T`.  Preserve the package default.

## db_prescriptions_D.hadm.t
Title: prescriptions
Description: prescriptions
Category: `raw_extract`
Usage: `db_prescriptions_D.hadm.t( ..., xlsx = NULL, all = FALSE, subject_id, hadm_id = T, poe_seq, poe_id, pharmacy_id, starttime, stoptime, drug_type, drug, drugYesNo = F, CN, formulary_drug_cd, gsn, ndc, prod_strength, form_rx, dose_val_rx, dose_unit_rx, form_val_disp, form_unit_disp, doses_per_24_hrs, route, view = T, file = NULL )`
Standard call: `db_prescriptions_D.hadm.t(xlsx = NULL, all = FALSE, subject_id = FALSE, hadm_id = T, poe_seq = FALSE, poe_id = FALSE, pharmacy_id = FALSE, starttime = FALSE, stoptime = FALSE, drug_type = FALSE, drug = FALSE, drugYesNo = F, CN = NULL, formulary_drug_cd = FALSE, gsn = FALSE, ndc = FALSE, prod_strength = FALSE, form_rx = FALSE, dose_val_rx = FALSE, dose_unit_rx = FALSE, form_val_disp = FALSE, form_unit_disp = FALSE, doses_per_24_hrs = FALSE, route = FALSE, view = T, file = NULL)`
- `...`: optional.  Pass extra expressions explicitly.
- `xlsx`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `poe_seq`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `poe_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pharmacy_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `stoptime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drug_type`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drug`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drugYesNo`: optional; default `F`; standard `F`.  Preserve the package default.
- `CN`: required; standard `NULL`.  Required but not inferable from metadata alone; confirm before execution.
- `formulary_drug_cd`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gsn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ndc`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `prod_strength`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `form_rx`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dose_val_rx`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dose_unit_rx`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `form_val_disp`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `form_unit_disp`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `doses_per_24_hrs`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `route`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `view`: optional; default `T`; standard `T`.  Preserve the package default.
- `file`: optional; default `NULL`; standard `NULL`.  Preserve the package default.

## dt_icustays.detail
Title: icu详细信息（每行一个icu）
Description: 记录了3方面的信息 病人信息：gender, admission_age, race, dod 住院信息：admittime, dischtime, los_hospital_day, hospital_expire_flag, hospstay_seq, first_hosp_stay icu信息：icu_intime, icu_outtime, los_icu_day, icustay_seq, first_icu_stay
Category: `time_series`
Usage: `dt_icustays.detail( all = FALSE, subject_id = T, hadm_id = T, stay_id = T, gender = "sex", admission_age = "age", race, dod, admittime, dischtime, los_hospital_day = T, hospital_expire_flag, hospstay_seq, first_hosp_stay = T, icu_intime = "intime", icu_outtime = "outtime", los_icu_day = T, icustay_seq, first_icu_stay = T )`
Standard call: `dt_icustays.detail(all = FALSE, subject_id = T, hadm_id = T, stay_id = T, gender = "sex", admission_age = "age", race = NULL, dod = NULL, admittime = NULL, dischtime = NULL, los_hospital_day = T, hospital_expire_flag = NULL, hospstay_seq = NULL, first_hosp_stay = T, icu_intime = "intime", icu_outtime = "outtime", los_icu_day = T, icustay_seq = NULL, first_icu_stay = T)`
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `gender`: optional; default `"sex"`; standard `"sex"`. 性别 Preserve the package default.
- `admission_age`: optional; default `"age"`; standard `"age"`. 入院时年龄 Preserve the package default.
- `race`: required; standard `NULL`. 种族 Required but not inferable from metadata alone; confirm before execution.
- `dod`: required; standard `NULL`. 死亡日期 Required but not inferable from metadata alone; confirm before execution.
- `admittime`: required; standard `NULL`. 入院时间 Required but not inferable from metadata alone; confirm before execution.
- `dischtime`: required; standard `NULL`. 出院时间 Required but not inferable from metadata alone; confirm before execution.
- `los_hospital_day`: optional; default `T`; standard `T`. 住院时长（天） Preserve the package default.
- `hospital_expire_flag`: required; standard `NULL`. 是否在医院内死亡 Required but not inferable from metadata alone; confirm before execution.
- `hospstay_seq`: required; standard `NULL`. 住院顺序 Required but not inferable from metadata alone; confirm before execution.
- `first_hosp_stay`: optional; default `T`; standard `T`. 是否是第一次住院 Preserve the package default.
- `icu_intime`: optional; default `"intime"`; standard `"intime"`. 住入icu时间 Preserve the package default.
- `icu_outtime`: optional; default `"outtime"`; standard `"outtime"`. 从icu出院时间 Preserve the package default.
- `los_icu_day`: optional; default `T`; standard `T`. 在icu住院的天数 Preserve the package default.
- `icustay_seq`: required; standard `NULL`. 住icu的次序 Required but not inferable from metadata alone; confirm before execution.
- `first_icu_stay`: optional; default `T`; standard `T`. 是否是第一次住icu Preserve the package default.

## dt_icustays.hourly
Title: icustay hourly -- This query generates a row for every hour the patient is in the ICU. -- The hours are based on clock-hours (i.e. 02:00, 03:00). -- The hour clock starts 24 hours before the first heart rate measurement. -- Note that the time of the first heart rate measurement is ceilinged to the hour.
Description: icustay hourly -- This query generates a row for every hour the patient is in the ICU. -- The hours are based on clock-hours (i.e. 02:00, 03:00). -- The hour clock starts 24 hours before the first heart rate measurement. -- Note that the time of the first heart rate measurement is ceilinged to the hour.
Category: `time_series`
Usage: `dt_icustays.hourly(all = FALSE, stay_id = T, hr, starttime, endtime)`
Standard call: `dt_icustays.hourly(all = FALSE, stay_id = T, hr = FALSE, starttime = NULL, endtime = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `starttime`: required; standard `NULL`.  Required but not inferable from metadata alone; confirm before execution.
- `endtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## dt_VitalSign_icu.t
Title: ICU住院期间，每个时间点的提取生命体征
Description: 体温、脉搏、呼吸、血压、氧饱和度
Category: `time_series`
Usage: `dt_VitalSign_icu.t( all = FALSE, heart_rate, sbp, dbp, mbp, sbp_ni, dbp_ni, mbp_ni, resp_rate, temperature_site, temperature, spo2, glucose_mg.dL, dayn_icu = NULL, dup_max = F, dup_min = F, times_icu = NULL, subject_id = F, hadm_id = F )`
Standard call: `dt_VitalSign_icu.t(all = FALSE, heart_rate = NULL, sbp = NULL, dbp = NULL, mbp = NULL, sbp_ni = NULL, dbp_ni = NULL, mbp_ni = NULL, resp_rate = NULL, temperature_site = NULL, temperature = NULL, spo2 = NULL, glucose_mg.dL = NULL, dayn_icu = NULL, dup_max = F, dup_min = F, times_icu = NULL, subject_id = F, hadm_id = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `heart_rate`: required; standard `NULL`. 心率, bpm, 次/分 Required but not inferable from metadata alone; confirm before execution.
- `sbp`: required; standard `NULL`. 收缩压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `dbp`: required; standard `NULL`. 舒张压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `mbp`: required; standard `NULL`. 平均血压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `sbp_ni`: required; standard `NULL`. 非侵入收缩压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `dbp_ni`: required; standard `NULL`. 非侵入舒张压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `mbp_ni`: required; standard `NULL`. 非侵入平均血压, mmHg Required but not inferable from metadata alone; confirm before execution.
- `resp_rate`: required; standard `NULL`. 呼吸频率, insp/min Required but not inferable from metadata alone; confirm before execution.
- `temperature_site`: required; standard `NULL`. 体温测量部分 Required but not inferable from metadata alone; confirm before execution.
- `temperature`: required; standard `NULL`. 体温, 摄氏度 Required but not inferable from metadata alone; confirm before execution.
- `spo2`: required; standard `NULL`. 氧饱和度, 百分比 Required but not inferable from metadata alone; confirm before execution.
- `glucose_mg.dL`: required; standard `NULL`. 血糖, mg/dL Required but not inferable from metadata alone; confirm before execution.
- `dayn_icu`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `dup_max`: optional; default `F`; standard `F`.  Preserve the package default.
- `dup_min`: optional; default `F`; standard `F`.  Preserve the package default.
- `times_icu`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `subject_id`: optional; default `F`; standard `F`.  Preserve the package default.
- `hadm_id`: optional; default `F`; standard `F`.  Preserve the package default.

## dt_ventilation_icu.t
Title: ventilation
Description: ventilation
Category: `time_series`
Usage: `dt_ventilation_icu.t( data, all = FALSE, stay_id = T, starttime, endtime, ventilation_status, join = "left" )`
Standard call: `dt_ventilation_icu.t(data = cohort_dat, all = FALSE, stay_id = T, starttime = FALSE, endtime = FALSE, ventilation_status = FALSE, join = "left")`
- `data`: required; standard `cohort_dat`. data Use the standard data object name for this stage.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `endtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ventilation_status`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `join`: optional; default `"left"`; standard `"left"`. join Preserve the package default.

## d1_lab_icu
Title: 住入icu第一天的实验室检查
Description: 住入icu第一天的实验室检查
Category: `day_summary`
Usage: `d1_lab_icu( all = FALSE, stay_id = T, hematocrit_max, hemoglobin_g.dL_max, platelet_max, wbc_max, hematocrit_min, hemoglobin_g.dL_min, platelet_min, wbc_min, albumin_g.dL_max, globulin_g.dL_max, total_protein_g.dL_max, aniongap_mEq.L_max, bicarbonate_mEq.L_max, bun_mg.dL_max, total_calcium_mg.dL_max, chloride_mEq.L_max, creatinine_mg.dL_max, glucose_mg.dL_max, sodium_mEq.L_max, potassium_mEq.L_max, albumin_g.dL_min, globulin_g.dL_min, total_protein_g.dL_min, aniongap_mEq.L_min, bicarbonate_mEq.L_min, bun_mg.dL_min, total_calcium_mg.dL_min, chloride_mEq.L_min, creatinine_mg.dL_min, glucose_mg.dL_min, sodium_mEq.L_min, potassium_mEq.L_min, basophils_abs_max, eosinophils_abs_max, lymphocytes_abs_max, monocytes_abs_max, neutrophils_abs_max, atypical_lymphocytes_max, bands_max, immature_granulocytes_max, metamyelocytes_max, nrbc_max, basophils_abs_min, eosinophils_abs_min, lymphocytes_abs_min, monocytes_abs_min, neutrophils_abs_min, atypical_lymphocytes_min, bands_min, immature_granulocytes_min, metamyelocytes_min, nrbc_min, D_dimer_ng.mL_max, fibrinogen_mg.dL_max, thrombin_sec_max, INR_max, pt_sec_max, ptt_sec_max, D_dimer_ng.mL_min, fibrinogen_mg.dL_min, thrombin_sec_min, INR_min, pt_sec_min, ptt_sec_min, alt_IU.L_max, alp_IU.L_max, ast_IU.L_max, amylase_IU.L_max, bilirubin_total_mg.dL_max, bilirubin_direct_mg.dL_max, bilirubin_indirect_mg.dL_max, ck_cpk_IU.L_max, ck_mb_ng.mL_max, ggt_IU.L_max, ld_ldh_IU.L_max, alt_IU.L_min, alp_IU.L_min, ast_IU.L_min, amylase_IU.L_min, bilirubin_total_mg.dL_min, bilirubin_direct_mg.dL_min, bilirubin_indirect_mg.dL_min, ck_cpk_IU.L_min, ck_mb_ng.mL_min, ggt_IU.L_min, ld_ldh_IU.L_min )`
Standard call: `d1_lab_icu(all = FALSE, stay_id = T, hematocrit_max = FALSE, hemoglobin_g.dL_max = FALSE, platelet_max = FALSE, wbc_max = FALSE, hematocrit_min = FALSE, hemoglobin_g.dL_min = FALSE, platelet_min = FALSE, wbc_min = FALSE, albumin_g.dL_max = FALSE, globulin_g.dL_max = FALSE, total_protein_g.dL_max = FALSE, aniongap_mEq.L_max = FALSE, bicarbonate_mEq.L_max = FALSE, bun_mg.dL_max = FALSE, total_calcium_mg.dL_max = FALSE, chloride_mEq.L_max = FALSE, creatinine_mg.dL_max = FALSE, glucose_mg.dL_max = FALSE, sodium_mEq.L_max = FALSE, potassium_mEq.L_max = FALSE, albumin_g.dL_min = FALSE, globulin_g.dL_min = FALSE, total_protein_g.dL_min = FALSE, aniongap_mEq.L_min = FALSE, bicarbonate_mEq.L_min = FALSE, bun_mg.dL_min = FALSE, total_calcium_mg.dL_min = FALSE, chloride_mEq.L_min = FALSE, creatinine_mg.dL_min = FALSE, glucose_mg.dL_min = FALSE, sodium_mEq.L_min = FALSE, potassium_mEq.L_min = FALSE, basophils_abs_max = FALSE, eosinophils_abs_max = FALSE, lymphocytes_abs_max = FALSE, monocytes_abs_max = FALSE, neutrophils_abs_max = FALSE, atypical_lymphocytes_max = FALSE, bands_max = FALSE, immature_granulocytes_max = FALSE, metamyelocytes_max = FALSE, nrbc_max = FALSE, basophils_abs_min = FALSE, eosinophils_abs_min = FALSE, lymphocytes_abs_min = FALSE, monocytes_abs_min = FALSE, neutrophils_abs_min = FALSE, atypical_lymphocytes_min = FALSE, bands_min = FALSE, immature_granulocytes_min = FALSE, metamyelocytes_min = FALSE, nrbc_min = FALSE, D_dimer_ng.mL_max = FALSE, fibrinogen_mg.dL_max = FALSE, thrombin_sec_max = FALSE, INR_max = FALSE, pt_sec_max = FALSE, ptt_sec_max = FALSE, D_dimer_ng.mL_min = FALSE, fibrinogen_mg.dL_min = FALSE, thrombin_sec_min = FALSE, INR_min = FALSE, pt_sec_min = FALSE, ptt_sec_min = FALSE, alt_IU.L_max = FALSE, alp_IU.L_max = FALSE, ast_IU.L_max = FALSE, amylase_IU.L_max = FALSE, bilirubin_total_mg.dL_max = FALSE, bilirubin_direct_mg.dL_max = FALSE, bilirubin_indirect_mg.dL_max = FALSE, ck_cpk_IU.L_max = FALSE, ck_mb_ng.mL_max = FALSE, ggt_IU.L_max = FALSE, ld_ldh_IU.L_max = FALSE, alt_IU.L_min = FALSE, alp_IU.L_min = FALSE, ast_IU.L_min = FALSE, amylase_IU.L_min = FALSE, bilirubin_total_mg.dL_min = FALSE, bilirubin_direct_mg.dL_min = FALSE, bilirubin_indirect_mg.dL_min = FALSE, ck_cpk_IU.L_min = FALSE, ck_mb_ng.mL_min = FALSE, ggt_IU.L_min = FALSE, ld_ldh_IU.L_min = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `hematocrit_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hemoglobin_g.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `platelet_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `wbc_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hematocrit_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hemoglobin_g.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `platelet_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `wbc_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `albumin_g.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `globulin_g.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `total_protein_g.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `aniongap_mEq.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bicarbonate_mEq.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bun_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `total_calcium_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `chloride_mEq.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creatinine_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `glucose_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sodium_mEq.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `potassium_mEq.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `albumin_g.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `globulin_g.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `total_protein_g.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `aniongap_mEq.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bicarbonate_mEq.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bun_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `total_calcium_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `chloride_mEq.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creatinine_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `glucose_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sodium_mEq.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `potassium_mEq.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `basophils_abs_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eosinophils_abs_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `lymphocytes_abs_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `monocytes_abs_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `neutrophils_abs_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `atypical_lymphocytes_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bands_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `immature_granulocytes_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `metamyelocytes_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `nrbc_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `basophils_abs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eosinophils_abs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `lymphocytes_abs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `monocytes_abs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `neutrophils_abs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `atypical_lymphocytes_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bands_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `immature_granulocytes_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `metamyelocytes_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `nrbc_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `D_dimer_ng.mL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `fibrinogen_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `thrombin_sec_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `INR_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pt_sec_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ptt_sec_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `D_dimer_ng.mL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `fibrinogen_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `thrombin_sec_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `INR_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pt_sec_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ptt_sec_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `alt_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `alp_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ast_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `amylase_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_total_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_direct_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_indirect_mg.dL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ck_cpk_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ck_mb_ng.mL_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ggt_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ld_ldh_IU.L_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `alt_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `alp_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ast_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `amylase_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_total_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_direct_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_indirect_mg.dL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ck_cpk_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ck_mb_ng.mL_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ggt_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ld_ldh_IU.L_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## d1_VitalSign_icu
Title: 住入icu第一天的生命体征
Description: 住入icu第一天的生命体征
Category: `day_summary`
Usage: `d1_VitalSign_icu( all = FALSE, stay_id = T, heart_rate_mean, sbp_mean, dbp_mean, mbp_mean, resp_rate_mean, temperature_mean, spo2_mean, glucose_mean, heart_rate_max, sbp_max, dbp_max, mbp_max, resp_rate_max, temperature_max, spo2_max, glucose_max, heart_rate_min, sbp_min, dbp_min, mbp_min, resp_rate_min, temperature_min, spo2_min, glucose_min )`
Standard call: `d1_VitalSign_icu(all = FALSE, stay_id = T, heart_rate_mean = FALSE, sbp_mean = FALSE, dbp_mean = FALSE, mbp_mean = FALSE, resp_rate_mean = FALSE, temperature_mean = FALSE, spo2_mean = FALSE, glucose_mean = FALSE, heart_rate_max = FALSE, sbp_max = FALSE, dbp_max = FALSE, mbp_max = FALSE, resp_rate_max = FALSE, temperature_max = FALSE, spo2_max = FALSE, glucose_max = FALSE, heart_rate_min = FALSE, sbp_min = FALSE, dbp_min = FALSE, mbp_min = FALSE, resp_rate_min = FALSE, temperature_min = FALSE, spo2_min = FALSE, glucose_min = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `heart_rate_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sbp_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dbp_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `mbp_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `resp_rate_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `temperature_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `spo2_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `glucose_mean`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `heart_rate_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sbp_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dbp_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `mbp_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `resp_rate_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `temperature_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `spo2_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `glucose_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `heart_rate_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sbp_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dbp_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `mbp_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `resp_rate_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `temperature_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `spo2_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `glucose_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## d1_GCS_icu
Title: 入住icu第一天的GCS评分
Description: 入住icu第一天的GCS评分
Category: `day_summary`
Usage: `d1_GCS_icu( all = FALSE, stay_id = T, gcs_min = T, gcs_motor, gcs_verbal, gcs_eyes, gcs_unable )`
Standard call: `d1_GCS_icu(all = FALSE, stay_id = T, gcs_min = T, gcs_motor = FALSE, gcs_verbal = FALSE, gcs_eyes = FALSE, gcs_unable = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. T Preserve the package default.
- `gcs_min`: optional; default `T`; standard `T`. T Preserve the package default.
- `gcs_motor`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gcs_verbal`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gcs_eyes`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gcs_unable`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## d1_sofa_icu
Title: d1_sofa_icu
Description: d1_sofa_icu
Category: `day_summary`
Usage: `d1_sofa_icu( all = FALSE, stay_id = T, sofa = T, respiration, coagulation, liver, cardiovascular, cns, renal, subject_id = F, hadm_id = F )`
Standard call: `d1_sofa_icu(all = FALSE, stay_id = T, sofa = T, respiration = FALSE, coagulation = FALSE, liver = FALSE, cardiovascular = FALSE, cns = FALSE, renal = FALSE, subject_id = F, hadm_id = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. T Preserve the package default.
- `sofa`: optional; default `T`; standard `T`. T Preserve the package default.
- `respiration`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `coagulation`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `liver`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cardiovascular`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cns`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `renal`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `subject_id`: optional; default `F`; standard `F`.  Preserve the package default.
- `hadm_id`: optional; default `F`; standard `F`.  Preserve the package default.

## d1_saps2_icu
Title: d1_saps2_icu
Description: d1_saps2_icu
Category: `day_summary`
Usage: `d1_saps2_icu( all = FALSE, stay_id = T, starttime, endtime, sapsii = T, sapsii_prob, age_score, hr_score, sysbp_score, temp_score, pao2fio2_score, uo_score, bun_score, wbc_score, potassium_score, sodium_score, bicarbonate_score, bilirubin_score, gcs_score, comorbidity_score, admissiontype_score, subject_id = F, hadm_id = F )`
Standard call: `d1_saps2_icu(all = FALSE, stay_id = T, starttime = FALSE, endtime = FALSE, sapsii = T, sapsii_prob = FALSE, age_score = FALSE, hr_score = FALSE, sysbp_score = FALSE, temp_score = FALSE, pao2fio2_score = FALSE, uo_score = FALSE, bun_score = FALSE, wbc_score = FALSE, potassium_score = FALSE, sodium_score = FALSE, bicarbonate_score = FALSE, bilirubin_score = FALSE, gcs_score = FALSE, comorbidity_score = FALSE, admissiontype_score = FALSE, subject_id = F, hadm_id = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. T Preserve the package default.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `endtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sapsii`: optional; default `T`; standard `T`. T Preserve the package default.
- `sapsii_prob`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `age_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hr_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sysbp_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `temp_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pao2fio2_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `uo_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bun_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `wbc_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `potassium_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sodium_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bicarbonate_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gcs_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `comorbidity_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `admissiontype_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `subject_id`: optional; default `F`; standard `F`.  Preserve the package default.
- `hadm_id`: optional; default `F`; standard `F`.  Preserve the package default.

## diag_AKI.kdigo_icu
Title: diag_AKI.kdigo_icu
Description: diag_AKI.kdigo_icu
Category: `diagnosis`
Usage: `diag_AKI.kdigo_icu(all = FALSE, stay_id = T, aki_stage = "AKI_stage")`
Standard call: `diag_AKI.kdigo_icu(all = FALSE, stay_id = T, aki_stage = "AKI_stage")`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `aki_stage`: optional; default `"AKI_stage"`; standard `"AKI_stage"`. character or logical Preserve the package default.

## diag_CKD_hadm
Title: CKD
Description: CKD
Category: `diagnosis`
Usage: `diag_CKD_hadm( all = FALSE, hadm_id = T, long_title, code_yn = "CKD_yn", code_10 )`
Standard call: `diag_CKD_hadm(all = FALSE, hadm_id = T, long_title = FALSE, code_yn = "CKD_yn", code_10 = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `long_title`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `code_yn`: optional; default `"CKD_yn"`; standard `"CKD_yn"`. character or logical Preserve the package default.
- `code_10`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## diag_ARDS_hadm
Title: ARDS
Description: ARDS
Category: `diagnosis`
Usage: `diag_ARDS_hadm( subject_id = F, hadm_id = T, long_title = F, code_yn = "ARDS", code_10 = F, drop_no = F )`
Standard call: `diag_ARDS_hadm(subject_id = F, hadm_id = T, long_title = F, code_yn = "ARDS", code_10 = F, drop_no = F)`
- `subject_id`: optional; default `F`; standard `F`. character or logical Preserve the package default.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `long_title`: optional; default `F`; standard `F`. character or logical Preserve the package default.
- `code_yn`: optional; default `"ARDS"`; standard `"ARDS"`. character or logical Preserve the package default.
- `code_10`: optional; default `F`; standard `F`. character or logical Preserve the package default.
- `drop_no`: optional; default `F`; standard `F`. 是否查看词典结果 Preserve the package default.

## diag_suspicion.of.infection_hadm
Title: suspicion.of.infection
Description: 每一行是一个住院病人使用的抗生素
Category: `diagnosis`
Usage: `diag_suspicion.of.infection_hadm( all = FALSE, subject_id, hadm_id = T, stay_id, ab_id, antibiotic, antibiotic_time, suspected_infection, suspected_infection_time, culture_time, specimen, positive_culture )`
Standard call: `diag_suspicion.of.infection_hadm(all = FALSE, subject_id = FALSE, hadm_id = T, stay_id = FALSE, ab_id = FALSE, antibiotic = FALSE, antibiotic_time = FALSE, suspected_infection = FALSE, suspected_infection_time = FALSE, culture_time = FALSE, specimen = FALSE, positive_culture = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `stay_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `ab_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `antibiotic`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `antibiotic_time`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `suspected_infection`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `suspected_infection_time`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `culture_time`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `specimen`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `positive_culture`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## dex_charlson_hadm
Title: Charlson共病指数
Description: Charlson共病指数
Category: `derived_index`
Usage: `dex_charlson_hadm( all = FALSE, hadm_id = T, charlson_comorbidity_index = "Charlson_comorbidity_index", age_score, myocardial_infarct, congestive_heart_failure, peripheral_vascular_disease, cerebrovascular_disease, dementia, chronic_pulmonary_disease, rheumatic_disease, peptic_ulcer_disease, mild_liver_disease, diabetes_without_cc, diabetes_with_cc, paraplegia, renal_disease, malignant_cancer, severe_liver_disease, metastatic_solid_tumor, aids )`
Standard call: `dex_charlson_hadm(all = FALSE, hadm_id = T, charlson_comorbidity_index = "Charlson_comorbidity_index", age_score = FALSE, myocardial_infarct = FALSE, congestive_heart_failure = FALSE, peripheral_vascular_disease = FALSE, cerebrovascular_disease = FALSE, dementia = FALSE, chronic_pulmonary_disease = FALSE, rheumatic_disease = FALSE, peptic_ulcer_disease = FALSE, mild_liver_disease = FALSE, diabetes_without_cc = FALSE, diabetes_with_cc = FALSE, paraplegia = FALSE, renal_disease = FALSE, malignant_cancer = FALSE, severe_liver_disease = FALSE, metastatic_solid_tumor = FALSE, aids = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `hadm_id`: optional; default `T`; standard `T`. T Preserve the package default.
- `charlson_comorbidity_index`: optional; default `"Charlson_comorbidity_index"`; standard `"Charlson_comorbidity_index"`. T Preserve the package default.
- `age_score`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `myocardial_infarct`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `congestive_heart_failure`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `peripheral_vascular_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cerebrovascular_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dementia`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `chronic_pulmonary_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `rheumatic_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `peptic_ulcer_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `mild_liver_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `diabetes_without_cc`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `diabetes_with_cc`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `paraplegia`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `renal_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `malignant_cancer`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `severe_liver_disease`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `metastatic_solid_tumor`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `aids`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## dex_eGFR
Title: eGFR
Description: eGFR
Category: `derived_index`
Usage: `dex_eGFR( data, all = FALSE, subject_id, hadm_id, stay_id, age, sex, race, weight, height, charttime, creat, creat_low_past_48hr, creat_low_past_7day, eGFR_CKD_EPI.2021, eGFR_CKD_EPI.2021_low_past_48hr, eGFR_CKD_EPI.2021_low_past_7day, eGFR_CKD_EPI.2009, eGFR_CKD_EPI.2009_low_past_48hr, eGFR_CKD_EPI.2009_low_past_7day, eGFR_MDRD.2007, eGFR_MDRD.2007_low_past_48hr, eGFR_MDRD.2007_low_past_7day, eGFR_Cockcroft_Gault.1976, eGFR_Cockcroft_Gault.1976_low_past_48hr, eGFR_Cockcroft_Gault.1976_low_past_7day, eGFR_FAS_age.2016, eGFR_FAS_age.2016_low_past_48hr, eGFR_FAS_age.2016_low_past_7day, eGFR_FAS_height.2016, eGFR_FAS_height.2016_low_past_48hr, eGFR_FAS_height.2016_low_past_7day, join = "left" )`
Standard call: `dex_eGFR(data = cohort_dat, all = FALSE, subject_id = FALSE, hadm_id = FALSE, stay_id = FALSE, age = FALSE, sex = FALSE, race = FALSE, weight = FALSE, height = FALSE, charttime = FALSE, creat = FALSE, creat_low_past_48hr = FALSE, creat_low_past_7day = FALSE, eGFR_CKD_EPI.2021 = FALSE, eGFR_CKD_EPI.2021_low_past_48hr = FALSE, eGFR_CKD_EPI.2021_low_past_7day = FALSE, eGFR_CKD_EPI.2009 = FALSE, eGFR_CKD_EPI.2009_low_past_48hr = FALSE, eGFR_CKD_EPI.2009_low_past_7day = FALSE, eGFR_MDRD.2007 = FALSE, eGFR_MDRD.2007_low_past_48hr = FALSE, eGFR_MDRD.2007_low_past_7day = FALSE, eGFR_Cockcroft_Gault.1976 = FALSE, eGFR_Cockcroft_Gault.1976_low_past_48hr = FALSE, eGFR_Cockcroft_Gault.1976_low_past_7day = FALSE, eGFR_FAS_age.2016 = FALSE, eGFR_FAS_age.2016_low_past_48hr = FALSE, eGFR_FAS_age.2016_low_past_7day = FALSE, eGFR_FAS_height.2016 = FALSE, eGFR_FAS_height.2016_low_past_48hr = FALSE, eGFR_FAS_height.2016_low_past_7day = FALSE, join = "left")`
- `data`: required; standard `cohort_dat`. data Use the standard data object name for this stage.
- `all`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `stay_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `age`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sex`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `race`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `weight`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `height`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `charttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creat`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creat_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creat_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2021`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2021_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2021_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2009`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2009_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_CKD_EPI.2009_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_MDRD.2007`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_MDRD.2007_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_MDRD.2007_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_Cockcroft_Gault.1976`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_Cockcroft_Gault.1976_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_Cockcroft_Gault.1976_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_age.2016`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_age.2016_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_age.2016_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_height.2016`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_height.2016_low_past_48hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `eGFR_FAS_height.2016_low_past_7day`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `join`: optional; default `"left"`; standard `"left"`. join Preserve the package default.

## dex_sofa_icu.t
Title: dex_sofa_icu.t
Description: dex_sofa_icu.t
Category: `derived_index`
Usage: `dex_sofa_icu.t( all = FALSE, stay_id = T, hr, sofa_24hours, respiration_24hours, coagulation_24hours, liver_24hours, cardiovascular_24hours, cns_24hours, renal_24hours, starttime, endtime, pao2fio2ratio_novent, pao2fio2ratio_vent, rate_epinephrine, rate_norepinephrine, rate_dopamine, rate_dobutamine, meanbp_min, gcs_min, uo_24hr, bilirubin_max, creatinine_max, platelet_min, respiration, coagulation, liver, cardiovascular, cns, renal, subject_id = F, hadm_id = F )`
Standard call: `dex_sofa_icu.t(all = FALSE, stay_id = T, hr = FALSE, sofa_24hours = FALSE, respiration_24hours = FALSE, coagulation_24hours = FALSE, liver_24hours = FALSE, cardiovascular_24hours = FALSE, cns_24hours = FALSE, renal_24hours = FALSE, starttime = FALSE, endtime = FALSE, pao2fio2ratio_novent = FALSE, pao2fio2ratio_vent = FALSE, rate_epinephrine = FALSE, rate_norepinephrine = FALSE, rate_dopamine = FALSE, rate_dobutamine = FALSE, meanbp_min = FALSE, gcs_min = FALSE, uo_24hr = FALSE, bilirubin_max = FALSE, creatinine_max = FALSE, platelet_min = FALSE, respiration = FALSE, coagulation = FALSE, liver = FALSE, cardiovascular = FALSE, cns = FALSE, renal = FALSE, subject_id = F, hadm_id = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `sofa_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `respiration_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `coagulation_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `liver_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cardiovascular_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cns_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `renal_24hours`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `endtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pao2fio2ratio_novent`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `pao2fio2ratio_vent`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `rate_epinephrine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `rate_norepinephrine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `rate_dopamine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `rate_dobutamine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `meanbp_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `gcs_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `uo_24hr`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `bilirubin_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `creatinine_max`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `platelet_min`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `respiration`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `coagulation`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `liver`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cardiovascular`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `cns`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `renal`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `subject_id`: optional; default `F`; standard `F`.  Preserve the package default.
- `hadm_id`: optional; default `F`; standard `F`.  Preserve the package default.

## drug_ssTime_hadm
Title: 根据入院时间判断药物的使用情况
Description: 根据入院时间判断药物的使用情况
Category: `drug_exposure`
Usage: `drug_ssTime_hadm(d, colnm = "xx", post_hour = 0)`
Standard call: `drug_ssTime_hadm(d = NULL, colnm = "xx", post_hour = 0)`
- `d`: required; standard `NULL`. 数据 Required but not inferable from metadata alone; confirm before execution.
- `colnm`: optional; default `"xx"`; standard `"xx"`. 新列名称 Preserve the package default.
- `post_hour`: optional; default `0`; standard `0`. 入院时间向后推几小时 Preserve the package default.

## drug_ssTime_icu
Title: 根据入icu时间判断药物的使用情况
Description: 根据入icu时间判断药物的使用情况
Category: `drug_exposure`
Usage: `drug_ssTime_icu(d, colnm = "xx", post_hour = 0)`
Standard call: `drug_ssTime_icu(d = NULL, colnm = "xx", post_hour = 0)`
- `d`: required; standard `NULL`. 数据 Required but not inferable from metadata alone; confirm before execution.
- `colnm`: optional; default `"xx"`; standard `"xx"`. 新列名称 Preserve the package default.
- `post_hour`: optional; default `0`; standard `0`. 入icu时间向后推几小时 Preserve the package default.

## drug_antibiotic.pre_hadm.t
Title: 抗生素
Description: 抗生素
Category: `drug_exposure`
Usage: `drug_antibiotic.pre_hadm.t( all = FALSE, subject_id, hadm_id = T, stay_id, antibiotic, route, starttime, stoptime, drugYesNo = F )`
Standard call: `drug_antibiotic.pre_hadm.t(all = FALSE, subject_id = FALSE, hadm_id = T, stay_id = FALSE, antibiotic = FALSE, route = FALSE, starttime = FALSE, stoptime = FALSE, drugYesNo = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `subject_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `hadm_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `stay_id`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `antibiotic`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `route`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `stoptime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drugYesNo`: optional; default `F`; standard `F`.  Preserve the package default.

## drug_vasoactive.agent.input_icu.t
Title: 血管活性药
Description: 血管活性药
Category: `drug_exposure`
Usage: `drug_vasoactive.agent.input_icu.t( all = FALSE, stay_id = T, starttime, endtime, dopamine, epinephrine, norepinephrine, phenylephrine, vasopressin, dobutamine, milrinone, drugYesNo = F )`
Standard call: `drug_vasoactive.agent.input_icu.t(all = FALSE, stay_id = T, starttime = FALSE, endtime = FALSE, dopamine = FALSE, epinephrine = FALSE, norepinephrine = FALSE, phenylephrine = FALSE, vasopressin = FALSE, dobutamine = FALSE, milrinone = FALSE, drugYesNo = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `stay_id`: optional; default `T`; standard `T`. character or logical Preserve the package default.
- `starttime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `endtime`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dopamine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `epinephrine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `norepinephrine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `phenylephrine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `vasopressin`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `dobutamine`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `milrinone`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `drugYesNo`: optional; default `F`; standard `F`.  Preserve the package default.

## death_icu
Title: icu病人的死亡(icu)
Description: icu病人的死亡(icu)
Category: `outcome`
Usage: `death_icu(all = FALSE, n = NULL, survival_days, status_01, status_yn)`
Standard call: `death_icu(all = FALSE, n = NULL, survival_days = FALSE, status_01 = FALSE, status_yn = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `n`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `survival_days`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_01`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_yn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## death_hadm
Title: icu病人的死亡（icu，普通病房）
Description: icu病人的死亡（icu，普通病房）
Category: `outcome`
Usage: `death_hadm(all = FALSE, n = NULL, survival_days, status_01, status_yn)`
Standard call: `death_hadm(all = FALSE, n = NULL, survival_days = FALSE, status_01 = FALSE, status_yn = FALSE)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `n`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `survival_days`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_01`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_yn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.

## death_hadm_nday
Title: death_hadm_nday
Description: death_hadm_nday
Category: `outcome`
Usage: `death_hadm_nday( all = FALSE, n = 30, survival_days, status_yn, status_01, Include.death.discharge = F )`
Standard call: `death_hadm_nday(all = FALSE, n = 30, survival_days = FALSE, status_yn = FALSE, status_01 = FALSE, Include.death.discharge = F)`
- `all`: optional; default `FALSE`; standard `FALSE`.  Preserve the package default.
- `n`: optional; default `30`; standard `30`. 天数 Preserve the package default.
- `survival_days`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_yn`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `status_01`: required; standard `FALSE`. character or logical Use FALSE unless the protocol requires otherwise.
- `Include.death.discharge`: optional; default `F`; standard `F`.  Preserve the package default.

## crude.Model.n
Title: crude model, model 1, model 2
Description: crude model, model 1, model 2
Category: `plot_model`
Usage: `crude.Model.n( ..., bys = NULL, round = 2, xlsx = NULL, character2integer = TRUE, quadratic = FALSE )`
Standard call: `crude.Model.n(bys = NULL, round = 2, xlsx = NULL, character2integer = TRUE, quadratic = FALSE)`
- `...`: optional. 多个模型，model0, model1, model2 Pass extra expressions explicitly.
- `bys`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `round`: optional; default `2`; standard `2`. 保留小数位数，默认为2位 Preserve the package default.
- `xlsx`: optional; default `NULL`; standard `NULL`. 赋值excel名字，把结果写出去，例如xlsx="结果.xslx" Preserve the package default.
- `character2integer`: optional; default `TRUE`; standard `TRUE`. logical Preserve the package default.
- `quadratic`: optional; default `FALSE`; standard `FALSE`. logical Preserve the package default.

## reg_table
Title: 查看回归结果
Description: 查看回归结果
Category: `plot_model`
Usage: `reg_table(fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL)`
Standard call: `reg_table(fit = model1, round = 2, style = 2, x = NULL, view = T, xlsx = NULL)`
- `fit`: required; standard `model1`. fit Use the first fitted model object by default.
- `round`: optional; default `2`; standard `2`. 2 Preserve the package default.
- `style`: optional; default `2`; standard `2`. integer Preserve the package default.
- `x`: optional; default `NULL`; standard `NULL`. x varaibles Preserve the package default.
- `view`: optional; default `T`; standard `T`. logical Preserve the package default.
- `xlsx`: optional; default `NULL`; standard `NULL`.  Preserve the package default.

## RCS
Title: RCS
Description: RCS
Category: `plot_model`
Usage: `RCS( ..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.95, ref.zero = F, portion = 100, xlsx = NULL, cat = T )`
Standard call: `RCS(nknots = NULL, reference = "median", by = NULL, conf.int = 0.95, ref.zero = F, portion = 100, xlsx = NULL, cat = T)`
- `...`: optional. one or more regression Pass extra expressions explicitly.
- `nknots`: optional; default `NULL`; standard `NULL`. number of knots Preserve the package default.
- `reference`: optional; default `"median"`; standard `"median"`. reference, default is median Preserve the package default.
- `by`: optional; default `NULL`; standard `NULL`. one or more variable Preserve the package default.
- `conf.int`: optional; default `0.95`; standard `0.95`.  Preserve the package default.
- `ref.zero`: optional; default `F`; standard `F`.  Preserve the package default.
- `portion`: optional; default `100`; standard `100`.  Preserve the package default.
- `xlsx`: optional; default `NULL`; standard `NULL`.  Preserve the package default.
- `cat`: optional; default `T`; standard `T`.  Preserve the package default.

## km_plot
Title: km曲线
Description: km曲线
Category: `plot_model`
Usage: `km_plot( time, y, x = NULL, ck = T, color = NULL, linewidth = 0.6, median.line = F, conf.int = T, alpha = 0.3, pval.xy = NULL, xlim = NULL, ylim = NULL, break.x.by = NULL, axis.title.size = 13, xlab = "Time", ylab = "Survival porbability", legend.labs = NULL, legend.title = NULL, legend.title.size = 11.5, risk.table = T, risk.table.height = 2, risk.title.size = 13, file = NULL, width = par("din")[1], height = par("din")[2], unit = "in", dpi = 300 )`
Standard call: `km_plot(time = NULL, y = NULL, x = NULL, ck = T, color = NULL, linewidth = 0.6, median.line = F, conf.int = T, alpha = 0.3, pval.xy = NULL, xlim = NULL, ylim = NULL, break.x.by = NULL, axis.title.size = 13, xlab = "Time", ylab = "Survival porbability", legend.labs = NULL, legend.title = NULL, legend.title.size = 11.5, risk.table = T, risk.table.height = 2, risk.title.size = 13, file = NULL, width = par("din")[1], height = par("din")[2], unit = "in", dpi = 300)`
- `time`: required; standard `NULL`. time Required but not inferable from metadata alone; confirm before execution.
- `y`: required; standard `NULL`. y Required but not inferable from metadata alone; confirm before execution.
- `x`: optional; default `NULL`; standard `NULL`. x Preserve the package default.
- `ck`: optional; default `T`; standard `T`. 条件 Preserve the package default.
- `color`: optional; default `NULL`; standard `NULL`. 颜色 Preserve the package default.
- `linewidth`: optional; default `0.6`; standard `0.6`. 线宽 Preserve the package default.
- `median.line`: optional; default `F`; standard `F`. 中位随访时间线 Preserve the package default.
- `conf.int`: optional; default `T`; standard `T`. 可信区间 Preserve the package default.
- `alpha`: optional; default `0.3`; standard `0.3`. 可信区间透明度 Preserve the package default.
- `pval.xy`: optional; default `NULL`; standard `NULL`. p值坐标 Preserve the package default.
- `xlim`: optional; default `NULL`; standard `NULL`. x轴范围 Preserve the package default.
- `ylim`: optional; default `NULL`; standard `NULL`. y轴范围 Preserve the package default.
- `break.x.by`: optional; default `NULL`; standard `NULL`. x轴坐标间隔 Preserve the package default.
- `axis.title.size`: optional; default `13`; standard `13`. 坐标轴标题大小 Preserve the package default.
- `xlab`: optional; default `"Time"`; standard `"Time"`. x轴标题 Preserve the package default.
- `ylab`: optional; default `"Survival porbability"`; standard `"Survival porbability"`. y轴标题 Preserve the package default.
- `legend.labs`: optional; default `NULL`; standard `NULL`. 图例文本 Preserve the package default.
- `legend.title`: optional; default `NULL`; standard `NULL`. 图例标题 Preserve the package default.
- `legend.title.size`: optional; default `11.5`; standard `11.5`. 图例标题大小 Preserve the package default.
- `risk.table`: optional; default `T`; standard `T`. 风险表格 Preserve the package default.
- `risk.table.height`: optional; default `2`; standard `2`.  Preserve the package default.
- `risk.title.size`: optional; default `13`; standard `13`. 风险表格标题大小 Preserve the package default.
- `file`: optional; default `NULL`; standard `NULL`. 文件名 Preserve the package default.
- `width`: optional; default `par("din")[1]`; standard `par("din")[1]`. 宽度 Preserve the package default.
- `height`: optional; default `par("din")[2]`; standard `par("din")[2]`. 高度 Preserve the package default.
- `unit`: optional; default `"in"`; standard `"in"`. 单位 Preserve the package default.
- `dpi`: optional; default `300`; standard `300`. 分辨率 Preserve the package default.

## forestplot
Title: 森林图
Description: 森林图
Category: `plot_model`
Usage: `forestplot(x, ...)`
Standard call: `forestplot(x = NULL)`
- `x`: required; standard `NULL`.  Required but not inferable from metadata alone; confirm before execution.
- `...`: optional.  Pass extra expressions explicitly.

## missValue
Title: 查看数据的缺失值
Description: 查看数据的缺失值
Category: `missing_data`
Usage: `missValue(data)`
Standard call: `missValue(data = analytic_dat)`
- `data`: required; standard `analytic_dat`. 数据 Use the standard data object name for this stage.

## mice2
Title: 使用mice包来处理缺失值
Description: 参考文献doi:10.18637/jss.v045.i03
Category: `missing_data`
Usage: `mice2(d, seed = 1)`
Standard call: `mice2(d = NULL, seed = 1)`
- `d`: required; standard `NULL`. 数据 Required but not inferable from metadata alone; confirm before execution.
- `seed`: optional; default `1`; standard `1`. 随机种子 Preserve the package default.

## missForest2
Title: 使用missForest包处理缺失值
Description: 参考文献PMID: 22039212
Category: `missing_data`
Usage: `missForest2(d, ntree = 5, seed = 1)`
Standard call: `missForest2(d = NULL, ntree = 5, seed = 1)`
- `d`: required; standard `NULL`. 数据 Required but not inferable from metadata alone; confirm before execution.
- `ntree`: optional; default `5`; standard `5`.  Preserve the package default.
- `seed`: optional; default `1`; standard `1`.  Preserve the package default.


