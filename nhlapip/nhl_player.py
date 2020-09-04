from .nhl_url import NhlUrl
from .const import NHLAPI_BASEURL

class Player(NhlUrl):
    def __init__(self, id):
        super().__init__(endpoint = "people", suffixes = id)
        self.playerId = id
        self.data = None
        self.stats = None

    def get_data(self):
         super().get_data()
         self.data = self.data["people"][0]
         self.data

    def get_stats_allseasons(self):
        self.stats = NhlUrl(
            endpoint = "people",
            suffixes = [self.playerId, "stats"],
            params = {"stats": "yearByYear"}
        ).get_data()["stats"][0]["splits"]


