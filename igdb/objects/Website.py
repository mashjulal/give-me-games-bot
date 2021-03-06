

class Website:

    __SITE = "<a href='{website_url}'>{website_name}</a>"

    __WEBSITES = {1: "official", 2: "wikia", 3: "wikipedia", 4: "facebook",
                5: "twitter", 6: "twitch", 8: "instagram", 9: "youtube",
                10: "iphone", 11: "ipad", 12: "android", 13: "steam"}

    def __init__(self):
        self.category = 0
        self.url = ""
        self.name = ""

    @staticmethod
    def as_website(d):
        w = Website()
        w.__dict__.update(d)
        w.name = Website.__WEBSITES[d["category"]]
        return w

    def __str__(self):
        s = Website.__SITE.format(
            website_name=self.name.capitalize(),
            website_url=self.url)

        return s
