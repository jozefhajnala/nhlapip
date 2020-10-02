from nhlapip.player import Player
from nhlapip.game import Game
from nhlapip.team import Team
from nhlapip.tournament import Tournament
from nhlapip.schedule import Schedule
from nhlapip.standings import Standings
from nhlapip.md_endpoints import *
from nhlapip.minor_endpoints import *
import pandas as pd

# Standings
standings = Standings()
print(pd.json_normalize(standings.get_data()))

standings = Standings(season="19931994")
print(pd.json_normalize(standings.get_data()))

standings = Standings(season="19931994", standingsType="byDivision")
print(pd.json_normalize(standings.get_data()))

standings = Standings(season="19931994", expand="standings.record")
print(pd.json_normalize(standings.get_data()))


# Schedules
schedule = Schedule()
print(pd.json_normalize(schedule.get_data()))

schedule = Schedule(season="19931994")
print(pd.json_normalize(schedule.get_data()))

# List of matches per team
schedule = Schedule(season="19931994", teamId="1", expand="schedule.linescore")
print(pd.json_normalize(schedule.get_data()))

# Details on games on a particular date
schedule = Schedule(startDate="2018-01-02", endDate="2018-01-02")
schedule.get_data()
print(pd.json_normalize(schedule.data[0]["games"]))


# Tournaments
tournament = Tournament(type="playoffs")
print(pd.json_normalize(tournament.get_data()))

tournament = Tournament(type="playoffs", season="19961997")
print(pd.json_normalize(tournament.get_data()))

tournament = Tournament(type="playoffs", season="19961997", expand="round.series")
tournament.get_data()
print(pd.json_normalize(tournament.data["rounds"]))

# One team
team = Team(1)

team.get_data()
print(pd.json_normalize(team.data))

team.get_roster()
print(pd.json_normalize(team.roster))

team.get_roster(season="19931994")
print(pd.json_normalize(team.roster))

team.get_schedule_previous()
print(pd.json_normalize(team.schedulePrevious))

team.get_stats()
print(pd.json_normalize(team.stats))

team.get_stats(season="19931994")
print(pd.json_normalize(team.stats))


# All Teams
all_teams = Team()
all_teams.get_data()
print(pd.json_normalize(all_teams.data))

all_teams.get_roster()
print(pd.json_normalize(all_teams.roster))

all_teams.get_roster(season="19931994")
print(pd.json_normalize(all_teams.roster))

all_teams.get_schedule_previous()
print(pd.json_normalize(all_teams.schedulePrevious))

all_teams.get_schedule_next()
print(pd.json_normalize(all_teams.scheduleNext))


# Player Data
sakic = Player('8451101')
sakic.get_data()
print(pd.json_normalize(sakic.data))

# Player's Seasons Statistics
sakic.get_stats_allseasons()
groups = ['sequenceNumber', 'season']
aggregations = {'stat.goals': 'sum', 'stat.assists': 'sum'}
print(pd.json_normalize(sakic.stats).groupby(groups).agg(aggregations))

# Game Details
game = Game("2017010001")
game.get_linescore()
print(pd.json_normalize(game.linescore.data["periods"]))
game.get_feed()
plays = game.feed.data["liveData"]["plays"]["allPlays"]
print(pd.json_normalize(plays))

# Game Types metadata
game_types = GameTypesMd()
game_types.get_data()
print(pd.json_normalize(game_types.data))

# Game Statuses metadata
game_statues = GameStatusesMd()
game_statues.get_data()
print(pd.json_normalize(game_statues.data))

# Play Types metadata
play_types = PlayTypesMd()
play_types.get_data()
print(pd.json_normalize(play_types.data))

# Conferences
conferences = Conferences()
conferences.get_data()
print(pd.json_normalize(conferences.data))

# Divisions
divisions = Divisions()
divisions.get_data()
print(pd.json_normalize(divisions.data))

# Drafts
drafts = Drafts(2019)
drafts.get_data()
print(pd.json_normalize(drafts.data))

# All Seasons
seasons = Seasons()
seasons.get_data()
print(pd.json_normalize(seasons.data))

# Season 1999/2000
print(pd.json_normalize(Seasons("19992000").get_data()))

# All Awards
awards = Awards()
print(pd.json_normalize(awards.get_data()))

# All venues
venues = Venues()
print(pd.json_normalize(venues.get_data()))

# Draft Prospects
draft_prospects = DraftProspects()
print(pd.json_normalize(draft_prospects.get_data()))
