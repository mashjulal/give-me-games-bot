from urllib.parse import urlparse


class Cover:

    def __init__(self):
        self.url = ""
        self.height = 0
        self.width = 0

    @staticmethod
    def as_cover(d):
        c = Cover()
        for key in d:
            if key == "url":
                c.__dict__[key] = "https:" + d[key].replace("/t_thumb", "")
            else:
                c.__dict__[key] = d[key]
        return c
