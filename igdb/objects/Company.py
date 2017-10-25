import pycountry


class Company:

    __NAME = "\n<b>{company_name}</b>"
    __DESCRIPTION = "\n{company_summary}"
    __COUNTRY = "\n<b>Country:</b> {company_country}"
    __SITE = "\n<b>Website:</b> {website_url}"

    def __init__(self):
        self.id = 0
        self.name = ""
        self.website = ""
        self.description = ""
        self.country = ""

    def __str__(self):
        msg = Company.__NAME.format(
            company_name=self.name)
        if self.description:
            msg += Company.__DESCRIPTION.format(
                company_summary=self.description)
        if self.country:
            msg += Company.__COUNTRY.format(
                company_country=self.country)
        if self.website:
            msg += Company.__SITE.format(
                website_url=self.website)
        return msg

    @staticmethod
    def as_company(d):
        c = Company()
        for key in d:
            if key == "country":
                country = pycountry.countries.get(numeric=str(d[key]))
                c.country = country.name
            else:
                c.__dict__[key] = d[key]
        return c
