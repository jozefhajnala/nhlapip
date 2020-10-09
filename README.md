# nhlapip - Low-dependency NHL API interface for Python

![Install and Test](https://github.com/jozefhajnala/nhlapip/workflows/ci/badge.svg)
![Pandas Showcase](https://github.com/jozefhajnala/nhlapip/workflows/pandas_showcase/badge.svg)
![CLI Showcase](https://github.com/jozefhajnala/nhlapip/workflows/cli_showcase/badge.svg)
![Lint](https://github.com/jozefhajnala/nhlapip/workflows/lint/badge.svg)


## Installation

Install nhlapip with pip:

```bash
pip install nhlapip
```

## Usage

### With Python

The API is exposed via endpoint-based classes. See [below for a full list of endpoints](#currently-implemented-endpoints). Some quick examples:

```python
# Player Data for Joe Sakic
from nhlapip.player import Player
sakic = Player('8451101')
print(sakic.get_data())

# Player's All Seasons Statistics
print(sakic.get_stats_allseasons())

# All Teams' Rosters
from nhlapip.team import Team
all_teams = Team()
print(all_teams.get_roster())
```

Many usage examples can be found in the [Pandas showcase](ci/pandas_showcase.py) that shows data retrieval for many endpoints.

### Command line interface (CLI)

A very simple CLI is also available. This is still in active development. Some examples:

```bash
echo '\n\Get data nhlapip for 1 player:\n'
nhlapip Player 8451101

echo '\n\nGet data for 2 Teams :\n'
nhlapip Team 1 2
```

Many usage examples can be found in the [CLI showcase](ci/cli_showcase.sh) that shows CLI data retrieval for many endpoints.


## Currently implemented endpoints

### Major endpoints

- [x] Teams
    - [x] Team Metadata `Team().get_data()`
    - [x] Team Rosters `Team().get_roster()`
    - [x] Team Schedules `Team().get_schedule_next()`, `Team().get_schedule_previous()`
    - [x] Team Stats `Team().get_stats()`

- [x] People (`Player`)
    - [x] Players metadata `Player.get_data()`
    - [x] Players all season stats `Player.get_stats_allseasons()`

- [x] Games (`Game`)
    - [x] Games content `Game.get_content()`
    - [x] Games full live feed `Game.get_feed()`
    - [x] Games box score info `Game.get_boxscore()`
    - [x] Games line score info `Game.get_linescore()`

- [x] Tournaments
    - [x] Playoffs `Tournament("playoffs")`
    - [x] Olympics `Tournament("olympics")`
    - [x] World Cups `Tournament("worldcup")`

- [x] Schedule
    - [x] Generic API with all parameters `Schedule()`

- [x] Standings `Standings()`

### Minor endpoints

- [x] Divisions `Divisions()`
- [x] Conferences `Conferences()`
- [x] Drafts `Drafts()`
- [x] Seasons `Seasons()`
- [x] Awards `Awards()`
- [x] Venues `Venues()`
- [x] Draft prospects `DraftProspects()`

### Metadata endpoints

- [x] Game Types `GameTypesMd()`
- [x] Game Statuses `GameStatusMd()`
- [x] Play Types `PlayTypesMd()`
- [x] Tournament Types `TournamentTypesMd()`
- [x] Standings Types `StandingsTypesMd()`
- [x] Stats Types `StatTypesMd()`
- [x] Event Types `EventTypesMd()`


## NHL API data for R users

This package is a Python port of a more mature and feature-rich R package `{nhlapi}`. If you are an R user, please check the package out on [GitHub](https://github.com/jozefhajnala/nhlapi) and on [CRAN](https://cran.r-project.org/package=nhlapi).


## Acknowledgments

Thanks go to Drew Hynes for documenting this so well on [GitLab](https://gitlab.com/dword4/nhlapi/blob/master/stats-api.md).


## Copyright message

> NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2020. All Rights Reserved.
