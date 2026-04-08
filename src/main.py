from extract import extract
from transform import transform
from load import load

RAW_PATH = "data/raw/sales.csv"
OUTPUT_PATH = "data/processed/clean_sales.csv"

def run_pipeline():
    df = extract(RAW_PATH)
    df = transform(df)
    load(df, OUTPUT_PATH)
    print("✅ ETL pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()