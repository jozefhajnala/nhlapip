"""Implementation of the game endpoint."""
from .url import NhlUrl

class Game(NhlUrl):
    """Game

    Args:
        NhlUrl: NhlUrl to be enriched with Game-specific elements
    """
    def __init__(self, game_id):
        """[summary]

        Args:
            game_id (str): game id is a 10 digit number where thes
                * first 4 digits identify the season of the game, for instance
                  2017 for the 2017-2018 season.
                * next 2 digits give the type of game, where
                    * 01 - preseason,
                    * 02 - regular season,
                    * 03 - playoffs,
                    * 04 - all-star.
                * final 4 digits identify the specific game number
                    * for regular season and preseason games, this ranges from
                      0001 to the number of games played. That is 1271 for
                      seasons with 31 teams and 1230 for seasons with 30 teams.
                    * for playoff games, the
                        * second digit gives the round of the playoffs
                        * third digit specifies the match-up
                        * fourth digit specifies the game (out of 7)
        """
        super().__init__(endpoint = "game", suffixes = game_id)
        self.game_id = game_id
        self.data = None
        self.boxscore = None
        self.linescore = None
        self.feed = None
        self.content = None

    def create_game_element(self, element):
        """Crate a game element `NhlUrl`

        Args:
            element (str): Which element to create,
              one of "boxscore", "linescore", "feed/live", "content".

        Returns:
            `NhlUrl`: object for that element of this game.
        """
        return NhlUrl(endpoint = self.endpoint, suffixes = [self.game_id, element])

    def get_boxscore(self):
        """Get data from the boxscore endpoint and store in the boxscore property.

             Provides far less detail than `get_feed`.

             May be more suitable for analyzing post-game statistics
             including goals, shots, penalty minutes, blocked, takeaways, etc.
        """
        self.boxscore = self.create_game_element("boxscore")
        self.boxscore.get_data()

    def get_linescore(self):
        """Get data from the linescore endpoint and store in the linescore property.

             Provides even fewer details than `get_boxscore()`.

             Has goals, shots on goal, power-play
             and goalie pulled status, number of skaters and shootout
             information if applicable.
        """
        self.linescore = self.create_game_element("linescore")
        self.linescore.get_data()

    def get_feed(self):
        """Get data from the feed/live endpoint and store in the feed property.

             Provides data about a specified game id
             including play data with on-ice coordinates and post-game
             details like first, second and third stars and details about
             shootouts.

             Note that the data returned is sizable, often over 30 000 lines.
        """
        self.feed = self.create_game_element("feed/live")
        self.feed.get_data()

    def get_content(self):
        """Get data from the content endpoint and store in the content property.

             Complex endpoint returning multiple types
             of media relating to the game including videos of shots,
             goals and saves.
        """
        self.content = self.create_game_element("content")
        self.content.get_data()
