# Phase 1: Data Preparation & Exploratory Analysis
## Customer Lifetime Value Optimization Through Proactive Health Engagement

**Project:** CX Data Analyst Portfolio - Insurance Industry  
**Author:** Rodion Barskov 
**Date:** December 2025 - TBD  
**Status:** ✅ Phase 1 Complete

[🔝 Back to Top](#phase-1-complete-data-preparation-exploratory-analysis)

---

## 📑 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [Dataset Overview](#-dataset-overview)
3. [Data Cleaning Actions](#-data-cleaning-actions)
4. [Key Findings from EDA](#-key-findings-from-eda)
5. [Business Insights for CX Strategy](#-business-insights-for-cx-strategy)
6. [Deliverables](#-deliverables)
7. [Data Quality Scorecard](#-data-quality-scorecard)
8. [Technical Skills Demonstrated](#-technical-skills-demonstrated)
9. [Next Steps: Phase 2](#-next-steps-phase-2)
10. [Portfolio Notes](#-portfolio-notes)

---

## 📋 Executive Summary

[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

Phase 1 successfully completed data cleaning, feature engineering, and comprehensive exploratory data analysis on 25,000 insurance policyholders. The cleaned dataset now contains 35 features (11 newly engineered) and is ready for advanced analytics in Phase 2.

**Key Deliverables:**
✅ Cleaned dataset (insurance_data_clean.csv)
✅ Data dictionary and cleaning log
✅ 4 comprehensive visualization sets
✅ Statistical analysis and insights
✅ Customer segment profiles

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 🎯 Dataset Overview

**Original Data:**
- 25,000 customers (policyholders)
- 24 features
- 990 missing BMI values (3.96%)
- 11,881 missing Year_last_admitted (47.52% - intentional)
- 0 duplicates
- 1 typo corrected (Occupation: "Salried" → "Salaried")

**Cleaned Data:**
- 25,000 customers (no rows removed)
- 35 features (11 engineered features added)
- BMI imputed using gender/age-stratified median
- All categorical variables standardized
- Ready for modeling and analysis

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 🛠️ Data Cleaning Actions

### 1. **Missing Value Treatment**
| Feature | Missing | Strategy |
|---------|---------|----------|
| BMI | 990 (3.96%) | Imputed with median by Gender × Age Group |
| Year_last_admitted | 11,881 (47.52%) | Retained (indicates "never admitted" - valuable info) |

### 2. **Data Standardization**
- Fixed typo: "Salried" → "Salaried" (4,811 records)
- Created binary flag: `has_other_coverage` (N→0, Y→1)
- Created numeric cholesterol from ranges (e.g., "150 to 175" → 162.5)
- Created binary flag: `ever_admitted` from Year_last_admitted

### 3. **Feature Engineering**
Created 11 new features to support CX analysis:

**Segmentation Features:**
- `tenure_segment`: New (0-2yr), Established (3-5yr), Loyal (6-8yr)
- `age_group`: 18-30, 31-45, 46-60, 60+
- `bmi_category`: Underweight, Normal, Overweight, Obese (WHO standards)

**Health Risk Indicators:**
- `high_cholesterol`: ≥200 mg/dL (binary)
- `high_glucose`: ≥140 mg/dL (binary)
- `obesity`: BMI ≥30 (binary)
- `smoker`: Current or former smoker (binary)
- `health_risk_score`: Composite 0-4 scale (sum of 4 risk flags)

**Customer Behavior:**
- `cholesterol_numeric`: Numeric midpoint of ranges
- `ever_admitted`: Hospital admission history (binary)
- `has_other_coverage`: Dual insurance indicator (binary)

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 📊 Key Findings from EDA

### 1. Customer Base Characteristics

**Demographics:**
- Average age: 44.9 years
- Gender: 65.7% Male, 34.3% Female
- Average BMI: 31.4 (Obese category)
- Occupation: 40.7% Student, 40.1% Business, 19.2% Salaried

**Customer Tenure:**
- Average: 4.1 years
- New (0-2yr): 7,576 customers (30.3%)
- Established (3-5yr): 8,777 customers (35.1%)
- Loyal (6-8yr): 8,647 customers (34.6%)

**Competitive Landscape:**
- 30.3% (7,582) have other insurance coverage
- Dual coverage customers pay **$3,167 more** on average ($29,354 vs $26,187)
- **Significant finding:** Dual coverage is a strong predictor of cost (p < 0.001)

---

### 2. Insurance Cost Analysis

**Cost Distribution:**
- Mean: $27,147
- Median: $27,148
- Range: $2,468 - $67,870
- High-value customers (top 25%): ≥$37,020

**Cost Drivers (Statistical Testing):**
- ✅ **Has Other Coverage**: Significant difference (t=-16.15, p<0.001)
  - No coverage: $26,187
  - Has coverage: $29,354
- ⚠️ **Tenure**: No significant difference (F=2.59, p=0.075)
- **Top correlations with cost:**
  1. Ever admitted (r=0.16)
  2. Has other coverage (r=0.10)
  3. Health risk factors: Very weak correlation (surprising!)

**Key Insight:** Health risk scores show minimal correlation with current insurance costs (-0.007), suggesting potential pricing inefficiencies or cross-subsidization.

---

## ⚠️ **Data Quality Limitation - Mock Dataset**

**⚠️ IMPORTANT:** This mock dataset exhibits unrealistic patterns where health risk factors show minimal to inverse correlation with insurance costs (r ≈ -0.007). In real-world insurance data, smokers, obese customers, and those with multiple risk factors would pay significantly higher premiums due to actuarial pricing.

**Impact on Analysis:**
- Cost prediction models show weak health risk signals
- Segment profiling shows similar costs across risk levels  
- Business insights demonstrate analytical methodology rather than real pricing recommendations

This limitation is acknowledged and demonstrates critical data quality assessment skills.

---

### 3. Health Profile & Risk

**Prevalence of Risk Factors:**
- 62.8% (15,710) have high glucose (≥140)
- 54.3% (13,578) are obese (BMI ≥30)
- 32.8% (8,196) are current/former smokers
- 20.1% (5,017) have high cholesterol (≥200)

**Health Risk Score Distribution:**
- Score 0 (no risk factors): 9.8% (2,457)
- Score 1: 33.3% (8,333)
- Score 2: 36.4% (9,097) ← Most common
- Score 3: 17.9% (4,478)
- Score 4 (all risk factors): 2.5% (635)

**Critical Finding:** 20.5% of customers have 3-4 risk factors but show similar costs to healthier customers, indicating opportunity for risk-based pricing or preventive interventions.

**⚠️ Data Quality Note:** The inverse relationship observed (higher risk = lower cost for group 4) is unrealistic and indicates synthetic data generation without proper business logic. Real insurance pricing would show a strong positive correlation between risk factors and premiums.

---

### 4. Customer Engagement Patterns

**Healthcare Utilization:**
- Average regular checkups: 0.77 per year (LOW!)
- Average doctor visits: 3.10 per year
- 52.5% (13,119) have hospital admission history

**Engagement by Tenure:**
- New customers (0-2yr): 0.62 checkups/year
- Established (3-5yr): 0.85 checkups/year
- Loyal (6-8yr): 0.82 checkups/year

**Key Insight:** Regular preventive checkups are LOW across all segments, representing a major opportunity for health engagement programs.

**Dual Coverage Impact:**
- Customers with other insurance: 39% of established/loyal segments
- Only 9% of new customers have dual coverage
- Suggests competitive shopping in early years

---

### 5. High-Value Customer Profile (Top 25%)

**Characteristics:**
- Threshold: $37,020+ annual premium
- Count: 6,677 customers (26.7%)
- Average age: 45.1 years (similar to overall)
- Average tenure: 4.1 years (similar to overall)
- Health risk score: 1.70 (same as overall - UNEXPECTED!)
- Has other coverage: 37.4% (vs 30.3% overall)

**Strategic Implication:** High-value customers are NOT significantly unhealthier, suggesting value is driven by coverage levels, not risk. Dual coverage holders are overrepresented in high-value segment.

---

## 📈 Statistical Validation

### Hypothesis Testing Results

**T-Test: Insurance Cost by Other Coverage**
- Null Hypothesis: No difference in cost between dual coverage vs. exclusive customers
- Result: **REJECTED** (t=-16.15, p<0.001)
- Dual coverage customers pay significantly more

**ANOVA: Insurance Cost by Tenure Segment**
- Null Hypothesis: No difference in cost across tenure groups
- Result: **Failed to reject** (F=2.59, p=0.075)
- No significant cost differences by tenure (marginally significant at α=0.10)

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 💡 Business Insights for CX Strategy

### 🎯 Opportunity 1: **Preventive Care Engagement Gap**
**Finding:** Only 0.77 average annual checkups across all customers  
**Impact:** Low preventive care → Higher reactive medical costs  
**CX Action:** Wellness incentive program (see Phase 5 simulation)

### 🎯 Opportunity 2: **Competitive Retention Risk**
**Finding:** 30.3% have dual coverage, paying $3,167 more annually  
**Impact:** Price-sensitive customers at churn risk  
**CX Action:** Exclusive customer benefits, competitive pricing analysis

### 🎯 Opportunity 3: **New Customer Activation**
**Finding:** New customers (30.3% of base) have lowest checkup rates (0.62/year)  
**Impact:** Missing critical engagement window  
**CX Action:** Onboarding wellness programs, early health screenings

### 🎯 Opportunity 4: **Risk-Based Personalization**
**Finding:** 20.5% have 3-4 risk factors but no targeted interventions  
**Impact:** Missed prevention opportunities, future claim costs  
**CX Action:** Risk-stratified health coaching, personalized wellness plans

### 🎯 Opportunity 5: **High-Value Customer Retention**
**Finding:** High-value customers don't differ significantly in health but have higher dual coverage  
**Impact:** Premium customers may be getting better competing offers  
**CX Action:** VIP services, premium benefits, price justification

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 📁 Deliverables

### Files Generated

**Data Files:**
1. `insurance_data_clean.csv` - Cleaned dataset (3.9 MB)
2. `data_dictionary.csv` - Column metadata
3. `data_cleaning_log.txt` - Audit trail

**Code:**
4. `01_data_cleaning.py` - Reproducible cleaning script
5. `02_eda.py` - Full EDA analysis script

**Visualizations:**
6. `01_univariate_distributions.png` - Distribution analysis (9 plots)
7. `02_cost_by_segments.png` - Cost by customer segments (6 plots)
8. `03_correlation_heatmap.png` - Feature correlation matrix
9. `04_key_insights.png` - Key business insights (4 plots)

---

## 🔍 Data Quality Scorecard

| Metric | Score | Status |
|--------|-------|--------|
| Completeness | 98.4% | ✅ Excellent |
| Accuracy | 100% | ✅ Validated |
| Consistency | 100% | ✅ Standardized |
| Duplicates | 0% | ✅ None found |
| Outliers Handled | Yes | ✅ Documented |
| Feature Engineering | 11 new features | ✅ Complete |
| Documentation | Full audit trail | ✅ Complete |

**Overall Data Quality: A+ (Ready for modeling)**

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 📊 Technical Skills Demonstrated

### ✅ Data Wrangling
- Missing value imputation (stratified median)
- Categorical encoding
- Feature engineering (11 new features)
- Data type conversions
- Text standardization

### ✅ Statistical Analysis
- Descriptive statistics
- Hypothesis testing (t-test, ANOVA)
- Correlation analysis
- Distribution analysis
- Outlier detection

### ✅ Visualization
- Univariate distributions (histograms, bar charts)
- Bivariate analysis (box plots, scatter plots)
- Correlation heatmaps
- Segment comparisons
- Business insights dashboards

### ✅ Business Analytics
- Customer segmentation
- Risk profiling
- Competitive analysis
- High-value customer identification
- Actionable insights generation

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 🚀 Next Steps: Phase 2

**Focus:** Customer Segmentation & Retention Analysis

**Planned Activities:**
1. Build churn risk prediction model
2. Calculate Customer Lifetime Value (CLV)
3. Advanced customer segmentation (K-means clustering)
4. Retention strategy recommendations
5. Segment-specific CX interventions

**Timeline:** 8-10 hours

**Expected Outputs:**
- Churn risk scores for all customers
- CLV estimates by segment
- Predictive model (Logistic Regression / Random Forest)
- Feature importance analysis
- Retention playbook by segment

---

## 📝 Portfolio Notes

### What Makes This Strong for CX Roles

**1. Business-First Approach:**
- Started with business questions, not just technical exploration
- Every finding tied to actionable CX strategy
- Framed insights in terms of customer value and retention

**2. Industry Relevance:**
- Addressed real insurance CX challenges (retention, wellness, competition)
- Used domain knowledge (BMI categories, health metrics)
- Positioned analysis for insurance decision-makers

**3. Statistical Rigor:**
- Hypothesis testing with proper interpretation
- Validated assumptions
- Acknowledged limitations (weak health-cost correlation)

**4. Communication Skills:**
- Clear documentation
- Visual storytelling
- Executive-friendly summaries
- Technical depth when needed

**5. End-to-End Workflow:**
- From raw data → cleaned data → insights → recommendations
- Reproducible code
- Audit trail maintained

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## 🎓 Lessons Learned

**Surprising Findings:**
1. Health risk has minimal correlation with current costs (suggests pricing opportunities)
2. Tenure doesn't significantly affect costs (contrary to typical expectation)
3. Dual coverage is a stronger cost predictor than health metrics

**Technical Challenges:**
1. BMI missing values required thoughtful imputation strategy
2. Year_last_admitted required understanding "missingness as information"
3. Balancing feature creation with model complexity

**Skills Reinforced:**
- Importance of domain context in feature engineering
- Power of visual EDA in uncovering patterns
- Value of statistical testing to validate intuitions

---


[🔝 Back to Top](#phase-1-complete-data-preparation--exploratory-analysis)

## ✅ Phase 1 Checklist

- [x] Data loaded and inspected
- [x] Missing values handled appropriately
- [x] Data quality validated
- [x] Categorical variables standardized
- [x] 11 engineered features created
- [x] Comprehensive EDA completed
- [x] Statistical testing performed
- [x] 4 visualization sets created
- [x] Customer segments profiled
- [x] Business insights documented
- [x] Code documented and reproducible
- [x] Files organized and exported
- [x] Summary report completed


---

*This analysis was conducted as part of a portfolio project for CX Data Analyst roles in the insurance industry. All analysis is based on publicly available Kaggle mock data.*
