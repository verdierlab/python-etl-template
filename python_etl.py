"""
python-etl-template

Simple ETL pipeline using Pandas.

Author: Verdiér
License: MIT
"""

from pathlib import Path

import pandas as pd


INPUT_FILE = "sales.csv"

OUTPUT_CSV = "sales_clean.csv"

OUTPUT_PARQUET = "sales.parquet"

REPORT_FILE = "report.txt"


def extract() -> pd.DataFrame:
    """Read CSV data."""

    return pd.read_csv(INPUT_FILE)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform the dataset."""

    df = df.drop_duplicates()

    df = df.dropna()

    df["quantity"] = df["quantity"].astype(int)

    df["price"] = df["price"].astype(float)

    df["total"] = df["quantity"] * df["price"]

    return df


def load(df: pd.DataFrame):
    """Save transformed data."""

    df.to_csv(
        OUTPUT_CSV,
        index=False,
    )

    df.to_parquet(
        OUTPUT_PARQUET,
        index=False,
    )


def report(df: pd.DataFrame):

    text = f"""
ETL REPORT
==========

Rows: {len(df)}

Columns: {len(df.columns)}

Total Sales: {df["total"].sum():.2f}

Average Sale: {df["total"].mean():.2f}
"""

    Path(REPORT_FILE).write_text(
        text.strip(),
        encoding="utf-8",
    )


def run():

    data = extract()

    clean = transform(data)

    load(clean)

    report(clean)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run()
