"""Implementation of the standings endpoint."""
from .url import NhlUrl

class Standings(NhlUrl):
    """Standings

    Args:
        NhlUrl: NhlUrl to be enriched with Standings-specific elements
    """

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
        ret_data = super().get_data()["records"]
        self.data = ret_data
        return ret_data
