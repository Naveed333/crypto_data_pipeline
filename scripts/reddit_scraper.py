import praw  # type: ignore
import pandas as pd  # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# Fetch posts from r/CryptoCurrency
subreddit = reddit.subreddit("CryptoCurrency")
print("🚀 Fetching data from Reddit...", subreddit)
posts = []
for post in subreddit.hot(limit=100):  # Get top 100 posts
    posts.append([post.title, post.score, post.num_comments, post.created_utc])

print("📊 Data fetched successfully!", posts[0])
if posts:
    df = pd.DataFrame(posts, columns=["Title", "Upvotes", "Comments", "Timestamp"])
    df.to_csv("./datasets/raw/reddit_data.csv", index=False)
    print("✅ Reddit data saved successfully!")
else:
    print("❌ No data fetched from Reddit!")
