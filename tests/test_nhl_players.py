import unittest
from nhlapip.nhl_players import Player
from nhlapip.const import NHLAPI_BASEURL

class TestConst(unittest.TestCase):

    def test_constructor(self):           
       self.assertEqual(Player("1").url.url, NHLAPI_BASEURL + "people/1")
