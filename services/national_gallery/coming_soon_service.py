from .national_gallery_base_service import InnerService


class ComingSoonService(InnerService):
    def __init__(self, url):
        self._url = url

    def get_data(self):
        zipped = super().get_data()

        return self.get_exhibition_details(zipped[1])