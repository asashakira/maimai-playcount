""" Tweeter """

import os

import dotenv
import requests_oauthlib


class Tweeter:
    """tweeter class"""

    def __init__(
        self,
        key_path: str | None = os.path.expanduser("~/.twitterapi.key"),
    ) -> None:
        if key_path is not None and os.path.isfile(key_path):
            dotenv.load_dotenv(key_path)

        self.twitter_oauth: requests_oauthlib.OAuth1Session = self.get_twitter_oauth()

    @staticmethod
    def get_twitter_oauth() -> requests_oauthlib.OAuth1Session:
        """Create a Twitter OAuth Object."""
        consumer_key = os.environ["CONSUMER_KEY"]
        consumer_secret = os.environ["CONSUMER_SECRET"]
        access_token = os.environ["ACCESS_TOKEN"]
        access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

        return requests_oauthlib.OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

    def tweet_playcount(self, tweet: str):
        response = self.twitter_oauth.post(
            "https://api.twitter.com/2/tweets",
            json={"text": tweet},
        )
        return response

    def run(self, tweet: str):
        response = self.tweet_playcount(tweet)

        if response.status_code != 201:
            return f"Request returned an error: {response.status_code} {response.text}"

        return f"Response code: {response.status_code}"
