import unittest
from nhlapip.url import NhlUrl
from nhlapip.tournament import Tournament
from nhlapip.const import NHLAPI_BASEURL

class TestTournament(unittest.TestCase):

    def test_tournament_constructor(self):
        tournament = Tournament(tournament_type = "playoffs")
        self.assertEqual(tournament.url, NHLAPI_BASEURL + "tournaments/playoffs")
        self.assertEqual(tournament.endpoint, "tournaments")
        self.assertEqual(tournament.suffixes, "playoffs")
        self.assertEqual(tournament.params, None)
        self.assertEqual(tournament.data, None)

    def test_tournament_constructor_with_expand(self):
        tournament = Tournament(tournament_type = "playoffs", expand = "round.series")
        self.assertEqual(tournament.url, NHLAPI_BASEURL + "tournaments/playoffs?expand=round.series")
        self.assertEqual(tournament.endpoint, "tournaments")
        self.assertEqual(tournament.suffixes, "playoffs")
        self.assertEqual(tournament.params, ["expand=round.series"])
        self.assertEqual(tournament.data, None)

    def test_tournament_constructor_with_season(self):
         tournament = Tournament(tournament_type = "playoffs", season = "19931994")
         self.assertEqual(tournament.url, NHLAPI_BASEURL + "tournaments/playoffs?season=19931994")
         self.assertEqual(tournament.endpoint, "tournaments")
         self.assertEqual(tournament.suffixes, "playoffs")
         self.assertEqual(tournament.params, ["season=19931994"])
         self.assertEqual(tournament.data, None)

    def test_tournament_constructor_with_expand_and_season(self):
         tournament = Tournament(tournament_type = "playoffs", expand = "round.series", season = "19931994")
         self.assertEqual(tournament.url, NHLAPI_BASEURL + "tournaments/playoffs?expand=round.series&season=19931994")
         self.assertEqual(tournament.endpoint, "tournaments")
         self.assertEqual(tournament.suffixes, "playoffs")
         self.assertEqual(tournament.params, ["expand=round.series", "season=19931994"])
         self.assertEqual(tournament.data, None)
