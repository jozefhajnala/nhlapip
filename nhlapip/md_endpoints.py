"""Implementations of the metadata endpoints."""
from .url import NhlUrl

class MdEndpoint(NhlUrl):
    """Generic metadata endpoint."""
    def __init__(self, endpoint):
        super().__init__(endpoint = endpoint)

class GameTypesMd(MdEndpoint):
    """Implementation of the gameTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "gameTypes")

class GameStatusMd(MdEndpoint):
    """Implementation of the gameStatus metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "gameStatus")

class PlayTypesMd(MdEndpoint):
    """Implementation of the playTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "playTypes")

class TournamentTypesMd(MdEndpoint):
    """Implementation of the tournamentTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "tournamentTypes")

class StandingsTypesMd(MdEndpoint):
    """Implementation of the standingsTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "standingsTypes")

class StatTypesMd(MdEndpoint):
    """Implementation of the statTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "statTypes")

class EventTypesMd(MdEndpoint):
    """Implementation of the eventTypes metadata endpoint."""
    def __init__(self):
        super().__init__(endpoint = "eventTypes")
