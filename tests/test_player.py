import unittest
from nhlapip.player import Player
from nhlapip.const import NHLAPI_BASEURL

class TestPlayer(unittest.TestCase):

    def test_player_constructor(self):
       pl = Player("1")
       self.assertEqual(pl.url, NHLAPI_BASEURL + "people/1")
       self.assertEqual(pl.endpoint, "people")
       self.assertEqual(pl.suffixes, "1")
       self.assertEqual(pl.data, None)

    def test_player_getdata(self):
       pl = Player("8451101")
       dt = pl.get_data()
       self.assertEqual(dt["fullName"], "Joe Sakic")
       self.assertIsInstance(pl.data, dict)
       self.assertEqual(str(pl.data["id"]), pl.player_id)
       self.assertEqual(pl.data["fullName"], "Joe Sakic")

    def test_player_get_stats_allseasons(self):
       pl = Player("8451101")
       pl.get_stats_allseasons()
       self.assertIsInstance(pl.stats, list)

