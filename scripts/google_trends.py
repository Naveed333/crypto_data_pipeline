import time
from pytrends.request import TrendReq  # type: ignore
import pandas as pd  # type: ignore
import os

# Define search parameters
# KEYWORDS = ["Bitcoin price", "Ethereum", "Crypto regulation"]
# KEYWORDS = ["Bitcoin price", "Crypto regulation"]
KEYWORDS = ["Bitcoin price"]
TIMEFRAME = "today 12-m"
REGION = "US"
OUTPUT_DIR = "./datasets/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "google_trends.csv")


def fetch_google_trends(keywords, timeframe, region, output_path):
    try:
        print("🔄 Fetching Google Trends data...")
        pytrends = TrendReq()

        # Add a delay between requests to prevent getting blocked
        time.sleep(20)

        pytrends.build_payload(kw_list=keywords, timeframe=timeframe, geo=region)
        data = pytrends.interest_over_time()

        if data.empty:
            print("⚠️ No data found for the given keywords.")
            return

        # Reshape data
        data.reset_index(inplace=True)
        data = data.melt(
            id_vars=["date"], var_name="Keyword", value_name="Interest Score"
        )
        data.rename(columns={"date": "Date"}, inplace=True)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False)

        print(f"✅ Google Trends data saved successfully at: {output_path}")

    except Exception as e:
        print(f"❌ Error: Failed to fetch data. Details: {e}")


if __name__ == "__main__":
    fetch_google_trends(KEYWORDS, TIMEFRAME, REGION, OUTPUT_FILE)
