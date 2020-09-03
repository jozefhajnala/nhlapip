from nhlapip.nhl_player import Player
import pandas as pd

sakic = Player('8451101')
sakic.get_data()
print(pd.json_normalize(sakic.data))

sakic.get_stats_allseasons()
groups = ['sequenceNumber', 'season']
aggregations = {'stat.goals': 'sum', 'stat.assists': 'sum'}
print(pd.json_normalize(sakic.stats).groupby(groups).agg(aggregations))
