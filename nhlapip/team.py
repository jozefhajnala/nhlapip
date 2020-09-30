from .url import NhlUrl
from .const import NHLAPI_BASEURL

class Team(NhlUrl):

    def __init__(self, id = None):
        super().__init__(endpoint = "teams", suffixes = id)
        self.id = id
        self.data = None
        self.stats = None
        self.roster = None
        self.scheduleNext = None
        self.schedulePrevious = None

    def is_one_team(self):
        return isinstance(self.id, int) | isinstance(self.id, str)

    def get_team_url(self, expand, season = None):
        pars = ["expand=" + expand]
        if season is not None:
            pars.append("season=" + season)
        return NhlUrl(endpoint = "teams", suffixes = self.id, params = pars)

    def get_data(self):
         self.data = super().get_data()["teams"]
         return self.data

    def get_roster(self, season = None):
        rosterUrl = self.get_team_url(expand = "team.roster", season = season)
        rosterData = rosterUrl.get_data()["teams"]

        # For just one team, extract the roster directly
        if (self.is_one_team()):
            rosterData = rosterData[0]["roster"]["roster"]
        self.roster = rosterData
        return rosterData

    def get_schedule_previous(self):
        schPrevUrl = self.get_team_url(expand = "team.schedule.previous")
        schPrevData = schPrevUrl.get_data()["teams"]

        # For just one team, extract the schedule directly
        if (self.is_one_team()):
            schPrevData = schPrevData[0]["previousGameSchedule"]["dates"]
        self.schedulePrevious = schPrevData
        return schPrevData

    def get_schedule_next(self):
        schNextUrl = self.get_team_url(expand = "team.schedule.next")
        schNextData = schNextUrl.get_data()["teams"]

        # For just one team, extract the roster directly
        if (self.is_one_team()):
            schNextData = schNextData[0]["nextGameSchedule"]["dates"]
        self.scheduleNext = schNextData
        return schNextData

    def get_stats(self, season = None):
        statsUrl = self.get_team_url(expand = "team.stats", season = season)
        statsData = statsUrl.get_data()["teams"]

        # For just one team, extract the roster directly
        if (self.is_one_team()):
            statsData = statsData[0]["teamStats"]
        self.stats = statsData
        return statsData
