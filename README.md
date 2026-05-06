# 📡 Telco Customer Churn Analysis
> End-to-End Data Analytics Pipeline — Python, SQL, DuckDB & Looker Studio

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![DuckDB](https://img.shields.io/badge/SQL-DuckDB-yellow)
![Looker](https://img.shields.io/badge/BI-Looker_Studio-4285F4?logo=looker)

---

## 🎯 Business Problem
A telco company is experiencing customer churn, resulting in a loss of Monthly Recurring Revenue (MRR). This analysis identifies:
- Customer segments most at risk of churn
- Revenue at risk (MRR at risk)
- Retention action recommendations for the business team

---

## 💡 Key Insights

| Findings | Churn Rate | Actions |
|--------|-----------|------|
| Month-to-Month Contracts | 43% | Upsell to Annual Contracts |
| Fiber Optic Internet | 42% | Price Review vs. Competitors |
| Pay via Electronic Check | 45% | Encourage Auto-Pay |
| Tenure < 12 months | 48% | 90-Day Onboarding Program |

---

## 🏗️ Project Structure
```text
telco-churn-analysis/
├── 📂 src/
│    ├── 📄 ingestion.py          # ETL: Schema validation & data cleaning
│    ├── 📄 transform.py          # Analytics: Feature engineering & business logic
│    ├── 📄 load.py               # Data Warehouse: Loading to DuckDB/BigQuery
│    └── 📄 export.py             # Data Export: Export Data for Looker Studio
├── 📂 data/
│   ├── 📂 raw/                   # Original dataset (WA_Fn-UseC_-Telco-Customer-Churn.csv)
│   ├── 📂 processed/             # Cleaned and featured Parquet files
│   └── 📄 telco_churn.duckdb     # database     
├── 📄 requirements.txt      # Project dependencies
└── 📄 README.md             # Project documentation
```
---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/USERNAME/telco-churn-analysis.git
cd telco-churn-analysis
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install duckdb pandas matplotlib seaborn plotly openpyxl
```

### 3. Download Dataset
Download from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
→ Save to `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`

### 4. Run the Pipeline
```bash
# 1. Clean the data
python ingestion.py --input data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv    

# 2. Apply transformations
python transform.py

# 3. Load to local DuckDB
python load.py --target duckdb
```
---

## 📊 Dashboard

The dashboard was created in **Google Looker Studio** using the CSV export from DuckDB.

---

## 🗃️ Dataset

**Source:** IBM Telco Customer Churn
**Link:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
**Total:** 7,043 customers, 21 features

---

## 📚 References

1. IBM Telco Dataset — https://www.kaggle.com/datasets/blastchar/telco-customer-churn
2. DuckDB Documentation — https://duckdb.org/docs
3. Google Looker Studio — https://lookerstudio.google.com
4. Pandas Documentation — https://pandas.pydata.org/docs

---

## 📄 License
MIT License

