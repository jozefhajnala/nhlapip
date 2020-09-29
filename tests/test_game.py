import unittest
from nhlapip.url import NhlUrl
from nhlapip.game import Game
from nhlapip.const import NHLAPI_BASEURL

class TestGame(unittest.TestCase):

    def test_game_constructor(self):
       gm = Game("2017010001")
       self.assertEqual(gm.url, NHLAPI_BASEURL + "game/2017010001")
       self.assertEqual(gm.endpoint, "game")
       self.assertEqual(gm.suffixes, "2017010001")
       self.assertEqual(gm.data, None)

    def test_create_game_element(self):
        gm = Game("2017010001")
        self.assertDictEqual(
            vars(gm.create_game_element("boxscore")),
            vars(NhlUrl(endpoint = "game", suffixes = ["2017010001", "boxscore"]))
        )
