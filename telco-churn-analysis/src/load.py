"""
load.py
Loads the feature Parquet into BigQuery (or DuckDB locally).
"""
import os
import pandas as pd
import duckdb
from pathlib import Path
from dotenv import load_dotenv
import logging

load_dotenv()
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

PARQUET_PATH = "data/processed/telco_churn_features.parquet"
DUCKDB_PATH  = "data/telco_churn.duckdb"
BQ_PROJECT   = os.getenv("GCP_PROJECT_ID")
BQ_DATASET   = os.getenv("BQ_DATASET", "telco_analytics")
BQ_TABLE     = "customers"

def load_to_duckdb(parquet: str = PARQUET_PATH) -> None:
    """Load to local DuckDB — no credentials required."""
    con = duckdb.connect(DUCKDB_PATH)
    con.execute(f"""
        CREATE OR REPLACE TABLE customers AS
        SELECT * FROM read_parquet('{parquet}')
    """)
    count = con.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
    log.info(f"DuckDB: {count:,} rows loaded into `customers`")
    con.close()

def load_to_bigquery(parquet: str = PARQUET_PATH) -> None:
    """Load to Google BigQuery — requires GCP credentials in env."""
    from google.cloud import bigquery
    client = bigquery.Client(project=BQ_PROJECT)
    table_ref = f"{BQ_PROJECT}.{BQ_DATASET}.{BQ_TABLE}"
    df = pd.read_parquet(parquet)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    log.info(f"BigQuery: {len(df):,} rows loaded into `{table_ref}`")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=["duckdb", "bigquery"], default="duckdb")
    args = parser.parse_args()

    if args.target == "duckdb":
        load_to_duckdb()
    else:
        load_to_bigquery()