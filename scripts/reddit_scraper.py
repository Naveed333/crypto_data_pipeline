import praw  # Reddit API library
import os
from dotenv import load_dotenv  # To load environment variables
import csv  # For saving data as CSV
from datetime import datetime  # For formatting the date

# Load environment variables from .env file
load_dotenv()

# Reddit API Credentials
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# Define subreddits and keywords
subreddits = ["CryptoCurrency", "Bitcoin"]  # Subreddits to scrape
keywords = [
    "crypto",
    "bitcoin",
    "btc",
    "BTC",
    "ETH",
    "Etherum",
    "sol",
    "Blockchain",
    "Altcoin",
    "Crypto Wallet",
    "Web3",
    "Token",
    "NFT",
    "DeFi",
    "Crypto Exchange",
    "Crypto Trading",
    "Crypto Investment",
    "Crypto Market",
    "Crypto News",
    "Crypto Regulation",
    "Crypto Mining",
    "Crypto Payment",
    "Crypto Tax",
]  # Keywords to filter posts

# Initialize an empty list to store posts
posts = []

# Fetch posts from each subreddit
for subreddit_name in subreddits:
    print(f"🚀 Fetching data from r/{subreddit_name}...")
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.hot(limit=100):  # Fetch top 100 posts
        # Filter posts containing keywords in the title or post text
        if any(
            keyword.lower() in (post.title + post.selftext).lower()
            for keyword in keywords
        ):
            posts.append(
                {
                    "Title": post.title,
                    "Post Text": post.selftext,
                    "Author": post.author.name if post.author else "Unknown",
                    "Date": post.created_utc,
                    "Upvotes": post.score,
                    "Subreddit": subreddit_name,
                }
            )

output_file = "./datasets/raw/reddit_data.csv"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

if posts:
    print(f"📊 Writing {len(posts)} posts to {output_file}...")
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=["Title", "Post Text", "Author", "Date", "Upvotes", "Subreddit"],
        )
        writer.writeheader()
        writer.writerows(posts)
    print("✅ Reddit data saved successfully!")
else:
    print("❌ No matching posts found!")
