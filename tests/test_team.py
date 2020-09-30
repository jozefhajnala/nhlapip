import unittest
from nhlapip.url import NhlUrl
from nhlapip.team import Team
from nhlapip.const import NHLAPI_BASEURL

class TestTeam(unittest.TestCase):

    def test_team_constructor_all_teams(self):
       team = Team()
       self.assertEqual(team.url, NHLAPI_BASEURL + "teams")
       self.assertEqual(team.endpoint, "teams")
       self.assertEqual(team.suffixes, None)
       self.assertEqual(team.data, None)

    def test_team_constructor_one_team(self):
       team = Team(1)
       self.assertEqual(team.url, NHLAPI_BASEURL + "teams/1")
       self.assertEqual(team.endpoint, "teams")
       self.assertEqual(team.suffixes, 1)
       self.assertEqual(team.data, None)

    def test_is_one_team(self):
       self.assertEqual(Team(1).is_one_team(), True)
       self.assertEqual(Team().is_one_team(), False)

    def test_get_team_url_roster(self):
       self.assertEqual(
           Team(1).get_team_url(expand="team.roster", season=None).url,
           NHLAPI_BASEURL + "teams/1?expand=team.roster"
        )
       self.assertEqual(
           Team(1).get_team_url(expand="team.roster", season="19931994").url,
           NHLAPI_BASEURL + "teams/1?expand=team.roster&season=19931994"
        )

    def test_get_team_url_roster_all_teams(self):
       self.assertEqual(
           Team().get_team_url(expand="team.roster", season=None).url,
           NHLAPI_BASEURL + "teams?expand=team.roster"
        )
       self.assertEqual(
           Team().get_team_url(expand="team.roster", season="19931994").url,
           NHLAPI_BASEURL + "teams?expand=team.roster&season=19931994"
        )

    def test_get_team_url_schedule_previous(self):
       self.assertEqual(
           Team(1).get_team_url(expand="team.schedule.previous").url,
           NHLAPI_BASEURL + "teams/1?expand=team.schedule.previous"
        )

    def test_get_team_url_schedule_previous_all_teams(self):
       self.assertEqual(
           Team().get_team_url(expand="team.schedule.previous").url,
           NHLAPI_BASEURL + "teams?expand=team.schedule.previous"
        )

    def test_get_team_url_schedule_next(self):
       self.assertEqual(
           Team(1).get_team_url(expand="team.schedule.next").url,
           NHLAPI_BASEURL + "teams/1?expand=team.schedule.next"
        )

    def test_get_team_url_schedule_next_all_teams(self):
       self.assertEqual(
           Team().get_team_url(expand="team.schedule.next").url,
           NHLAPI_BASEURL + "teams?expand=team.schedule.next"
        )

    def test_get_team_url_stats(self):
       self.assertEqual(
           Team(1).get_team_url(expand="team.stats", season=None).url,
           NHLAPI_BASEURL + "teams/1?expand=team.stats"
        )

       self.assertEqual(
           Team(1).get_team_url(expand="team.stats", season="19931994").url,
           NHLAPI_BASEURL + "teams/1?expand=team.stats&season=19931994"
        )

    def test_get_team_url_stats_all_teams(self):
       self.assertEqual(
           Team().get_team_url(expand="team.stats", season=None).url,
           NHLAPI_BASEURL + "teams?expand=team.stats"
        )

       self.assertEqual(
           Team().get_team_url(expand="team.stats", season="19931994").url,
           NHLAPI_BASEURL + "teams?expand=team.stats&season=19931994"
        )
