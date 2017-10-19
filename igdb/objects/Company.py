import pycountry


class Company:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.website = ""
        self.logo_url = ""
        self.description = ""
        self.country = ""

    @staticmethod
    def as_company(d):
        c = Company()
        for key in d:
            if key == "logo":
                url = "https:" + d[key]["url"].replace("/t_thumb", "")
                c.logo_url = url
            elif key == "country":
                country = pycountry.countries.get(numeric=str(d[key]))
                c.country = country.name
            else:
                c.__dict__[key] = d[key]
        return c
