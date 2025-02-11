import requests  # type: ignore
import pandas as pd  # type: ignore

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": "false",
}

try:
    print("🔄 Fetching real-time crypto data...")
    response = requests.get(API_URL, params=params)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save dataset
    df.to_csv("./datasets/raw/crypto_public_data.csv", index=False)
    print("✅ Real-time crypto dataset saved successfully!")

except Exception as e:
    print(f"❌ Error: Failed to fetch data. Details: {e}")
