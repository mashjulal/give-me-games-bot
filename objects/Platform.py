class Platform:

    def __init__(self):
        self.id = 0
        self.name = ""

    @staticmethod
    def as_platform(d):
        p = Platform()
        p.__dict__.update(d)
        return p
