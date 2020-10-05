"""Implementations of the minor endpoints."""
from .url import NhlUrl

class MinorEndpoint(NhlUrl):
    """Generic minor endpoint."""
    def __init__(self, endpoint, oid = None, el_name = None):
        super().__init__(endpoint = endpoint, suffixes = oid)
        self.el_name = el_name
    def get_data(self):
        ret_data = super().get_data()
        element = self.endpoint if self.el_name is None else self.el_name
        ret_data = ret_data[element]
        self.data = ret_data
        return ret_data

class Conferences(MinorEndpoint):
    """Implementation of the conferences endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "conferences", oid = oid)

class Divisions(MinorEndpoint):
    """Implementation of the divisions endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "divisions", oid = oid)

class Drafts(MinorEndpoint):
    """Implementation of the drafts endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "draft", oid = oid, el_name = "drafts")

class Seasons(MinorEndpoint):
    """Implementation of the seasons endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "seasons", oid = oid)

class Awards(MinorEndpoint):
    """Implementation of the awards endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "awards", oid = oid)

class Venues(MinorEndpoint):
    """Implementation of the venues endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "venues", oid = oid)

class DraftProspects(MinorEndpoint):
    """Implementation of the draft prospects endpoint."""
    def __init__(self, oid = None):
        super().__init__(endpoint = "draft/prospects", oid = oid, el_name = "prospects")
