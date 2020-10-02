from .url import NhlUrl

class Tournament(NhlUrl):
    def __init__(self, type, expand = None, season = None):
        pars = []
        if expand is not None:
            pars.append("expand=" + expand)
        if season is not None:
            pars.append("season=" + season)
        if pars == []:
            pars = None

        super().__init__(
            endpoint = "tournaments",
            suffixes = type,
            params = pars
        )
        self.data = None
