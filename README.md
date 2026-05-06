# 📡 Telco Customer Churn Analysis
> End-to-End Data Analytics Pipeline — Python, SQL, DuckDB & Looker Studio

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![DuckDB](https://img.shields.io/badge/SQL-DuckDB-yellow)
![Looker](https://img.shields.io/badge/BI-Looker_Studio-4285F4?logo=looker)

---

**Live Dashboard:** [View Interactive Dashboard Here](https://datastudio.google.com/embed/u/0/reporting/5c0c882f-a70e-4008-a4cf-dee78a94dc18/page/UWNxF)

---
## 📌 Project Overview
Customer retention is highly critical in the telecommunications industry. The cost of acquiring a new customer is significantly higher than retaining an existing one. This project focuses on analyzing a Telco Customer Churn dataset to identify key drivers of customer attrition, quantify the Monthly Recurring Revenue (MRR) at risk, and provide data-driven recommendations to improve retention rates.

---

### 🎯 Business Problem
* **Revenue Threat:** The telecommunications company is experiencing continuous customer attrition (churn), which directly threatens the Monthly Recurring Revenue (MRR).
* **Analytical Need:** The business must identify which customer segments are most likely to churn, pinpoint the specific lifecycle stage where drop-offs occur, and understand the driving factors.
* **Strategic Goal:** By uncovering these patterns, the marketing and retention teams can implement proactive, data-driven strategies to minimize churn and secure long-term revenue.
---

### 💡 Key Insights
* **The 12-Month Churn Cliff:** A massive drop-off occurs among month-to-month customers within their first 12 months of service (plunging from 1,955 to just 394 active users in the second year).
* **High Financial Exposure:** The month-to-month segment is not only losing the most customers but also holds the largest concentration of Monthly Recurring Revenue (MRR) at risk.
* **Long-Term Stability:** Customers on one-year and two-year contracts display highly stable retention heatmaps over time, proving that early commitment secures Customer Lifetime Value (LTV).
* **Payment Method Friction:** Customers using manual payment methods, specifically Electronic Checks, show a significantly higher churn risk compared to those using automatic payments (Credit Card/Bank Transfer).
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

