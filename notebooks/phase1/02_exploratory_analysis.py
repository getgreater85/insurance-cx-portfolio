"""
PHASE 1 (Part 2): EXPLORATORY DATA ANALYSIS
Customer Lifetime Value Optimization Through Proactive Health Engagement

This script performs comprehensive EDA including:
1. Univariate analysis (distributions)
2. Bivariate analysis (relationships)
3. Correlation analysis
4. Customer segment profiling
5. Key business insights visualization

Author: Rodion
Date: December 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================
print("="*70)
print("EXPLORATORY DATA ANALYSIS - PHASE 1")
print("="*70)

df = pd.read_csv('insurance_data_clean.csv')
print(f"\n✓ Loaded cleaned data: {df.shape[0]:,} rows × {df.shape[1]} columns\n")

# ==========================================
# 2. UNIVARIATE ANALYSIS
# ==========================================
print("="*70)
print("UNIVARIATE ANALYSIS")
print("="*70)

# 2.1 Numerical variables distribution
print("\nNumerical Variables - Descriptive Statistics:")
numerical_cols = ['age', 'bmi', 'insurance_cost', 'years_of_insurance_with_us', 
                  'avg_glucose_level', 'cholesterol_numeric', 'daily_avg_steps']
print(df[numerical_cols].describe().round(2))

# 2.2 Key metrics
print("\n\nKey Business Metrics:")
print(f"  • Average insurance cost: ${df['insurance_cost'].mean():,.2f}")
print(f"  • Median insurance cost: ${df['insurance_cost'].median():,.2f}")
print(f"  • Average customer tenure: {df['years_of_insurance_with_us'].mean():.1f} years")
print(f"  • Average age: {df['age'].mean():.1f} years")
print(f"  • Average BMI: {df['bmi'].mean():.1f}")

# Create comprehensive distribution plots
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Distribution of Key Variables', fontsize=16, fontweight='bold', y=1.00)

# Age distribution
axes[0, 0].hist(df['age'], bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].axvline(df['age'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age"].mean():.1f}')
axes[0, 0].legend()

# Insurance cost distribution
axes[0, 1].hist(df['insurance_cost'], bins=40, edgecolor='black', alpha=0.7, color='coral')
axes[0, 1].set_xlabel('Insurance Cost ($)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Insurance Cost Distribution')
axes[0, 1].axvline(df['insurance_cost'].median(), color='red', linestyle='--', linewidth=2, label=f'Median: ${df["insurance_cost"].median():,.0f}')
axes[0, 1].legend()

# Tenure distribution
tenure_counts = df['years_of_insurance_with_us'].value_counts().sort_index()
axes[0, 2].bar(tenure_counts.index, tenure_counts.values, edgecolor='black', alpha=0.7, color='lightgreen')
axes[0, 2].set_xlabel('Years of Insurance')
axes[0, 2].set_ylabel('Number of Customers')
axes[0, 2].set_title('Customer Tenure Distribution')
axes[0, 2].set_xticks(range(9))

# BMI distribution
axes[1, 0].hist(df['bmi'], bins=30, edgecolor='black', alpha=0.7, color='plum')
axes[1, 0].set_xlabel('BMI')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('BMI Distribution')
axes[1, 0].axvline(df['bmi'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["bmi"].mean():.1f}')
axes[1, 0].axvline(30, color='orange', linestyle='--', linewidth=2, label='Obesity threshold')
axes[1, 0].legend()

# Cholesterol distribution
axes[1, 1].hist(df['cholesterol_numeric'], bins=20, edgecolor='black', alpha=0.7, color='gold')
axes[1, 1].set_xlabel('Cholesterol Level')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Cholesterol Distribution')
axes[1, 1].axvline(200, color='red', linestyle='--', linewidth=2, label='High cholesterol (≥200)')
axes[1, 1].legend()

# Glucose distribution
axes[1, 2].hist(df['avg_glucose_level'], bins=30, edgecolor='black', alpha=0.7, color='lightcoral')
axes[1, 2].set_xlabel('Average Glucose Level')
axes[1, 2].set_ylabel('Frequency')
axes[1, 2].set_title('Glucose Level Distribution')
axes[1, 2].axvline(140, color='red', linestyle='--', linewidth=2, label='High glucose (≥140)')
axes[1, 2].legend()

# Health risk score
risk_counts = df['health_risk_score'].value_counts().sort_index()
axes[2, 0].bar(risk_counts.index, risk_counts.values, edgecolor='black', alpha=0.7, color='salmon')
axes[2, 0].set_xlabel('Health Risk Score (0-4)')
axes[2, 0].set_ylabel('Number of Customers')
axes[2, 0].set_title('Health Risk Score Distribution')

# Gender distribution
gender_counts = df['Gender'].value_counts()
axes[2, 1].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
axes[2, 1].set_title('Gender Distribution')

# Tenure segments
tenure_seg_counts = df['tenure_segment'].value_counts()
axes[2, 2].barh(tenure_seg_counts.index, tenure_seg_counts.values, edgecolor='black', alpha=0.7, color='teal')
axes[2, 2].set_xlabel('Number of Customers')
axes[2, 2].set_title('Customer Tenure Segments')

plt.tight_layout()
plt.savefig('01_univariate_distributions.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: 01_univariate_distributions.png")
plt.close()

# ==========================================
# 3. BIVARIATE ANALYSIS
# ==========================================
print("\n" + "="*70)
print("BIVARIATE ANALYSIS")
print("="*70)

# 3.1 Insurance cost by categorical variables
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Insurance Cost by Customer Segments', fontsize=16, fontweight='bold')

# By tenure segment
df.boxplot(column='insurance_cost', by='tenure_segment', ax=axes[0, 0])
axes[0, 0].set_title('Insurance Cost by Tenure')
axes[0, 0].set_xlabel('Tenure Segment')
axes[0, 0].set_ylabel('Insurance Cost ($)')
axes[0, 0].get_figure().suptitle('')

# By BMI category
df.boxplot(column='insurance_cost', by='bmi_category', ax=axes[0, 1])
axes[0, 1].set_title('Insurance Cost by BMI Category')
axes[0, 1].set_xlabel('BMI Category')
axes[0, 1].set_ylabel('Insurance Cost ($)')
axes[0, 1].tick_params(axis='x', rotation=45)

# By smoking status
df.boxplot(column='insurance_cost', by='smoking_status', ax=axes[0, 2])
axes[0, 2].set_title('Insurance Cost by Smoking Status')
axes[0, 2].set_xlabel('Smoking Status')
axes[0, 2].set_ylabel('Insurance Cost ($)')
axes[0, 2].tick_params(axis='x', rotation=45)

# By occupation
df.boxplot(column='insurance_cost', by='Occupation', ax=axes[1, 0])
axes[1, 0].set_title('Insurance Cost by Occupation')
axes[1, 0].set_xlabel('Occupation')
axes[1, 0].set_ylabel('Insurance Cost ($)')

# By exercise level
df.boxplot(column='insurance_cost', by='exercise', ax=axes[1, 1])
axes[1, 1].set_title('Insurance Cost by Exercise Level')
axes[1, 1].set_xlabel('Exercise Level')
axes[1, 1].set_ylabel('Insurance Cost ($)')

# By other coverage
df.boxplot(column='insurance_cost', by='has_other_coverage', ax=axes[1, 2])
axes[1, 2].set_title('Insurance Cost by Other Coverage')
axes[1, 2].set_xlabel('Has Other Coverage (0=No, 1=Yes)')
axes[1, 2].set_ylabel('Insurance Cost ($)')

plt.tight_layout()
plt.savefig('02_cost_by_segments.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: 02_cost_by_segments.png")
plt.close()

# 3.2 Statistical tests for cost differences
print("\n\nStatistical Testing - Insurance Cost Differences:")

# By tenure segment (ANOVA)
tenure_groups = [group['insurance_cost'].values for name, group in df.groupby('tenure_segment')]
f_stat, p_value = stats.f_oneway(*tenure_groups)
print(f"\n  Tenure segments (ANOVA):")
print(f"    F-statistic: {f_stat:.4f}, p-value: {p_value:.4f}")
print(f"    Result: {'Significant difference' if p_value < 0.05 else 'No significant difference'}")

# By other coverage (T-test)
no_other = df[df['has_other_coverage'] == 0]['insurance_cost']
has_other = df[df['has_other_coverage'] == 1]['insurance_cost']
t_stat, p_value = stats.ttest_ind(no_other, has_other)
print(f"\n  Other coverage (T-test):")
print(f"    t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
print(f"    Result: {'Significant difference' if p_value < 0.05 else 'No significant difference'}")
print(f"    Mean (no coverage): ${no_other.mean():,.2f}")
print(f"    Mean (has coverage): ${has_other.mean():,.2f}")

# ==========================================
# 4. CORRELATION ANALYSIS
# ==========================================
print("\n" + "="*70)
print("CORRELATION ANALYSIS")
print("="*70)

# Select numerical columns for correlation
corr_cols = ['age', 'bmi', 'insurance_cost', 'years_of_insurance_with_us',
             'avg_glucose_level', 'cholesterol_numeric', 'health_risk_score',
             'regular_checkup_lasy_year', 'visited_doctor_last_1_year',
             'has_other_coverage', 'ever_admitted', 'daily_avg_steps']

correlation_matrix = df[corr_cols].corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Key Variables', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('03_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: 03_correlation_heatmap.png")
plt.close()

# Print top correlations with insurance cost
cost_corr = correlation_matrix['insurance_cost'].sort_values(ascending=False)
print("\n\nTop correlations with Insurance Cost:")
print(cost_corr.head(10))

# ==========================================
# 5. CUSTOMER SEGMENT PROFILING
# ==========================================
print("\n" + "="*70)
print("CUSTOMER SEGMENT PROFILING")
print("="*70)

# 5.1 Profile by tenure segment
print("\n\n1. TENURE SEGMENT PROFILE:")
tenure_profile = df.groupby('tenure_segment').agg({
    'insurance_cost': ['mean', 'median', 'count'],
    'age': 'mean',
    'bmi': 'mean',
    'health_risk_score': 'mean',
    'regular_checkup_lasy_year': 'mean',
    'has_other_coverage': 'mean'
}).round(2)
print(tenure_profile)

# 5.2 Profile by health risk score
print("\n\n2. HEALTH RISK SCORE PROFILE:")
risk_profile = df.groupby('health_risk_score').agg({
    'insurance_cost': ['mean', 'median', 'count'],
    'age': 'mean',
    'years_of_insurance_with_us': 'mean',
    'regular_checkup_lasy_year': 'mean'
}).round(2)
print(risk_profile)

# 5.3 High-value customer analysis
print("\n\n3. HIGH-VALUE CUSTOMERS (Top 25% by cost):")
high_value_threshold = df['insurance_cost'].quantile(0.75)
high_value = df[df['insurance_cost'] >= high_value_threshold]

print(f"\nThreshold: ${high_value_threshold:,.2f}")
print(f"Count: {len(high_value):,} customers ({len(high_value)/len(df)*100:.1f}%)")
print(f"\nCharacteristics:")
print(f"  • Average age: {high_value['age'].mean():.1f} years")
print(f"  • Average tenure: {high_value['years_of_insurance_with_us'].mean():.1f} years")
print(f"  • Average BMI: {high_value['bmi'].mean():.1f}")
print(f"  • Health risk score: {high_value['health_risk_score'].mean():.2f}")
print(f"  • Regular checkup rate: {high_value['regular_checkup_lasy_year'].mean():.2f} per year")
print(f"  • Has other coverage: {high_value['has_other_coverage'].mean()*100:.1f}%")

# ==========================================
# 6. KEY INSIGHTS VISUALIZATION
# ==========================================
print("\n" + "="*70)
print("CREATING KEY INSIGHTS VISUALIZATION")
print("="*70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Key Business Insights - Customer Engagement & Risk', fontsize=16, fontweight='bold')

# 6.1 Average cost by tenure and other coverage
pivot_data = df.groupby(['tenure_segment', 'has_other_coverage'])['insurance_cost'].mean().unstack()
pivot_data.plot(kind='bar', ax=axes[0, 0], color=['steelblue', 'coral'], edgecolor='black', alpha=0.8)
axes[0, 0].set_title('Avg Insurance Cost: Tenure × Other Coverage')
axes[0, 0].set_xlabel('Tenure Segment')
axes[0, 0].set_ylabel('Average Insurance Cost ($)')
axes[0, 0].legend(['No Other Coverage', 'Has Other Coverage'])
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(axis='y', alpha=0.3)

# 6.2 Health risk vs cost
risk_cost = df.groupby('health_risk_score')['insurance_cost'].mean()
axes[0, 1].plot(risk_cost.index, risk_cost.values, marker='o', linewidth=2, markersize=8, color='darkred')
axes[0, 1].set_title('Avg Insurance Cost by Health Risk Score')
axes[0, 1].set_xlabel('Health Risk Score (0-4)')
axes[0, 1].set_ylabel('Average Insurance Cost ($)')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xticks(range(5))

# 6.3 Checkup engagement by tenure
checkup_tenure = df.groupby('tenure_segment')['regular_checkup_lasy_year'].mean()
axes[1, 0].barh(checkup_tenure.index, checkup_tenure.values, color='mediumseagreen', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('Avg Regular Checkups by Tenure Segment')
axes[1, 0].set_xlabel('Average Checkups per Year')
axes[1, 0].set_ylabel('Tenure Segment')
axes[1, 0].grid(axis='x', alpha=0.3)

# 6.4 Cost distribution by BMI and smoking
bmi_smoke_pivot = df.groupby(['bmi_category', 'smoker'])['insurance_cost'].mean().unstack()
bmi_smoke_pivot.plot(kind='bar', ax=axes[1, 1], color=['lightgreen', 'indianred'], edgecolor='black', alpha=0.8)
axes[1, 1].set_title('Avg Cost: BMI Category × Smoking Status')
axes[1, 1].set_xlabel('BMI Category')
axes[1, 1].set_ylabel('Average Insurance Cost ($)')
axes[1, 1].legend(['Non-Smoker', 'Smoker/Former'])
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('04_key_insights.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: 04_key_insights.png")
plt.close()

# ==========================================
# 7. SUMMARY REPORT
# ==========================================
print("\n" + "="*70)
print("EDA SUMMARY REPORT")
print("="*70)

print("\n\n📊 KEY FINDINGS:\n")

print("1. CUSTOMER BASE:")
print(f"   • Total customers: {len(df):,}")
print(f"   • Average tenure: {df['years_of_insurance_with_us'].mean():.1f} years")
print(f"   • {(df['has_other_coverage']==1).sum():,} ({(df['has_other_coverage']==1).mean()*100:.1f}%) have other coverage")

print("\n2. COST PATTERNS:")
print(f"   • Average cost: ${df['insurance_cost'].mean():,.2f}")
print(f"   • Cost range: ${df['insurance_cost'].min():,.0f} - ${df['insurance_cost'].max():,.0f}")
print(f"   • High-value customers (top 25%): ${high_value_threshold:,.2f}+")

print("\n3. HEALTH PROFILE:")
print(f"   • {(df['obesity']==1).sum():,} ({(df['obesity']==1).mean()*100:.1f}%) obese customers")
print(f"   • {(df['smoker']==1).sum():,} ({(df['smoker']==1).mean()*100:.1f}%) current/former smokers")
print(f"   • {(df['high_glucose']==1).sum():,} ({(df['high_glucose']==1).mean()*100:.1f}%) high glucose levels")
print(f"   • Average health risk score: {df['health_risk_score'].mean():.2f} / 4.0")

print("\n4. ENGAGEMENT:")
print(f"   • Average regular checkups: {df['regular_checkup_lasy_year'].mean():.2f} per year")
print(f"   • Average doctor visits: {df['visited_doctor_last_1_year'].mean():.2f} per year")
print(f"   • {(df['ever_admitted']==1).sum():,} ({(df['ever_admitted']==1).mean()*100:.1f}%) have been admitted")

print("\n5. RISK FACTORS:")
most_common_risk = df['health_risk_score'].mode()[0]
print(f"   • Most common risk score: {most_common_risk}")
print(f"   • Customers with 3+ risk factors: {len(df[df['health_risk_score']>=3]):,} ({len(df[df['health_risk_score']>=3])/len(df)*100:.1f}%)")

print("\n\n✓ Phase 1 EDA Complete!")
print("\nGenerated files:")
print("  1. 01_univariate_distributions.png")
print("  2. 02_cost_by_segments.png")
print("  3. 03_correlation_heatmap.png")
print("  4. 04_key_insights.png")
print("\nNext: Proceed to Phase 2 - Customer Segmentation & Retention Analysis")
