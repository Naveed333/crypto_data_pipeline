import pandas as pd

# Example: Load a Kaggle dataset
dataset_url = "https://raw.githubusercontent.com/datasets/cryptocurrency/master/data/crypto-markets.csv"
df = pd.read_csv(dataset_url)

# Save to CSV
df.to_csv("../datasets/raw/crypto_public_data.csv", index=False)
print("✅ Public dataset saved successfully!")
