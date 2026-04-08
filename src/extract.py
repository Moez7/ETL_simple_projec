import pandas as pd

def extract(path):
    print("📥 Extracting data...")
    df = pd.read_csv(path)
    return df