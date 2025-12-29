# Customer Lifetime Value Optimization Through Proactive Health Engagement
## CX Data Analyst Portfolio Project - Insurance Industry

---

## 📋 PROJECT OVERVIEW

**Business Problem**: Insurance companies face high customer acquisition costs and increasing competition. Retaining existing customers while promoting preventive health behaviors can simultaneously reduce churn and lower claim costs.

**Analysis Goal**: Identify actionable strategies to improve customer lifetime value through targeted health engagement programs, with specific focus on retention drivers and wellness incentives.

**Key Questions**:
1. What factors drive customer retention and long-term value?
2. How does health engagement correlate with customer loyalty and costs?
3. Which customer segments are at highest risk of churn?
4. What is the potential ROI of wellness incentive programs?
5. Where should we focus geographic expansion or retention efforts?

---

## 🗺️ PROJECT STRUCTURE

### **Phase 1: Data Preparation & Exploration**
### **Phase 2: Customer Segmentation & Retention Analysis**
### **Phase 3: Health Engagement Scoring System**
### **Phase 4: Geospatial & Temporal Analysis**
### **Phase 5: A/B Test Simulation & ROI Modeling**
### **Phase 6: Dashboard & Recommendations**

---

## 📊 PHASE 1: DATA PREPARATION & EXPLORATION

### 1.1 Data Cleaning
**Tasks**:
- Handle missing values (BMI: 990 missing, Year_last_admitted: 11,881 missing)
- Standardize categorical variables (occupation typo: "Salried" → "Salaried")
- Create data dictionary documenting each feature
- Validate data ranges (age, BMI, insurance_cost)

**Deliverables**:
- Clean dataset saved as `insurance_clean.csv`
- Data quality report (% missing, outliers identified)
- Cleaning script with comments

### 1.2 Exploratory Data Analysis (EDA)
**Tasks**:
- Univariate analysis: Distribution of key variables
- Bivariate analysis: Insurance cost vs. health metrics
- Correlation matrix: Identify multicollinearity
- Outlier detection: Flag anomalous insurance costs

**Visualizations**:
- Distribution plots (age, BMI, insurance cost)
- Box plots by categorical variables (occupation, gender, location)
- Correlation heatmap
- Cost distribution by tenure

**Skills Showcased**: Data cleaning, pandas, visualization (matplotlib/seaborn)

---

## 👥 PHASE 2: CUSTOMER SEGMENTATION & RETENTION ANALYSIS

### 2.1 Customer Tenure Segmentation
**Create 3 cohorts**:
- **New Customers** (0-2 years): Churn risk, acquisition focus
- **Established Customers** (3-5 years): Growth opportunities
- **Loyal Customers** (6-8 years): Retention champions

**Analysis**:
- Demographic profile of each cohort
- Average insurance cost by cohort
- Health engagement levels by cohort
- Dual coverage rate by cohort (competitive threat indicator)

### 2.2 Churn Risk Scoring
**Build a churn risk model**:
- **Target variable**: Create "At-Risk" flag (0-1 year tenure + dual coverage OR 0-2 years with low engagement)
- **Features**: Health engagement, demographics, cost, lifestyle
- **Models to test**: 
  - Logistic Regression (interpretability)
  - Decision Tree (rule-based insights)
  - Random Forest (accuracy benchmark)

**Deliverables**:
- Feature importance plot
- Confusion matrix & ROC curve
- Top 10 churn risk factors
- Customer churn risk scores (exportable list)

### 2.3 Customer Lifetime Value (CLV) Estimation
**Simplified CLV formula**:
```
CLV = (Avg Annual Premium × Avg Tenure) - (Avg Claims Cost*)
*Use insurance_cost as proxy for claims/risk
```

**Segmentation**:
- High CLV vs. Low CLV customers
- Characteristics of each group
- Actionable insights for retention

**Skills Showcased**: Predictive modeling, classification, business metrics

---

## 💪 PHASE 3: HEALTH ENGAGEMENT SCORING SYSTEM

### 3.1 Create Health Engagement Score (0-100)
**Components** (weighted):
- **Regular checkups** (30%): 0-5 scale → 0-30 points
- **Exercise frequency** (25%): None=0, Moderate=15, Extreme=25
- **Smoking status** (25%): Smokes=0, Unknown=10, Formerly=15, Never=25
- **Alcohol consumption** (10%): Daily=0, Rare=5, No=10
- **Doctor visits** (10%): Normalized 0-10 scale (fewer = better, preventive care)

**Formula example**:
```python
engagement_score = (
    (regular_checkup * 6) +
    (exercise_points) +
    (smoking_points) +
    (alcohol_points) +
    (doctor_visit_normalized)
)
```

### 3.2 Engagement Analysis
**Tasks**:
- Distribute customers into 4 tiers: Low (0-25), Medium (26-50), High (51-75), Elite (76-100)
- Analyze insurance cost by engagement tier
- Identify "high-risk, low-engagement" customers (high BMI/cholesterol + low score)
- Compare engagement scores across tenure cohorts

**Visualizations**:
- Engagement score distribution
- Scatter plot: Engagement Score vs. Insurance Cost
- Box plot: Engagement by tenure cohort
- Heatmap: Engagement score by demographic segments

### 3.3 Persona Development
**Create 4-5 customer personas**:
1. **Health Champion**: Elite engagement, long tenure, lower costs
2. **Prevention Avoider**: Low engagement, high costs, moderate tenure
3. **New & Uncertain**: New customer, mid engagement, exploring options
4. **High-Risk Engaged**: Health issues but proactive (regular checkups despite high costs)
5. **Loyal but Declining**: Long tenure but engagement dropping

**For each persona**:
- Size of segment
- Average metrics (age, cost, tenure, engagement)
- CX pain points
- Recommended interventions

**Skills Showcased**: Feature engineering, scoring models, persona development, storytelling

---

## 🗺️ PHASE 4: GEOSPATIAL & TEMPORAL ANALYSIS

### 4.1 Geospatial Heatmap
**Insurance Penetration by City**:
- Customer count by location (15 cities in dataset)
- Average insurance cost by city
- Engagement score distribution by city
- Dual coverage rate by city (competitive pressure indicator)

**Visualizations**:
- Choropleth map (if you can map city to state/region)
- Bar chart: Top 5 cities by customer count
- Scatter plot: City-level cost vs. engagement
- Competitive threat map: Cities with highest dual coverage rates

**Business Insights**:
- Which markets are saturated vs. growth opportunities?
- Where to focus retention efforts?
- Geographic pricing variations

### 4.2 Temporal Analysis: Engagement Trends Over Tenure
**Analysis**:
- Average engagement score by years_of_insurance
- Track how engagement changes over customer lifecycle
- Identify critical drop-off points (e.g., year 2-3?)

**Visualizations**:
- Line chart: Avg engagement score by tenure year
- Stacked area chart: Engagement tier distribution by tenure
- Trend analysis: Is engagement improving or declining over time?

**Hypothesis Testing**:
- T-test: Do loyal customers (6-8 years) have significantly higher engagement than new customers (0-2 years)?
- ANOVA: Is there a significant difference in engagement across tenure groups?

**Skills Showcased**: Geospatial analysis, time series, hypothesis testing, statistical rigor

---

## 🧪 PHASE 5: A/B TEST SIMULATION & ROI MODELING

### 5.1 A/B Test Simulation Setup
**Hypothesis**: Offering a 10% premium discount for regular checkups will:
- Increase checkup participation by 25-30%
- Improve engagement scores
- Reduce long-term costs (preventive care)
- Increase customer retention

**Simulation Approach**:
1. **Control Group**: Current behavior (randomly select 50% of customers)
2. **Treatment Group**: Simulate 25% increase in regular checkup participation
   - Recalculate engagement scores
   - Apply 10% discount to insurance_cost

### 5.2 Impact Analysis
**Metrics to calculate**:

**Customer Engagement**:
- % increase in average engagement score
- Number of additional customers moving to "High/Elite" engagement tiers

**Financial Impact**:
- **Cost**: Total discount given (10% × premium × treatment group size)
- **Benefit**: 
  - Retained customers (estimate 5-10% churn reduction in treatment group)
  - Potential claims cost reduction (proxy: lower insurance_cost for engaged customers)
  - Lifetime value increase

**ROI Formula**:
```
ROI = (Benefits - Costs) / Costs × 100%

Benefits = (Churn Reduction Value) + (Claims Cost Savings)
Costs = Premium Discounts Given
```

### 5.3 Scenario Analysis
**Create 3 scenarios**:
1. **Conservative**: 15% checkup increase, 3% churn reduction
2. **Expected**: 25% checkup increase, 5% churn reduction
3. **Optimistic**: 35% checkup increase, 8% churn reduction

**Deliverables**:
- Simulation results table (control vs. treatment comparison)
- ROI calculation by scenario
- Break-even analysis: At what participation rate does the program become profitable?
- Sensitivity analysis: How does ROI change with different assumptions?

**Visualizations**:
- Before/after engagement distribution
- Waterfall chart: ROI breakdown
- Scenario comparison bar chart

**Skills Showcased**: A/B testing, simulation, financial modeling, ROI analysis, business case development

---

## 📊 PHASE 6: DASHBOARD & STRATEGIC RECOMMENDATIONS

### 6.1 Interactive Dashboard (Choose: Tableau, Power BI, or Python Plotly/Streamlit)

**Dashboard Structure**:

**Page 1: Executive Summary**
- KPI cards: Total customers, avg CLV, churn risk %, engagement score avg
- Customer distribution by tenure cohort
- Top 3 insights (callout boxes)

**Page 2: Retention & Segmentation**
- Tenure cohort comparison table
- Churn risk distribution
- CLV by segment
- Filter by: Location, Occupation, Gender

**Page 3: Health Engagement**
- Engagement score distribution
- Engagement vs. Insurance Cost scatter
- Persona breakdown (pie/bar chart)
- Top/bottom 10 customers by engagement

**Page 4: Geographic Insights**
- Map: Insurance penetration by city
- City-level metrics table
- Competitive pressure indicators

**Page 5: Wellness Program ROI**
- A/B test results
- Scenario comparison
- ROI projections
- Implementation roadmap

### 6.2 Strategic Recommendations Document

**Structure**:
1. **Executive Summary** (1 page)
   - Business problem
   - Key findings
   - Recommended actions
   - Expected impact

2. **Customer Retention Strategy**
   - At-risk segment size and characteristics
   - Retention tactics by cohort
   - Predictive model insights

3. **Health Engagement Program**
   - Engagement scoring methodology
   - Persona-based communication strategies
   - Wellness incentive design

4. **Geographic Expansion & Competitive Defense**
   - High-growth markets
   - Competitive threat zones
   - Market-specific tactics

5. **Wellness Discount Program**
   - Program design
   - Financial projections (ROI)
   - Implementation plan
   - Success metrics

6. **Next Steps & Roadmap**
   - Quick wins (0-3 months)
   - Medium-term initiatives (3-6 months)
   - Long-term strategy (6-12 months)

**Skills Showcased**: Data visualization, dashboard design, business communication, strategic thinking

---

## 🛠️ TECHNICAL STACK RECOMMENDATIONS

### **Tools & Libraries**:
- **Data Analysis**: Python (pandas, numpy)
- **Visualization**: matplotlib, seaborn, plotly
- **Machine Learning**: scikit-learn
- **Dashboard**: 
  - Option A: Tableau Public (most common in CX roles)
  - Option B: Power BI
  - Option C: Streamlit/Plotly Dash (shows coding skills)
- **Version Control**: Git/GitHub
- **Documentation**: Jupyter Notebook + Markdown

### **Project Structure on GitHub**:
```
insurance-cx-analysis/
│
├── README.md                          # Project overview & key findings
├── requirements.txt                   # Python dependencies
│
├── data/
│   ├── raw/                          # Original Kaggle dataset
│   ├── processed/                    # Cleaned data
│   └── data_dictionary.md
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_segmentation_retention.ipynb
│   ├── 04_engagement_scoring.ipynb
│   ├── 05_geospatial_temporal.ipynb
│   ├── 06_ab_test_simulation.ipynb
│   └── 07_final_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py              # Reusable functions
│   ├── feature_engineering.py
│   ├── modeling.py
│   └── visualization.py
│
├── reports/
│   ├── figures/                      # All visualizations
│   ├── strategic_recommendations.pdf
│   └── technical_report.pdf
│
└── dashboard/
    └── tableau_workbook.twbx         # Or Streamlit app files
```

---

## 📈 SUCCESS METRICS FOR YOUR PORTFOLIO

**What hiring managers will look for**:
✅ **Clear business problem framing** (not just "I analyzed data")
✅ **End-to-end workflow** (from raw data to recommendations)
✅ **Multiple analysis techniques** (descriptive, predictive, prescriptive)
✅ **Statistical rigor** (hypothesis testing, model validation)
✅ **Actionable insights** (not just "correlations exist")
✅ **Professional presentation** (clean code, good documentation)
✅ **Industry relevance** (shows you understand insurance CX)

**Your differentiators**:
- Combined multiple advanced techniques in one cohesive project
- Business ROI focus (not just technical exercise)
- Persona development (shows CX empathy)
- A/B test simulation (shows experimental thinking)
- Professional dashboard (industry-ready deliverable)

---

## ⏱️ ESTIMATED TIMELINE

- **Phase 1**: 4-6 hours
- **Phase 2**: 8-10 hours
- **Phase 3**: 6-8 hours
- **Phase 4**: 4-6 hours
- **Phase 5**: 6-8 hours
- **Phase 6**: 8-10 hours

**Total**: 36-48 hours of focused work

**Suggested schedule** (if working part-time):
- Week 1: Phases 1-2
- Week 2: Phases 3-4
- Week 3: Phases 5-6
- Week 4: Documentation, dashboard polish, GitHub cleanup

---

## 📝 PORTFOLIO PRESENTATION TIPS

### **README.md Structure**:
```markdown
# Customer Lifetime Value Optimization Through Proactive Health Engagement

## Business Context
[1-2 paragraphs explaining the insurance industry challenge]

## Project Overview
- **Objective**: [Clear goal]
- **Dataset**: 25,000 insurance policyholders, 24 features
- **Techniques**: Segmentation, predictive modeling, A/B testing, ROI analysis

## Key Findings
1. [Finding 1 with metric]
2. [Finding 2 with metric]
3. [Finding 3 with metric]

## Recommendations
[3-5 actionable business recommendations]

## Project Structure
[Describe notebook flow]

## Tools & Technologies
Python | Pandas | Scikit-learn | Tableau | Git

## Dashboard
[Link to live dashboard or screenshots]

## How to Run
[Setup instructions]
```

### **DataCamp Workspace**:
- Create a clean, narrative-driven notebook
- Use markdown extensively to tell the story
- Include business context before each analysis section
- Add "So What?" after every finding
- End with a summary of recommendations

---

## 🎯 NEXT STEPS

1. **Review this roadmap** - Any questions or adjustments?
2. **Set up project structure** - Create GitHub repo, folders
3. **Phase 1 execution** - Start with data cleaning
4. **Iterative review** - I can help at each phase if needed

Ready to start? Let's begin with Phase 1! 🚀
