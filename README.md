# NHLAPI for Python

![Install and Test](https://github.com/jozefhajnala/nhlapip/workflows/ci/badge.svg)
![Pandas Showcase](https://github.com/jozefhajnala/nhlapip/workflows/pandas_showcase/badge.svg)
![CLI Showcase](https://github.com/jozefhajnala/nhlapip/workflows/cli_showcase/badge.svg)

### Major endpoints

- [ ] Teams
    - [ ] Team Metadata ``
    - [ ] Team Rosters ``
    - [ ] Team Schedules ``
    - [ ] Team Stats ``
    
- [x] People (`Player`)
    - [x] Players metadata `Player.get_data()`
    - [x] Players all season stats `Player.get_stats_allseasons()`

- [x] Games (`Game`)
    - [x] Games content `Game.get_content()`
    - [x] Games full live feed `Game.get_feed()`
    - [x] Games box score info `Game.get_boxscore()`
    - [x] Games line score info `Game.get_linescore()`

- [ ] Tournaments
    - [ ] Playoffs `nhl_tournaments_playoffs()`
    - [ ] Olympics `nhl_tournaments_olympics()`
    - [ ] World Cups `nhl_tournaments_worldcups()`
    
- [ ] Schedule
    - [ ] Generic API with all parameters `nhl_schedule()`
    - [ ] Today `nhl_schedule_today()`
    - [ ] Custom seasons `nhl_schedule_seasons()`
    - [ ] Custom date ranges `nhl_schedule_date_range()`

- [ ] Standings `nhl_standings()`

### Minor endpoints

- [x] Divisions `nhl_divisions()`
- [x] Conferences `nhl_conferences()`
- [x] Drafts `nhl_drafts()`
- [x] Seasons `nhl_seasons()`
- [x] Awards `nhl_awards()`
- [x] Venues `nhl_venues()`
- [x] Draft prospects `nhl_draft_prospects()`

### Metadata endpoints

- [x] Game Types `GameTypesMd()`
- [x] Game Statuses `GameStatusesMd()`
- [x] Play Types `PlayTypesMd()`
- [x] Tournament Types `TournamentTypesMd()`
- [x] Standings Types `StandingsTypesMd()`
- [x] Stats Types `StatTypesMd()`
- [x] Event Types `EventTypesMd()`


## Acknowledgments

Thanks go to Drew Hynes for documenting this so well on [GitLab](https://gitlab.com/dword4/nhlapi/blob/master/stats-api.md).


## Copyright message

> NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2020. All Rights Reserved.
