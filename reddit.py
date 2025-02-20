import praw
import os

CLIENT_ID = os.getenv('REDDIT_ID')
CLIENT_SECRET = os.getenv('REDDIT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT,
)
