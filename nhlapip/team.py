"""Implementation of the teams endpoint."""
from .url import NhlUrl

class Team(NhlUrl):
    """Team

    Args:
        NhlUrl: NhlUrl to be enriched with Team-specific elements
    """

    def __init__(self, team_id = None):
        super().__init__(endpoint = "teams", suffixes = team_id)
        self.team_id = team_id
        self.data = None
        self.stats = None
        self.roster = None
        self.schedule_next = None
        self.schedule_previous = None

    def is_one_team(self):
        """Check whether team_id is a single string or integer."""
        return isinstance(self.team_id, int) | isinstance(self.team_id, str)

    def get_team_url(self, expand, season = None):
        "Construct a team url with optional expand and season parameters"
        pars = ["expand=" + expand]
        if season is not None:
            pars.append("season=" + season)
        return NhlUrl(endpoint = "teams", suffixes = self.team_id, params = pars)

    def get_data(self):
        self.data = super().get_data()["teams"]
        return self.data

    def get_roster(self, season = None):
        """Provides rosters for the team"""

        roster_url = self.get_team_url(expand = "team.roster", season = season)
        roster_data = roster_url.get_data()["teams"]

        # For just one team, extract the roster directly
        if self.is_one_team():
            roster_data = roster_data[0]["roster"]["roster"]
        self.roster = roster_data
        return roster_data

    def get_schedule_previous(self):
        """Provides past schedule for the team"""
        sch_prev_url = self.get_team_url(expand = "team.schedule.previous")
        sch_prev_data = sch_prev_url.get_data()["teams"]

        # For just one team, extract the schedule directly
        if self.is_one_team():
            sch_prev_data = sch_prev_data[0]["previousGameSchedule"]["dates"]
        self.schedule_previous = sch_prev_data
        return sch_prev_data

    def get_schedule_next(self):
        """Provides future schedule for the team"""
        sch_next_url = self.get_team_url(expand = "team.schedule.next")
        sch_next_data = sch_next_url.get_data()["teams"]

        # For just one team, extract the roster directly
        if self.is_one_team():
            sch_next_data = sch_next_data[0]["nextGameSchedule"]["dates"]
        self.schedule_next = sch_next_data
        return sch_next_data

    def get_stats(self, season = None):
        """Provides the team.stats endpoint for the team and a specific season

        Args:
            season (str, optional): Seasons definition in the format `"YYYYZZZZ"`,
              where `ZZZZ = YYYY + 1`, e.g. `"19951996"` for season 1995/1996.
              Defaults to None.

        Returns:
            object: Data retrieved from the API
        """
        stats_url = self.get_team_url(expand = "team.stats", season = season)
        stats_data = stats_url.get_data()["teams"]

        # For just one team, extract the roster directly
        if self.is_one_team():
            stats_data = stats_data[0]["teamStats"]
        self.stats = stats_data
        return stats_data
