from nhlapip.nhl_player import Player
from nhlapip.nhl_game import Game
import pandas as pd

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
print(pd.json_normalize(game.feed.data["liveData"]["plays"]["allPlays"]))
