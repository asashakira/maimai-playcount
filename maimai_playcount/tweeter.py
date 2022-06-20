from requests_oauthlib import OAuth1Session
import os
import dotenv


class Tweeter:
    """tweeter class"""

    def __init__(
        self,
        key_path: str | None = os.path.expanduser("~/.twitterapi.key"),
    ) -> None:
        if key_path is not None and os.path.isfile(key_path):
            dotenv.load_dotenv(key_path)

        self.twitter_oauth: OAuth1Session = self.get_twitter_oauth()

    @staticmethod
    def get_twitter_oauth() -> OAuth1Session:
        """Create a Twitter OAuth Object."""
        consumer_key = os.environ["CONSUMER_KEY"]
        consumer_secret = os.environ["CONSUMER_SECRET"]
        access_token = os.environ["ACCESS_TOKEN"]
        access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
        return OAuth1Session(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret,
        )
