"""
Create a sample dataset and run the ETL pipeline.
"""

import pandas as pd

from python_etl import run


sample = pd.DataFrame(
    {
        "product": [
            "Laptop",
            "Mouse",
            "Keyboard",
            "Monitor",
            "Mouse",
        ],
        "quantity": [
            2,
            5,
            3,
            1,
            5,
        ],
        "price": [
            1200,
            25,
            75,
            350,
            25,
        ],
    }
)

sample.to_csv(
    "sales.csv",
    index=False,
)

run()

print()

print("Generated files:")

print("- sales_clean.csv")

print("- sales.parquet")

print("- report.txt")
