import unittest
from nhlapip.url import NhlUrl
from nhlapip.standings import Standings
from nhlapip.const import NHLAPI_BASEURL

class TestStandings(unittest.TestCase):

    def test_standings_constructor(self):
        standings = Standings()
        self.assertEqual(standings.url, NHLAPI_BASEURL + "standings")
        self.assertEqual(standings.endpoint, "standings")
        self.assertEqual(standings.suffixes, None)
        self.assertEqual(standings.params, None)
        self.assertEqual(standings.data, None)

    def test_standings_constructor_with_season(self):
         standings = Standings(season="19931994")
         self.assertEqual(standings.url, NHLAPI_BASEURL + "standings?season=19931994")
         self.assertEqual(standings.endpoint, "standings")
         self.assertEqual(standings.suffixes, None)
         self.assertEqual(standings.params, ["season=19931994"])
         self.assertEqual(standings.data, None)

    def test_standings_constructor_with_standingstype(self):
         standings = Standings(standingsType="byDivision")
         self.assertEqual(standings.url, NHLAPI_BASEURL + "standings?standingsType=byDivision")
         self.assertEqual(standings.endpoint, "standings")
         self.assertEqual(standings.suffixes, None)
         self.assertEqual(standings.params, ["standingsType=byDivision"])
         self.assertEqual(standings.data, None)
