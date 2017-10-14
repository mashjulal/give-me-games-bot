class Website:

    def __init__(self):
        pass

    @staticmethod
    def as_website(d):
        w = Website()
        w.__dict__.update(d)
        return w
