# Data Directory

## Overview

This directory contains both raw and processed datasets for the insurance CX analysis project.

---

## Directory Structure

```
data/
├── raw/                    # Original, unmodified datasets
│   └── insurance_data.csv  # Original Kaggle dataset (not tracked in git)
│
└── processed/              # Cleaned and processed datasets
    └── insurance_data_clean.csv  # Cleaned dataset with engineered features
```

---

## Dataset Information

### Known Limitations (Mock Data)
⚠️ **Unrealistic Risk-Cost Relationships:** Health risk factors (smoking, obesity, cholesterol, glucose) show minimal to inverse correlation with insurance costs. In real insurance data, these would be strong positive predictors due to actuarial pricing.

This limitation affects:
- Cost prediction models (weak health risk signals)
- Segment profiling (similar costs across risk levels)
- Business insights (must be interpreted cautiously)

**Implication:** Analysis focuses on demonstrating analytical methodology rather than claiming real-world pricing insights.

### Raw Data: `insurance_data.csv`
- **Source:** Kaggle Health Insurance Dataset (mock data)
- **Size:** 25,000 rows × 24 columns
- **Date Acquired:** December 2025
- **Missing Values:** BMI (990), Year_last_admitted (11,881)
- **Data Quality Issues:** Typo in Occupation column ("Salried")

### Processed Data: `insurance_data_clean.csv`
- **Size:** 25,000 rows × 35 columns
- **Processing Date:** December 28, 2025
- **Modifications:**
  - BMI imputed using gender/age-stratified median
  - Occupation typo corrected
  - 11 engineered features added
  - All categorical variables standardized

---

## Features

### Original Features (24)

**Customer Identifiers:**
- `applicant_id` - Unique customer ID

**Demographics:**
- `age` - Customer age (16-74 years)
- `Gender` - Male/Female
- `Occupation` - Salaried, Business, Student
- `Location` - City (15 unique cities in India)

**Health Metrics:**
- `bmi` - Body Mass Index
- `weight` - Weight in kg
- `cholesterol_level` - Categorical ranges (e.g., "150 to 175")
- `avg_glucose_level` - Average glucose level
- `fat_percentage` - Body fat percentage
- `smoking_status` - never smoked, formerly smoked, smokes, Unknown
- `heart_decs_history` - Heart disease history (binary)
- `other_major_decs_history` - Other major disease history (binary)

**Lifestyle:**
- `exercise` - No, Moderate, Extreme
- `Alcohol` - No, Rare, Daily
- `daily_avg_steps` - Average daily step count
- `adventure_sports` - Participation in adventure sports (binary)
- `weight_change_in_last_one_year` - Weight change

**Healthcare Engagement:**
- `years_of_insurance_with_us` - Customer tenure (0-8 years)
- `regular_checkup_lasy_year` - Number of regular checkups
- `visited_doctor_last_1_year` - Number of doctor visits
- `Year_last_admitted` - Last hospital admission year (missing = never admitted)

**Business Metrics:**
- `insurance_cost` - Annual insurance premium ($2,468 - $67,870)
- `covered_by_any_other_company` - Has other insurance (Y/N)

---

### Engineered Features (11)

**Segmentation:**
- `tenure_segment` - New (0-2yr), Established (3-5yr), Loyal (6-8yr)
- `age_group` - 18-30, 31-45, 46-60, 60+
- `bmi_category` - Underweight, Normal, Overweight, Obese (WHO standards)

**Health Risk Indicators:**
- `high_cholesterol` - Binary flag (≥200 mg/dL)
- `high_glucose` - Binary flag (≥140 mg/dL)
- `obesity` - Binary flag (BMI ≥30)
- `smoker` - Binary flag (current or former smoker)
- `health_risk_score` - Composite score 0-4 (sum of above 4 flags)

**Derived Features:**
- `cholesterol_numeric` - Numeric midpoint from categorical ranges
- `ever_admitted` - Binary flag (has hospital admission history)
- `has_other_coverage` - Binary flag (has dual insurance coverage)

---

## Data Quality Report

### Completeness
- Original dataset: 98.4% complete
- After cleaning: 100% complete (except intentional Year_last_admitted)

### Validity
- All numeric values within expected ranges
- No negative insurance costs
- Age range: 16-74 (336 customers <18 years flagged but retained)
- BMI range: 12.3-100.6 (570 extreme values flagged but retained)

### Consistency
- All categorical values standardized
- No duplicate applicant IDs
- Occupation typo corrected (4,811 records)

---

## Usage Notes

### For Analysis
```python
import pandas as pd

# Load cleaned data
df = pd.read_csv('data/processed/insurance_data_clean.csv')

# Check data
print(df.shape)  # (25000, 35)
print(df.isnull().sum())  # Verify data quality
```

### Important Considerations

1. **Missing Year_last_admitted:** Not imputed - missing values indicate "never admitted" which is valuable information. Use `ever_admitted` binary flag when needed.

2. **Extreme BMI values:** Some BMI values >50 retained as potentially valid (severe obesity). Review outliers for your specific analysis needs.

3. **Age <18:** 336 customers under 18 years retained. Verify if this is appropriate for your analysis context.

4. **Health Risk Score:** Composite score should not replace individual risk factor analysis - use both aggregate and detailed views.

5. **Data Privacy:** This is mock/synthetic data. No real customer PII included.

---

## Data Dictionary

For detailed feature descriptions and metadata, see: `docs/data_dictionary.md`

---

## Changelog

### 2025-12-28 - Phase 1 Data Cleaning
- Imputed 990 missing BMI values
- Corrected Occupation typo (Salried → Salaried)
- Created 11 engineered features
- Standardized all categorical variables
- Validated numeric ranges
- Exported cleaned dataset

---

**Data Steward:** Rodion Barskov 
**Last Updated:** December 28, 2025
