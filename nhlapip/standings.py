from .url import NhlUrl

class Standings(NhlUrl):
    def __init__(self, season=None, standingsType=None, expand=None):
        pars = []
        if season is not None:
            pars.append("season=" + season)
        if standingsType is not None:
            pars.append("standingsType=" + standingsType)
        if expand is not None:
            pars.append("expand=" + expand)
        if pars == []:
            pars = None

        super().__init__(endpoint = "standings", params = pars)
        self.data = None

    def get_data(self):
        retData = super().get_data()["records"]
        self.data = retData
        return retData
