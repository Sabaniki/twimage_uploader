from typing import List

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from src.image_file import ImageFile


class Uploader:
    def __init__(self, dir_path, image_files):
        self.dir_path = dir_path
        self.image_files = image_files  # type: List[ImageFile]
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(None)
        self.fonder_id = "1hXqzPVaN-YaTjU8zf9v5mZzzUJsxhYrR"

    def login(self) -> None:
        self.gauth.CommandLineAuth()
        self.drive = GoogleDrive(self.gauth)

    def run(self) -> None:
        for image_file in self.image_files:
            file = self.drive.CreateFile({'title': image_file.name, 'mimeType': image_file.type,
                                          'parents': [{'kind': 'drive#fileLink', 'id': self.fonder_id}]})
            file.SetContentFile(self.dir_path + "" + image_file.name)
            file.Upload()
