from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "customer_data.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

def profile(df):
    return {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "duplicate_record_ids": int(df["record_id"].duplicated().sum()),
        "missing_values": {k:int(v) for k,v in df.isna().sum().items() if v},
        "negative_income": int((df["annual_income"] < 0).sum()),
        "invalid_age": int(((df["age"] < 18) | (df["age"] > 100)).fillna(False).sum()),
        "duplicate_customer_ids": int(df["customer_id"].duplicated().sum()),
    }

def run():
    df = pd.read_csv(DATA)
    report = profile(df)

    checks = {
        "record_ids_unique": report["duplicate_record_ids"] == 0,
        "no_missing_customer_ids": report["missing_values"].get("customer_id", 0) == 0,
        "no_negative_income": report["negative_income"] == 0,
        "valid_age_range": report["invalid_age"] == 0,
    }
    report["checks"] = checks
    report["passed_checks"] = sum(checks.values())
    report["total_checks"] = len(checks)
    report["status"] = "PASS" if all(checks.values()) else "REVIEW"

    with open(OUT/"quality_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))
    return report

if __name__ == "__main__":
    run()
