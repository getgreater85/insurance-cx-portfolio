# Data Dictionary
## Insurance CX Portfolio Project

**Dataset:** Health Insurance Customer Data  
**Last Updated:** December 28, 2025  
**Total Features:** 35 (24 original + 11 engineered)

---

## Table of Contents
- [Customer Identifiers](#customer-identifiers)
- [Demographics](#demographics)
- [Health Metrics](#health-metrics)
- [Lifestyle Factors](#lifestyle-factors)
- [Healthcare Engagement](#healthcare-engagement)
- [Business Metrics](#business-metrics)
- [Engineered Features](#engineered-features)

---

## Customer Identifiers

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `applicant_id` | Integer | Unique customer identifier | 5000-29999 | Primary key, no duplicates |

---

## Demographics

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `age` | Integer | Customer age in years | 16-74 | 336 customers <18 years |
| `Gender` | Categorical | Customer gender | Male, Female | Male: 65.7%, Female: 34.3% |
| `Occupation` | Categorical | Employment type | Salaried, Business, Student | Student: 40.7%, Business: 40.1%, Salaried: 19.2% |
| `Location` | Categorical | City of residence | 15 Indian cities | Bangalore, Jaipur, Bhubaneswar, etc. |
| `weight` | Integer | Body weight in kilograms | Variable | Used for BMI calculation |

---

## Health Metrics

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `bmi` | Float | Body Mass Index | 12.3-100.6 | 990 missing values imputed; 570 extreme values flagged |
| `cholesterol_level` | Categorical | Cholesterol range | "125 to 150", "150 to 175", "175 to 200", "200 to 225", "225 to 250" | 5 categories in mg/dL |
| `avg_glucose_level` | Integer | Average glucose level | Variable | ≥140 considered high |
| `fat_percentage` | Integer | Body fat percentage | 11-42% | Health indicator |
| `heart_decs_history` | Binary | History of heart disease | 0 (No), 1 (Yes) | Health risk flag |
| `other_major_decs_history` | Binary | History of other major diseases | 0 (No), 1 (Yes) | Health risk flag |
| `smoking_status` | Categorical | Smoking behavior | never smoked, formerly smoked, smokes, Unknown | 37% never smoked, 30% Unknown, 17% formerly smoked, 15% smokes |

---

## Lifestyle Factors

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `exercise` | Categorical | Exercise frequency level | No, Moderate, Extreme | Moderate: 58.6%, Extreme: 21.0%, No: 20.5% |
| `Alcohol` | Categorical | Alcohol consumption | No, Rare, Daily | Rare: 55.0%, No: 34.2%, Daily: 10.8% |
| `daily_avg_steps` | Integer | Average daily step count | 2034-11255 | Fitness indicator; mean: 5,216 steps |
| `adventure_sports` | Binary | Participates in adventure sports | 0 (No), 1 (Yes) | Risk activity indicator |
| `weight_change_in_last_one_year` | Integer | Weight change in kg | Variable | Positive = gain, Negative = loss |

---

## Healthcare Engagement

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `years_of_insurance_with_us` | Integer | Customer tenure in years | 0-8 | Key retention metric; mean: 4.1 years |
| `regular_checkup_lasy_year` | Integer | Number of regular checkups last year | 0-5 | Preventive care indicator; mean: 0.77 |
| `visited_doctor_last_1_year` | Integer | Number of doctor visits last year | 0-12 | Healthcare utilization; mean: 3.10 |
| `Year_last_admitted` | Float | Year of last hospital admission | 1994-2017 or NaN | 47.5% missing (never admitted) |

---

## Business Metrics

| Feature | Type | Description | Range/Values | Notes |
|---------|------|-------------|--------------|-------|
| `insurance_cost` | Integer | Annual insurance premium in USD | $2,468-$67,870 | Target variable for analysis; mean: $27,147 |
| `covered_by_any_other_company` | Categorical | Has other insurance coverage | Y (Yes), N (No) | Competitive indicator; 30.3% have dual coverage |

---

## Engineered Features

### Segmentation Features

| Feature | Type | Description | Values | Calculation Logic |
|---------|------|-------------|--------|-------------------|
| `tenure_segment` | Categorical | Customer tenure category | New (0-2yr), Established (3-5yr), Loyal (6-8yr) | Based on `years_of_insurance_with_us` |
| `age_group` | Categorical | Age bracket | 18-30, 31-45, 46-60, 60+ | Binned from `age` |
| `bmi_category` | Categorical | BMI classification (WHO) | Underweight, Normal, Overweight, Obese | <18.5, 18.5-25, 25-30, ≥30 |

**Distribution:**
- Tenure: New 30.3%, Established 35.1%, Loyal 34.6%
- Age: 18-30: 23.9%, 31-45: 27.6%, 46-60: 26.5%, 60+: 22.1%
- BMI: Underweight 2.0%, Normal 17.5%, Overweight 26.7%, Obese 53.7%

---

### Health Risk Indicators

| Feature | Type | Description | Threshold | Prevalence |
|---------|------|-------------|-----------|------------|
| `high_cholesterol` | Binary | Elevated cholesterol flag | ≥200 mg/dL | 20.1% (5,017 customers) |
| `high_glucose` | Binary | Elevated glucose flag | ≥140 mg/dL | 62.8% (15,710 customers) |
| `obesity` | Binary | Obesity flag | BMI ≥30 | 54.3% (13,578 customers) |
| `smoker` | Binary | Current/former smoker flag | smokes OR formerly smoked | 32.8% (8,196 customers) |
| `health_risk_score` | Integer | Composite health risk score | 0-4 | Sum of above 4 binary flags |

**Health Risk Score Distribution:**
- 0 (No risk factors): 9.8%
- 1: 33.3%
- 2: 36.4% ← Most common
- 3: 17.9%
- 4 (All risk factors): 2.5%

---

### Derived Features

| Feature | Type | Description | Source | Calculation |
|---------|------|-------------|--------|-------------|
| `cholesterol_numeric` | Float | Numeric cholesterol value | `cholesterol_level` | Midpoint of categorical range (e.g., "150 to 175" → 162.5) |
| `ever_admitted` | Binary | Has hospital admission history | `Year_last_admitted` | 1 if Year_last_admitted is not null, else 0 |
| `has_other_coverage` | Binary | Has dual insurance coverage | `covered_by_any_other_company` | 1 if 'Y', else 0 |

---

## Feature Statistics

### Numerical Features Summary

| Feature | Mean | Median | Std Dev | Min | Max |
|---------|------|--------|---------|-----|-----|
| age | 44.9 | 45.0 | 16.1 | 16 | 74 |
| bmi | 31.4 | 30.7 | 7.7 | 12.3 | 100.6 |
| insurance_cost | $27,147 | $27,148 | $14,324 | $2,468 | $67,870 |
| years_of_insurance_with_us | 4.1 | 4.0 | 2.6 | 0 | 8 |
| avg_glucose_level | 169.1 | 162.5 | 31.5 | Variable | Variable |
| cholesterol_numeric | 169.1 | 162.5 | 31.5 | 137.5 | 237.5 |
| daily_avg_steps | 5,216 | 5,089 | 1,053 | 2,034 | 11,255 |
| regular_checkup_lasy_year | 0.77 | 0 | 1.16 | 0 | 5 |
| visited_doctor_last_1_year | 3.10 | 3 | 1.44 | 0 | 12 |
| health_risk_score | 1.70 | 2 | 0.97 | 0 | 4 |

---

## Data Quality Notes

### Missing Values
- **BMI:** 990 missing (3.96%) - Imputed using gender/age-stratified median
- **Year_last_admitted:** 11,881 missing (47.5%) - Intentionally retained; indicates "never admitted"
- **bmi_category:** 1 missing (edge case after imputation)

### Data Corrections Applied
- **Occupation typo:** "Salried" corrected to "Salaried" (4,811 records)

### Outliers Identified (Retained)
- **Age <18:** 336 customers (1.3%)
- **BMI extremes:** 570 customers with BMI <15 or >50 (2.3%)
- No negative or invalid insurance costs

### Validation Checks Passed
✅ No duplicate applicant_id  
✅ All categorical values standardized  
✅ Numeric ranges validated  
✅ No impossible values (e.g., negative age)  

---

## Usage Guidelines

### For Predictive Modeling
- **Target Variable:** `insurance_cost` (regression) or derived churn flag (classification)
- **Key Predictors:** tenure_segment, health_risk_score, has_other_coverage, bmi_category, smoking_status
- **Avoid Multicollinearity:** Don't use both `cholesterol_level` and `cholesterol_numeric` together

### For Customer Segmentation
- **Recommended Features:** tenure_segment, age_group, bmi_category, health_risk_score, has_other_coverage
- **Engagement Metrics:** regular_checkup_lasy_year, visited_doctor_last_1_year, ever_admitted

### For CX Analysis
- **Retention Indicators:** years_of_insurance_with_us, has_other_coverage
- **Engagement Metrics:** regular_checkup_lasy_year, visited_doctor_last_1_year
- **Value Metrics:** insurance_cost (proxy for CLV)

---

## Feature Relationships

### Strong Correlations
- `insurance_cost` ↔ `ever_admitted`: r = 0.164
- `insurance_cost` ↔ `has_other_coverage`: r = 0.102
- `bmi` ↔ `weight`: r = high (expected)

### Weak/No Correlations (Surprising)
- `insurance_cost` ↔ `health_risk_score`: r = -0.007
- `insurance_cost` ↔ `years_of_insurance_with_us`: r = 0.001
- Indicates pricing may not be strongly risk-adjusted

---

## Version History

### v1.0 - December 28, 2025 (Phase 1)
- Original 24 features documented
- 11 engineered features added
- Data quality assessment completed
- Missing value treatment documented
- Feature statistics calculated

---

## References

**WHO BMI Categories:**
- Underweight: <18.5
- Normal: 18.5-24.9
- Overweight: 25-29.9
- Obese: ≥30

**Medical Thresholds:**
- High Cholesterol: ≥200 mg/dL
- High Glucose: ≥140 mg/dL (prediabetes/diabetes indicator)

---

**Maintained By:** Rodion  
**Project:** Insurance CX Portfolio  
**Last Updated:** December 28, 2025
