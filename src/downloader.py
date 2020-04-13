import asyncio
import os
import urllib.error
import urllib.request
from typing import List

from src.image_file import ImageFile


class Downloader:
    def __init__(self, dir_path, image_files):
        self.dir_path = dir_path
        self.image_files = image_files  # type: List[ImageFile]

    def run(self):
        os.makedirs("tmp/", exist_ok=True)
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.fetch())

    async def fetch(self):
        return await asyncio.wait(
            [
                self.download(image_file.url,
                              dir_path=os.path.join(self.dir_path, os.path.basename(image_file.name)))
                for i, image_file in
                enumerate(self.image_files)
            ]
        )

    async def download(self, url, dir_path):
        try:
            with urllib.request.urlopen(url) as web_file, open(dir_path, 'wb') as local_file:
                local_file.write(web_file.read())
        except urllib.error.URLError as e:
            print(e)
