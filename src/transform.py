import pandas as pd

def transform(df):
    print("🔄 Transforming data...")

    # Handle missing price
    df['price'] = df['price'].fillna(0)

    # Create total price
    df['total_price'] = df['price'] * df['quantity']

    # Normalize customer names
    df['customer'] = df['customer'].str.lower()

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    return df