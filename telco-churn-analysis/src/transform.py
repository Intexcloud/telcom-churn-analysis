"""
transform.py
Feature engineering on the clean Parquet — adds derived columns for analytics.
"""
import pandas as pd
import numpy as np
from pathlib import Path
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def add_tenure_band(df: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 12, 24, 36, 48, 60, float("inf")]
    labels = ["0-12 mo", "13-24 mo", "25-36 mo", "37-48 mo", "49-60 mo", "60+ mo"]
    df["tenure_band"] = pd.cut(df["tenure"], bins=bins, labels=labels, right=True)
    return df

def add_service_count(df: pd.DataFrame) -> pd.DataFrame:
    service_cols = [
        "PhoneService", "MultipleLines", "InternetService",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies"
    ]
    # Count services that are "Yes" (not "No" or "No internet service")
    df["service_count"] = (
        df[service_cols].apply(lambda col: col == "Yes", axis=0).sum(axis=1)
    )
    return df

def add_monthly_charges_band(df: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 30, 60, 90, float("inf")]
    labels = ["<$30", "$30-60", "$60-90", "$90+"]
    df["charges_band"] = pd.cut(df["MonthlyCharges"], bins=bins, labels=labels)
    return df

def add_is_auto_pay(df: pd.DataFrame) -> pd.DataFrame:
    auto_methods = {"Bank transfer (automatic)", "Credit card (automatic)"}
    df["is_auto_pay"] = df["PaymentMethod"].isin(auto_methods)
    return df

def add_clv_estimate(df: pd.DataFrame) -> pd.DataFrame:
    """Crude CLV = TotalCharges + expected future revenue if not churned."""
    avg_months_remaining = 24  # assumption
    df["estimated_clv"] = np.where(
        ~df["Churn"],
        df["TotalCharges"] + df["MonthlyCharges"] * avg_months_remaining,
        df["TotalCharges"]
    )
    return df

def transform(in_path: str = "data/processed/telco_churn_clean.parquet",
              out_path: str = "data/processed/telco_churn_features.parquet") -> pd.DataFrame:
    df = pd.read_parquet(in_path)
    log.info(f"Loaded {len(df):,} rows for transformation")

    df = add_tenure_band(df)
    df = add_service_count(df)
    df = add_monthly_charges_band(df)
    df = add_is_auto_pay(df)
    df = add_clv_estimate(df)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out_path, index=False)
    log.info(f"Features saved → {out_path}")
    return df

if __name__ == "__main__":
    transform()