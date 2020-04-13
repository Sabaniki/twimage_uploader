class ImageFile:
    def __init__(self, image_file_url):
        self.url = image_file_url
        self.name = image_file_url[-19:]
        self.type = "image/jpg" if ".jpg" in self.name else "image/.png"
