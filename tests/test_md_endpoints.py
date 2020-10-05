import unittest
from nhlapip.md_endpoints import *
from nhlapip.const import NHLAPI_BASEURL

class TestGameTypesMd(unittest.TestCase):

    def test_game_types_md_constructor(self):
       game_types = GameTypesMd()
       self.assertEqual(game_types.url, NHLAPI_BASEURL + "gameTypes")
       self.assertEqual(game_types.endpoint, "gameTypes")
       self.assertEqual(game_types.suffixes, None)
       self.assertEqual(game_types.data, None)

    def test_game_types_md_getdata(self):
       game_types = GameTypesMd()
       game_types.get_data()
       self.assertIsInstance(game_types.data, list)


class TestGameStatusMd(unittest.TestCase):

    def test_game_statuses_md_constructor(self):
       game_statuses = GameStatusMd()
       self.assertEqual(game_statuses.url, NHLAPI_BASEURL + "gameStatus")
       self.assertEqual(game_statuses.endpoint, "gameStatus")
       self.assertEqual(game_statuses.suffixes, None)
       self.assertEqual(game_statuses.data, None)

    def test_game_statuses_md_getdata(self):
       game_statuses = GameStatusMd()
       game_statuses.get_data()
       self.assertIsInstance(game_statuses.data, list)


class TestPlayTypesMd(unittest.TestCase):

    def test_play_types_md_constructor(self):
       play_types = PlayTypesMd()
       self.assertEqual(play_types.url, NHLAPI_BASEURL + "playTypes")
       self.assertEqual(play_types.endpoint, "playTypes")
       self.assertEqual(play_types.suffixes, None)
       self.assertEqual(play_types.data, None)

    def test_play_types_md_getdata(self):
       play_types = PlayTypesMd()
       play_types.get_data()
       self.assertIsInstance(play_types.data, list)


class TestTournamentTypesMd(unittest.TestCase):

    def test_tournament_types_md_constructor(self):
       tournament_types = TournamentTypesMd()
       self.assertEqual(tournament_types.url, NHLAPI_BASEURL + "tournamentTypes")
       self.assertEqual(tournament_types.endpoint, "tournamentTypes")
       self.assertEqual(tournament_types.suffixes, None)
       self.assertEqual(tournament_types.data, None)

    def test_tournament_types_md_getdata(self):
       tournament_types = TournamentTypesMd()
       tournament_types.get_data()
       self.assertIsInstance(tournament_types.data, list)


class TestStandingsTypesMd(unittest.TestCase):

    def test_standings_types_md_constructor(self):
       standings_types = StandingsTypesMd()
       self.assertEqual(standings_types.url, NHLAPI_BASEURL + "standingsTypes")
       self.assertEqual(standings_types.endpoint, "standingsTypes")
       self.assertEqual(standings_types.suffixes, None)
       self.assertEqual(standings_types.data, None)

    def test_standings_types_md_getdata(self):
       standings_types = StandingsTypesMd()
       standings_types.get_data()
       self.assertIsInstance(standings_types.data, list)


class TestStatTypesMd(unittest.TestCase):

    def test_stat_types_md_constructor(self):
       stat_types = StatTypesMd()
       self.assertEqual(stat_types.url, NHLAPI_BASEURL + "statTypes")
       self.assertEqual(stat_types.endpoint, "statTypes")
       self.assertEqual(stat_types.suffixes, None)
       self.assertEqual(stat_types.data, None)

    def test_stat_types_md_getdata(self):
       stat_types = StatTypesMd()
       stat_types.get_data()
       self.assertIsInstance(stat_types.data, list)


class TestEventTypesMd(unittest.TestCase):

    def test_event_types_md_constructor(self):
       event_types = EventTypesMd()
       self.assertEqual(event_types.url, NHLAPI_BASEURL + "eventTypes")
       self.assertEqual(event_types.endpoint, "eventTypes")
       self.assertEqual(event_types.suffixes, None)
       self.assertEqual(event_types.data, None)

    def test_event_types_md_getdata(self):
       event_types = EventTypesMd()
       event_types.get_data()
       self.assertIsInstance(event_types.data, list)
