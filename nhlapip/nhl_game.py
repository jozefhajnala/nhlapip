from .nhl_url import NhlUrl
from .const import NHLAPI_BASEURL

class Game(NhlUrl):
    def __init__(self, id):
        super().__init__(endpoint = "game", suffixes = id)
        self.id = id
        self.data = None

    def create_game_element(self, element):
        """Crate a game element `NhlUrl`

        Args:
            element (`string`): Which element to create,
              one of "boxscore", "linescore", "feed/live", "content".


        Returns:
            `NhlUrl`: object for that element of this game.
        """
        return NhlUrl(endpoint = self.endpoint, suffixes = [self.id, element])

    def get_boxscore(self):
        self.boxscore = self.create_game_element("boxscore")
        self.boxscore.get_data()
    
    def get_linescore(self):
        self.linescore = self.create_game_element("linescore")
        self.linescore.get_data()

    def get_feed(self):
        self.feed = self.create_game_element("feed/live")
        self.feed.get_data()

    def get_content(self):
        self.content = self.create_game_element("content")
        self.content.get_data()

