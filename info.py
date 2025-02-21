from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import os
import json
import praw


load_dotenv()
CLIENT_ID = os.getenv('REDDIT_ID')
CLIENT_SECRET = os.getenv('REDDIT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')
NEWS_API = os.getenv('NEWS_API_KEY')
NEWS_URL = "https://newsapi.org/v2/everything"

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT,
)
crypto_subreddit = reddit.subreddit("cryptocurrency")



def get_news(choice):
    parameters = {
        'symbol': choice
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': NEWS_API,
    }
    session = Session()
    session.headers.update(headers)
    url = NEWS_URL
    try:
        response = session.get(url + f"?q={choice}%20OR%20bitcoin&apikey={NEWS_API}", params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
