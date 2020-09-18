from .nhl_url import NhlUrl
from .const import NHLAPI_BASEURL

class MdEndpoint(NhlUrl):
    def __init__(self, endpoint):
        super().__init__(endpoint = endpoint)

class GameTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "gameTypes")

class GameStatusesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "gameStatus")

class PlayTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "playTypes")

class TournamentTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "tournamentTypes")

class StandingsTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "standingsTypes")

class StatTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "statTypes")

class EventTypesMd(MdEndpoint):
    def __init__(self):
        super().__init__(endpoint = "eventTypes")
