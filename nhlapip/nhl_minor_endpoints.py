from .nhl_url import NhlUrl

class MinorEndpoint(NhlUrl):
    def __init__(self, endpoint, id = None, elName = None):
        super().__init__(endpoint = endpoint, suffixes = id)
        self.elName = elName
    def get_data(self):
        retData = super().get_data()
        element = self.endpoint if self.elName is None else self.elName
        retData = retData[element]
        self.data = retData
        return retData

class Conferences(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "conferences", id = id)

class Divisions(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "divisions", id = id)

class Drafts(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "draft", id = id, elName = "drafts")

class Seasons(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "seasons", id = id)

class Awards(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "awards", id = id)

class Venues(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "venues", id = id)

class DraftProspects(MinorEndpoint):
    def __init__(self, id = None):
        super().__init__(endpoint = "draft/prospects", id = id, elName = "prospects")
