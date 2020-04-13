from src.twitter_image_getter import TwitterImageGetter
from src.downloader import Downloader
from src.uploader import Uploader

if __name__ == '__main__':
    tmp_dir = "tmp/"
    twitter_image_getter = TwitterImageGetter()
    twitter_image_getter.login()
    image_urls = twitter_image_getter.get_image_url_list()
    downloader = Downloader(tmp_dir, image_urls)
    downloader.run()
    uploader = Uploader(tmp_dir, image_urls)
    uploader.login()
    uploader.run()
