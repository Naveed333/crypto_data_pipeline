from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq()

# Define search terms
keywords = ["Bitcoin", "Ethereum", "Crypto Regulation"]
pytrends.build_payload(kw_list=keywords, timeframe="today 12-m", geo="US")

# Fetch data
data = pytrends.interest_over_time()

# Save to CSV
data.to_csv("../datasets/raw/google_trends.csv")
print("✅ Google Trends data saved successfully!")
