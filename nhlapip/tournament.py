"""Implementation of the Tournaments endpoint."""

from .url import NhlUrl

class Tournament(NhlUrl):
    """Tournament

    Args:
        NhlUrl: NhlUrl to be enriched with Tournament-specific elements
    """
    def __init__(self, tournament_type, expand = None, season = None):
        pars = []
        if expand is not None:
            pars.append("expand=" + expand)
        if season is not None:
            pars.append("season=" + season)
        if pars == []:
            pars = None

        super().__init__(
            endpoint = "tournaments",
            suffixes = tournament_type,
            params = pars
        )
        self.data = None
