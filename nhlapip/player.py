"""Implementation of the people endpoint."""
from .url import NhlUrl

class Player(NhlUrl):
    """Player

    Args:
        NhlUrl: NhlUrl to be enriched with Player-specific elements
    """

    def __init__(self, player_id):
        super().__init__(endpoint = "people", suffixes = player_id)
        self.player_id = player_id
        self.data = None
        self.stats = None

    def get_data(self):
        super().get_data()
        self.data = self.data["people"][0]
        return self.data

    def get_stats_allseasons(self):
        """Provides all seasons statistics for the player and stores in the stats property."""
        self.stats = NhlUrl(
            endpoint = "people",
            suffixes = [self.player_id, "stats"],
            params = {"stats": "yearByYear"}
        ).get_data()["stats"][0]["splits"]
        return self.stats
