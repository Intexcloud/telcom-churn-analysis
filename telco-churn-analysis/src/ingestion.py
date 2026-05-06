"""
ingestion.py
Reads raw Telco CSV, validates schema, outputs a clean Parquet file.
"""
import pandas as pd
import numpy as np
import argparse
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

REQUIRED_COLS = [
    "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
    "tenure", "PhoneService", "MultipleLines", "InternetService",
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
    "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"
]

def load_raw(path: str) -> pd.DataFrame:
    log.info(f"Loading raw data from {path}")
    df = pd.read_csv(path)
    log.info(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
    return df

def validate_schema(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        log.error(f"Missing columns: {missing}")
        sys.exit(1)
    log.info("Schema validation passed ✓")

def clean(df: pd.DataFrame) -> pd.DataFrame:
    # TotalCharges arrives as string with spaces for new customers
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    nulls = df["TotalCharges"].isna().sum()
    if nulls:
        log.warning(f"Filling {nulls} null TotalCharges with 0 (new customers)")
        df["TotalCharges"] = df["TotalCharges"].fillna(0.0)

    # Normalise Churn to boolean
    df["Churn"] = df["Churn"].map({"Yes": True, "No": False})

    # SeniorCitizen: coerce to bool
    df["SeniorCitizen"] = df["SeniorCitizen"].astype(bool)

    log.info("Data cleaning complete ✓")
    return df

def save(df: pd.DataFrame, out_dir: str = "data/processed") -> Path:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    out = Path(out_dir) / "telco_churn_clean.parquet"
    df.to_parquet(out, index=False)
    log.info(f"Saved cleaned data → {out}")
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to raw CSV")
    parser.add_argument("--out-dir", default="data/processed")
    args = parser.parse_args()

    df = load_raw(args.input)
    validate_schema(df)
    df = clean(df)

    log.info(f"Churn rate: {df['Churn'].mean():.1%}")
    log.info(f"MRR at risk: ${df.loc[df['Churn'], 'MonthlyCharges'].sum():,.0f}")

    save(df, args.out_dir)

if __name__ == "__main__":
    main()