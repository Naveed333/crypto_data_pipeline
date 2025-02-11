import praw
import pandas as pd

# Reddit API Credentials (Replace with your own)
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="crypto_scraper",
)

# Fetch posts from r/CryptoCurrency
subreddit = reddit.subreddit("CryptoCurrency")
posts = []
for post in subreddit.hot(limit=100):  # Get top 100 posts
    posts.append([post.title, post.score, post.num_comments, post.created_utc])

# Save to CSV
df = pd.DataFrame(posts, columns=["Title", "Upvotes", "Comments", "Timestamp"])
df.to_csv("../datasets/raw/reddit_data.csv", index=False)

print("✅ Reddit data saved successfully!")
