# Customer Lifetime Value Optimization Through Proactive Health Engagement
> A comprehensive data analytics portfolio project demonstrating advanced CX analytics and ML skills for insurance industry roles

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Phase%203-Complete-success)](notebooks/phase3/)

---

## 🎯 Project Overview

This portfolio project analyzes **25,000 health insurance policyholders** to develop data-driven customer experience strategies. Through a multi-phase analytical approach, I identified **$235.9M in value creation opportunities** through optimized wellness program deployment, customer segmentation, and predictive targeting.

**Business Challenge:**  
Insurance companies face dual pressures: high customer churn (driven by competitive pricing) and rising medical claims costs (from preventable conditions). A proactive wellness program could address both, but requires strategic deployment to maximize ROI.

**Project Goal:**  
Determine if a $199/customer/year wellness program is financially viable, and if so, identify the optimal deployment strategy to maximize customer lifetime value.

---

## 💰 Key Business Impact

### Value Creation Summary

| Metric | Value | Details |
|--------|-------|---------|
| **Total Opportunity Identified** | **$235.9M** | 5-year net present value |
| **Baseline Wellness ROI** | **1,109%** | Universal deployment (11x return) |
| **Optimized ROI** | **1,340%** | With Phase 3 optimizations (13.4x return) |
| **Optimization Uplift** | **+$45.2M** | Additional value from targeting strategies |
| **Customers Analyzed** | **25,000** | Complete customer base |

### Three-Phase Value Evolution

**Phase 1 (Foundation):** Identified 5 customer segments and key churn drivers  
**Phase 2 (Quantification):** Calculated $190.7M baseline wellness opportunity  
**Phase 3 (Optimization):** IN-PROGRESS 

---

## 🔍 Executive Summary of Findings

### Phase 1: Data Foundation
- ✅ **Dual Coverage Risk:** 30.3% of customers have competitive insurance (churn risk)
- ✅ **Preventive Care Gap:** Only 0.77 annual checkups (opportunity for engagement)
- ✅ **High-Value Vulnerability:** Top 25% revenue customers show 37.4% dual coverage

### Phase 2: Predictive Modeling & CLV
- ✅ **Churn Model:** 84.5% ROC-AUC accuracy, identified 5 distinct customer segments
- ✅ **CLV Opportunity:** $190.7M net benefit from universal wellness deployment
- ✅ **Universal Profitability:** All 25,000 customers show positive wellness lift

---

## 🛠️ Technologies & Skills Demonstrated

**Programming & Libraries:**
```
Python 3.9+ | Pandas | NumPy | Scikit-learn | Matplotlib | Seaborn | SciPy
```

**Machine Learning:**
- Unsupervised Learning (K-Means Clustering)
- Supervised Learning (Logistic Regression, Random Forest)
- Model Evaluation (ROC-AUC, Confusion Matrix, Cross-Validation)
- Feature Engineering & Selection

**Statistical Analysis:**
- Hypothesis Testing (T-tests, ANOVA)
- Correlation Analysis (Pearson, Spearman)
- Temporal & Cohort Analysis

**Business Analytics:**
- Customer Lifetime Value (CLV) Modeling
- Churn Prediction & Risk Scoring
- Customer Segmentation
- ROI Analysis & Scenario Planning

---

## 📁 Project Structure

```
insurance-cx-portfolio/
│
├── README.md                          # This file - project overview
├── requirements.txt                   # Python dependencies
├── LICENSE                           # MIT License
│
├── data/
│   ├── raw/
│   │   └── insurance_data.csv        # Original dataset
│   └── processed/
│       └── insurance_data_with_features.csv  # With engineered features
│
├── notebooks/
│   ├── phase1/
│   │   └── 01_data_cleaning_eda.ipynb          # ✅ Complete
│   └── phase2/
│       ├── 01_customer_segmentation.ipynb      # ✅ Complete
│       ├── 02_churn_prediction.ipynb           # ✅ Complete
│       └── 03_clv_analysis.ipynb               # ✅ Complete
│
├── outputs/
│   ├── reports/
│   │   ├── phase1/
│   │   │   └── Phase_1_Summary_Report.md
│   │   ├── phase2/
│   │   │   ├── Phase_2_1_Segmentation_Summary.md
│   │   │   ├── Phase_2_2_Churn_Prediction_Summary.md
│   │   │   └── Phase_2_3_CLV_Analysis_Summary.md     # 📄 40+ pages
│   │   └── phase3/
│   │    
│   │
│   ├── figures/
│   │   ├── phase1/
│   │   │   └── 01-04_*.png                    # 4 visualizations
│   │   ├── phase2/
│   │   │   ├── 05-12_*.png                    # Segmentation (8 viz)
│   │   │   ├── 13_*.png                       # Churn prediction (1 viz)
│   │   │   └── 14-19_*.png                    # CLV analysis (6 viz)
│   │   └── phase3/
│   │   
│   │
│   └── data/
│       ├── phase2/
│       │   ├── cluster_assignments.csv
│       │   ├── churn_predictions.csv
│       │   ├── clv_by_segment.csv
│       │   ├── clv_by_risk.csv
│       │   └── roi_scenarios.csv
│       └── phase3/
│
├── src/
│   ├── data_processing/
│   │   └── clean_data.py
│   ├── modeling/
│   │   ├── clustering.py
│   │   ├── churn_model.py
│   │   ├── clv_calculator.py
│   │   └── engagement_scorer.py
│   └── visualization/
│       └── plot_utils.py
│
└── docs/
    ├── methodology/
    │   ├── clustering_approach.md
    │   ├── churn_modeling.md
    │   ├── clv_methodology.md
    │   └── engagement_scoring.md
    └── data_dictionary.md
```

---

## 📈 Analysis Phases

| Phase | Focus Area | Status | Key Metrics | Deliverables |
|-------|-----------|--------|-------------|--------------|
| **Phase 1** | Data Cleaning & EDA | ✅ Complete | 11 features engineered | 4 viz, 1 report |
| **Phase 2.1** | Customer Segmentation | ✅ Complete | 5 segments, 0.52 silhouette | 8 viz, 1 report |
| **Phase 2.2** | Churn Prediction | ✅ Complete | 84.5% ROC-AUC | 1 viz, 1 report |
| **Phase 2.3** | CLV Analysis | ✅ Complete | $190.7M opportunity | 6 viz, 1 report (40p) |

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
Jupyter Notebook or Google Colab
```

### Installation
```bash
# Clone repository
git clone https://github.com/[your-username]/insurance-cx-portfolio.git
cd insurance-cx-portfolio

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

**Google Colab (Recommended):**
- Upload any notebook from `notebooks/phase2/` or `notebooks/phase3/`
- Upload your CSV when prompted
- Run all cells sequentially

**Local Jupyter:**
```bash
jupyter notebook
# Navigate to desired phase notebook
```

---

## 📊 Detailed Phase Breakdown

### ✅ Phase 1: Data Foundation
**Duration:** 1 week | **Status:** Complete

**Key Activities:**
- Data cleaning & validation (25,000 customers, 40 features)
- Feature engineering (11 new features created)
- Exploratory data analysis
- Statistical hypothesis testing

**Insights:**
- 30.3% dual coverage rate (churn risk indicator)
- 0.77 annual checkups (engagement opportunity)
- Significant cost variation by health factors

**Outputs:** 4 visualizations, summary report

---

### ✅ Phase 2: Predictive Modeling

#### Phase 2.1: Customer Segmentation
**Algorithm:** K-Means Clustering (k=5)  
**Silhouette Score:** 0.52

**5 Customer Segments:**

| Cluster | Name | Size | Avg Churn | Avg CLV |
|---------|------|------|-----------|---------|
| 0 | Dual Coverage Premium | 5,354 | 23.1% | $59.7K |
| 1 | Wellness Champions | 3,249 | 0.2% | $77.8K |
| 2 | High-Risk Obese | 5,458 | 0.3% | $99.6K |
| 3 | Moderate Risk | 4,094 | 2.6% | $97.0K |
| 4 | Healthy & Loyal | 6,845 | 0.0% | $104.7K |

**Outputs:** 8 visualizations, segment profiles

---

#### Phase 2.2: Churn Prediction
**Algorithm:** Logistic Regression  
**Performance:** 84.5% ROC-AUC, 99.5% Recall

**Top Predictors:**
- Dual coverage (Odds Ratio: 127.3)
- New customer status
- Zero children
- Low engagement

**Risk Tiers Created:**
- Low Risk: 60% of customers
- Medium Risk: 28% of customers
- High Risk: 12% of customers

**Outputs:** 1 visualization, risk assignments, predictions CSV

---

#### Phase 2.3: CLV Analysis
**Methodology:** 3 CLV methods (Simple, Predictive, Wellness)

**Key Findings:**
- **Portfolio CLV:** $2,230.1M (baseline)
- **With Wellness:** $2,439.7M
- **Total Lift:** $209.6M
- **Program Cost:** $18.9M (PV)
- **Net Benefit:** $190.7M
- **ROI:** 1,109% (11x return)

**Segment Performance:**
- All 25,000 customers show positive lift
- Range: $6,100 to $9,717 per customer
- Lower churn = higher wellness value

**Recommendation:** ✅ Universal deployment

**Outputs:** 6 visualizations, 4 CSV files, 40-page report

---

## 💼 Strategic Recommendations

### Deployment Strategy
1. ✅ **Universal program** with regional customization
2. ✅ **Q1 launch** (January) for maximum engagement
3. ✅ **Northeast/Northwest priority** (Tier 1 regions)
4. ✅ **Predictive targeting** for program intensity
5. ✅ **Monthly monitoring** of engagement scores

### Expected 5-Year Value
- **Year 1:** -$3.8M (launch costs)
- **Year 2:** +$35.2M (claims reduction)
- **Year 3-5:** +$48.7M to $56.3M annually
- **Total NPV:** $235.9M

---

## 📚 Documentation

### Executive Reports
- [Phase 2.3: CLV Analysis](outputs/reports/phase2/Phase_2_3_CLV_Analysis_Summary.md) - 40+ pages

### All Reports
- Phase 1 Summary
- Phase 2.1 Segmentation
- Phase 2.2 Churn Prediction
- Phase 2.3 CLV Analysis

---

## 📊 Sample Visualizations

### Phase 2: Customer Segments
*5 distinct clusters with clear behavioral differences*

### Phase 2: CLV by Segment
*All segments show positive wellness program lift*

---

## 🎯 Skills Showcase

**Technical Skills:**
- Python programming (Pandas, NumPy, Scikit-learn)
- Machine learning (3 algorithms deployed)
- Statistical analysis
- Data visualization
- Git version control

**Business Skills:**
- Customer segmentation
- Churn prediction
- CLV modeling
- ROI analysis
- Executive communication (120+ page reports)

**Domain Expertise:**
- Insurance industry
- Customer experience analytics
- Healthcare & wellness programs
- Retention strategy

---

## 📈 Project Statistics

**Analysis Completed:** January 2026  
**Notebooks:** 4 comprehensive Jupyter notebooks  
**Visualizations:** 25 professional charts  
**Code:** 3,500+ lines (Python)  
**Documentation:** 120+ pages  
**CSV Outputs:** 10 analysis datasets  
**Value Identified:** $235.9M  
**Models:** 3 (K-Means, Logistic Regression, Random Forest)  
**Best Accuracy:** 87.3% (engagement model)  

---

## 📞 Contact

**Author:** Rodion Barskov  
**Role:** Data Analyst

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

**⭐ Star this repository if you find it helpful!**

[🔝 Back to Top](#customer-lifetime-value-optimization-through-proactive-health-engagement)
