from typing import List

import tweepy
from src import twitter_secrets
from src.image_file import ImageFile


class TwitterImageGetter:
    def __init__(self):
        self.__auth = tweepy.OAuthHandler(twitter_secrets.twitter_consumer_key, twitter_secrets.twitter_consumer_secret)
        self.__api = tweepy.API(None)

    def login(self):
        redirect_url = self.__auth.get_authorization_url()
        print(redirect_url)
        pin = input()
        access_token, access_token_secret = self.__auth.get_access_token(pin)
        self.__auth.set_access_token(access_token, access_token_secret)
        self.__api = tweepy.API(self.__auth)

    def __get_fav_and_rt(self, count=20):
        return [tweet for tweet in self.__api.user_timeline(count=count) if
                (tweet.retweeted and tweet.favorited)]

    def get_image_url_list(self, count=20) -> List[ImageFile]:  # returns List<ImageFile>
        image_url_list = []
        tweets = self.__get_fav_and_rt(count)
        for tweet in tweets:
            try:
                if tweet.retweeted_status.extended_entities is not None:
                    for media in tweet.retweeted_status.extended_entities.get('media'):
                        media_url = media.get('media_url')
                        if ".png" in media_url or ".jpg" in media_url:
                            image_url_list.append(ImageFile(media_url))
            except AttributeError:
                print("This tweet does not contain any images. So, it's passed.")
                pass
        return image_url_list
