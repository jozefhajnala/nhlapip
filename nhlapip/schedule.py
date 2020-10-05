"""Implementation of the Schedule endpoint."""
from .url import NhlUrl

class Schedule(NhlUrl):
    """Schedule

    Args:
        NhlUrl: NhlUrl to be enriched with Schedule-specific elements
    """
    def __init__( # pylint: disable=too-many-arguments
        self,
        season=None,
        teamId=None,
        startDate=None,
        endDate=None,
        gameType=None,
        expand=None
    ):
        pars = []
        if season is not None:
            pars.append("season=" + season)
        if teamId is not None:
            pars.append("teamId=" + teamId)
        if startDate is not None:
            pars.append("startDate=" + startDate)
        if endDate is not None:
            pars.append("endDate=" + endDate)
        if gameType is not None:
            pars.append("gameTypes=" + gameType)
        if expand is not None:
            pars.append("expand=" + expand)
        if pars == []:
            pars = None

        super().__init__(endpoint = "schedule", params = pars)
        self.data = None

    def get_data(self):
        ret_data = super().get_data()["dates"]
        self.data = ret_data
        return ret_data
