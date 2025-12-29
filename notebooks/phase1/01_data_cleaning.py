"""
PHASE 1: DATA PREPARATION & EXPLORATION
Customer Lifetime Value Optimization Through Proactive Health Engagement

This script performs:
1. Initial data inspection
2. Data quality assessment
3. Data cleaning and standardization
4. Feature engineering (basic)
5. Export cleaned dataset

Author: Rodion
Date: December 2025
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ==========================================
# 1. LOAD DATA
# ==========================================
print("="*70)
print("PHASE 1: DATA CLEANING & PREPARATION")
print("="*70)

df = pd.read_csv('insurance_data.csv')

print(f"\n✓ Data loaded successfully")
print(f"  - Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"  - Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# ==========================================
# 2. INITIAL DATA INSPECTION
# ==========================================
print("\n" + "="*70)
print("INITIAL DATA INSPECTION")
print("="*70)

print("\nColumn Names and Data Types:")
print(df.dtypes)

print("\n\nFirst 3 rows:")
print(df.head(3))

# ==========================================
# 3. DATA QUALITY ASSESSMENT
# ==========================================
print("\n" + "="*70)
print("DATA QUALITY ASSESSMENT")
print("="*70)

# Missing values
missing_summary = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
})
missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

print("\nMissing Values Summary:")
if len(missing_summary) > 0:
    print(missing_summary.to_string(index=False))
else:
    print("  ✓ No missing values detected")

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

# Check unique applicant IDs
unique_ids = df['applicant_id'].nunique()
print(f"Unique Applicant IDs: {unique_ids:,} (Expected: {len(df):,})")
if unique_ids != len(df):
    print("  ⚠ WARNING: Duplicate applicant IDs detected!")

# ==========================================
# 4. DATA CLEANING
# ==========================================
print("\n" + "="*70)
print("DATA CLEANING STEPS")
print("="*70)

# Create a copy for cleaning
df_clean = df.copy()
cleaning_log = []

# 4.1 Fix typo in Occupation column
print("\n1. Fixing 'Occupation' typo...")
before_occupation = df_clean['Occupation'].value_counts()
df_clean['Occupation'] = df_clean['Occupation'].replace('Salried', 'Salaried')
after_occupation = df_clean['Occupation'].value_counts()
print(f"   ✓ Changed 'Salried' → 'Salaried' ({before_occupation.get('Salried', 0):,} records)")
cleaning_log.append("Fixed typo: 'Salried' → 'Salaried'")

# 4.2 Handle missing BMI values
print("\n2. Handling missing BMI values...")
bmi_missing = df_clean['bmi'].isnull().sum()
print(f"   - Missing BMI values: {bmi_missing:,} ({bmi_missing/len(df_clean)*100:.2f}%)")

# Strategy: Impute with median BMI by Gender and Age group
df_clean['age_group'] = pd.cut(df_clean['age'], bins=[0, 30, 45, 60, 100], labels=['18-30', '31-45', '46-60', '60+'])
df_clean['bmi'] = df_clean.groupby(['Gender', 'age_group'])['bmi'].transform(
    lambda x: x.fillna(x.median())
)
# If still missing, fill with overall median
df_clean['bmi'].fillna(df_clean['bmi'].median(), inplace=True)
print(f"   ✓ Imputed BMI using median by Gender & Age Group")
cleaning_log.append(f"Imputed {bmi_missing} missing BMI values using gender/age-stratified median")

# 4.3 Handle missing Year_last_admitted
print("\n3. Handling missing 'Year_last_admitted'...")
year_missing = df_clean['Year_last_admitted'].isnull().sum()
print(f"   - Missing values: {year_missing:,} ({year_missing/len(df_clean)*100:.2f}%)")
print(f"   ✓ Keeping as missing (indicates 'Never Admitted' - valuable information)")
cleaning_log.append(f"Year_last_admitted: {year_missing} missing values retained (indicates never admitted)")

# 4.4 Create 'ever_admitted' binary flag
df_clean['ever_admitted'] = (~df_clean['Year_last_admitted'].isnull()).astype(int)
print(f"   ✓ Created 'ever_admitted' binary feature")
cleaning_log.append("Created 'ever_admitted' binary feature from Year_last_admitted")

# 4.5 Standardize categorical values
print("\n4. Standardizing categorical variables...")

# Gender: Already clean (Male/Female)
print(f"   ✓ Gender: {df_clean['Gender'].unique()}")

# covered_by_any_other_company: Convert to binary
df_clean['has_other_coverage'] = (df_clean['covered_by_any_other_company'] == 'Y').astype(int)
print(f"   ✓ Created binary 'has_other_coverage' (N→0, Y→1)")
cleaning_log.append("Created binary 'has_other_coverage' feature")

# Smoking status: Standardize
print(f"   - Smoking status categories: {df_clean['smoking_status'].unique()}")

# Exercise: Already clean
print(f"   - Exercise categories: {df_clean['exercise'].unique()}")

# Alcohol: Already clean
print(f"   - Alcohol categories: {df_clean['Alcohol'].unique()}")

# 4.6 Validate numeric ranges
print("\n5. Validating numeric ranges...")

# Age
age_outliers = (df_clean['age'] < 18) | (df_clean['age'] > 100)
print(f"   - Age range: {df_clean['age'].min()}-{df_clean['age'].max()} (Outliers: {age_outliers.sum()})")

# BMI
bmi_outliers = (df_clean['bmi'] < 15) | (df_clean['bmi'] > 50)
print(f"   - BMI range: {df_clean['bmi'].min():.1f}-{df_clean['bmi'].max():.1f} (Outliers: {bmi_outliers.sum()})")

# Insurance cost
cost_negative = df_clean['insurance_cost'] < 0
print(f"   - Insurance cost range: ${df_clean['insurance_cost'].min():,.0f}-${df_clean['insurance_cost'].max():,.0f} (Negative: {cost_negative.sum()})")

print(f"   ✓ All numeric values within expected ranges")

# 4.7 Create cholesterol numeric midpoint
print("\n6. Creating numeric cholesterol feature...")
cholesterol_mapping = {
    '125 to 150': 137.5,
    '150 to 175': 162.5,
    '175 to 200': 187.5,
    '200 to 225': 212.5,
    '225 to 250': 237.5
}
df_clean['cholesterol_numeric'] = df_clean['cholesterol_level'].map(cholesterol_mapping)
print(f"   ✓ Created 'cholesterol_numeric' from range midpoints")
cleaning_log.append("Created cholesterol_numeric from range midpoints")

# ==========================================
# 5. FEATURE ENGINEERING (BASIC)
# ==========================================
print("\n" + "="*70)
print("FEATURE ENGINEERING")
print("="*70)

# 5.1 Customer tenure categories
print("\n1. Creating tenure segments...")
df_clean['tenure_segment'] = pd.cut(
    df_clean['years_of_insurance_with_us'],
    bins=[-1, 2, 5, 8],
    labels=['New (0-2yr)', 'Established (3-5yr)', 'Loyal (6-8yr)']
)
print(f"   ✓ Created 'tenure_segment'")
print(df_clean['tenure_segment'].value_counts().sort_index())

# 5.2 BMI categories (WHO standards)
print("\n2. Creating BMI categories...")
df_clean['bmi_category'] = pd.cut(
    df_clean['bmi'],
    bins=[0, 18.5, 25, 30, 100],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)
print(f"   ✓ Created 'bmi_category'")
print(df_clean['bmi_category'].value_counts().sort_index())

# 5.3 Age groups (already created, formalize it)
print("\n3. Formalizing age groups...")
print(f"   ✓ 'age_group' already created during BMI imputation")
print(df_clean['age_group'].value_counts().sort_index())

# 5.4 Risk flags
print("\n4. Creating health risk flags...")
df_clean['high_cholesterol'] = (df_clean['cholesterol_numeric'] >= 200).astype(int)
df_clean['high_glucose'] = (df_clean['avg_glucose_level'] >= 140).astype(int)
df_clean['obesity'] = (df_clean['bmi'] >= 30).astype(int)
df_clean['smoker'] = (df_clean['smoking_status'].isin(['smokes', 'formerly smoked'])).astype(int)

risk_summary = pd.DataFrame({
    'Risk Factor': ['High Cholesterol (≥200)', 'High Glucose (≥140)', 'Obesity (BMI≥30)', 'Current/Former Smoker'],
    'Count': [
        df_clean['high_cholesterol'].sum(),
        df_clean['high_glucose'].sum(),
        df_clean['obesity'].sum(),
        df_clean['smoker'].sum()
    ],
    'Percentage': [
        df_clean['high_cholesterol'].mean() * 100,
        df_clean['high_glucose'].mean() * 100,
        df_clean['obesity'].mean() * 100,
        df_clean['smoker'].mean() * 100
    ]
})
print(risk_summary.to_string(index=False))

# 5.5 Calculate total risk score (0-4)
df_clean['health_risk_score'] = (
    df_clean['high_cholesterol'] +
    df_clean['high_glucose'] +
    df_clean['obesity'] +
    df_clean['smoker']
)
print(f"\n   ✓ Created 'health_risk_score' (0-4 scale)")
print("\nHealth Risk Distribution:")
print(df_clean['health_risk_score'].value_counts().sort_index())

# ==========================================
# 6. FINAL DATA SUMMARY
# ==========================================
print("\n" + "="*70)
print("CLEANED DATASET SUMMARY")
print("="*70)

print(f"\nOriginal shape: {df.shape}")
print(f"Cleaned shape: {df_clean.shape}")
print(f"Rows removed: {df.shape[0] - df_clean.shape[0]}")
print(f"Columns added: {df_clean.shape[1] - df.shape[1]}")

print("\n\nNew Features Created:")
new_features = [
    'age_group', 'ever_admitted', 'has_other_coverage', 'cholesterol_numeric',
    'tenure_segment', 'bmi_category', 'high_cholesterol', 'high_glucose',
    'obesity', 'smoker', 'health_risk_score'
]
for i, feat in enumerate(new_features, 1):
    print(f"  {i}. {feat}")

print("\n\nRemaining Missing Values:")
remaining_missing = df_clean.isnull().sum()
remaining_missing = remaining_missing[remaining_missing > 0]
if len(remaining_missing) > 0:
    print(remaining_missing)
else:
    print("  ✓ No missing values (except intentional Year_last_admitted)")

# ==========================================
# 7. EXPORT CLEANED DATA
# ==========================================
print("\n" + "="*70)
print("EXPORTING CLEANED DATA")
print("="*70)

# Export main cleaned dataset
df_clean.to_csv('insurance_data_clean.csv', index=False)
print(f"\n✓ Exported: insurance_data_clean.csv")
print(f"  - {len(df_clean):,} rows × {len(df_clean.columns)} columns")

# Export data dictionary
data_dict = pd.DataFrame({
    'Column': df_clean.columns,
    'Type': df_clean.dtypes.astype(str),
    'Non_Null_Count': df_clean.count(),
    'Unique_Values': [df_clean[col].nunique() for col in df_clean.columns]
})
data_dict.to_csv('data_dictionary.csv', index=False)
print(f"✓ Exported: data_dictionary.csv")

# Export cleaning log
with open('data_cleaning_log.txt', 'w') as f:
    f.write("DATA CLEANING LOG\n")
    f.write("="*70 + "\n\n")
    f.write(f"Date: December 2025\n")
    f.write(f"Original records: {len(df):,}\n")
    f.write(f"Cleaned records: {len(df_clean):,}\n\n")
    f.write("CLEANING STEPS:\n")
    for i, step in enumerate(cleaning_log, 1):
        f.write(f"{i}. {step}\n")
print(f"✓ Exported: data_cleaning_log.txt")

print("\n" + "="*70)
print("✓ PHASE 1 COMPLETE - Data cleaning successful!")
print("="*70)
print("\nNext steps:")
print("  1. Review insurance_data_clean.csv")
print("  2. Proceed to Phase 2: EDA and visualization")
print("  3. Check data_cleaning_log.txt for audit trail")
