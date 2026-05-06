import duckdb

con = duckdb.connect(r'C:\telco-churn-analysis\data\telco_churn.duckdb')

# Export semua tabel ke CSV
tables = {
    'churn_by_contract': """
        SELECT Contract,
            COUNT(*) AS customers,
            ROUND(AVG(CASE WHEN Churn THEN 1.0 ELSE 0 END)*100,1) AS churn_rate_pct,
            ROUND(SUM(CASE WHEN Churn THEN MonthlyCharges END),0) AS mrr_at_risk
        FROM customers GROUP BY 1 ORDER BY churn_rate_pct DESC
    """,
    'churn_by_internet': """
        SELECT InternetService,
            COUNT(*) AS customers,
            ROUND(AVG(CASE WHEN Churn THEN 1.0 ELSE 0 END)*100,1) AS churn_rate_pct
        FROM customers GROUP BY 1 ORDER BY churn_rate_pct DESC
    """,
    'churn_by_payment': """
        SELECT PaymentMethod,
            COUNT(*) AS customers,
            ROUND(AVG(CASE WHEN Churn THEN 1.0 ELSE 0 END)*100,1) AS churn_rate_pct
        FROM customers GROUP BY 1 ORDER BY churn_rate_pct DESC
    """,
    'churn_by_tenure': """
        SELECT
            CASE
                WHEN tenure BETWEEN 0  AND 12 THEN '0-12 mo'
                WHEN tenure BETWEEN 13 AND 24 THEN '13-24 mo'
                WHEN tenure BETWEEN 25 AND 36 THEN '25-36 mo'
                WHEN tenure BETWEEN 37 AND 48 THEN '37-48 mo'
                WHEN tenure BETWEEN 49 AND 60 THEN '49-60 mo'
                ELSE '60+ mo'
            END AS tenure_band,
            COUNT(*) AS customers,
            ROUND(AVG(CASE WHEN Churn THEN 1.0 ELSE 0 END)*100,1) AS churn_rate_pct,
            MIN(tenure) AS sort_order
        FROM customers GROUP BY 1 ORDER BY sort_order
    """,
    'customers_full': "SELECT * FROM customers"
}

for name, query in tables.items():
    df = con.execute(query).df()
    path = rf'C:\telco-churn-analysis\data\{name}.csv'
    df.to_csv(path, index=False)
    print(f'✅ {name}.csv tersimpan ({len(df)} baris)')

print("\n✅ Semua file siap diupload ke Looker Studio!")