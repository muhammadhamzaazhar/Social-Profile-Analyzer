import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)

def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted", "text", and "url".
    """
    try:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )

        tweet_list = []
        for tweet in tweets.data:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

        return tweet_list
    except Exception as e:
        raise RuntimeError(f"[Twitter Scraping Failed]: {e}")

def scrape_user_tweets_mock(username="EdenEmarco177", num_tweets=5):
    HAMZA_TWITTER_GIST = "https://gist.githubusercontent.com/muhammadhamzaazhar/d7be4f83b15939093f65f1fd4ff1f14d/raw/8ac4901fc807304b031eb69094edd6731f33202b/muhammad-hamza-azhar-tweepy.json"
    tweets = requests.get(HAMZA_TWITTER_GIST, timeout=5).json()

    tweet_list = []
    for tweet in tweets:

        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list
