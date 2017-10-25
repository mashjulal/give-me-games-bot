class Platform:

    __NAME = "<b>{platform_name}</b>"
    __DESCRIPTION = "\n{platform_summary}"
    __ALTER_NAME = "\n<b>Alternative name:</b> {alter_name}"
    __GENERATION = "\n<b>Generation:</b> {generation}"

    def __init__(self):
        self.id = 0
        self.name = ""
        self.summary = ""
        self.alternative_name = ""
        self.generation = 0

    @staticmethod
    def as_platform(d):
        p = Platform()
        p.__dict__.update(d)
        return p

    def __str__(self):
        s = Platform.__NAME.format(platform_name=self.name)

        if self.summary:
            s += Platform.__DESCRIPTION.format(platform_summary=self.summary)
        if self.alternative_name:
            s += Platform.__ALTER_NAME.format(alter_name=self.alternative_name)
        if self.generation:
            s += Platform.__GENERATION.format(generation=self.generation)

        return s
