import tweepy
import SecretKey
class TwitterImageGetter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler()
    def login(self):

