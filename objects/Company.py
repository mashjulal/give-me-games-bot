class Company:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.url = ""
        self.logo = ""
        self.description = ""

    @staticmethod
    def as_company(d):
        c = Company()
        c.__dict__.update(d)
        return c