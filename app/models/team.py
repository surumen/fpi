from typing import List
from app.models.league import League
from app.models.common.team_stats import OVERALL_STATS, DEFENSIVE_STATS, PASSING_STATS, OFFENSIVE_STATS


_TEAM_STATS = OVERALL_STATS + DEFENSIVE_STATS + PASSING_STATS + OFFENSIVE_STATS


class Team:
    """A team."""

    def __init__(self,
                 team_name,
                 team_id,
                 leagues: List[League] = None) -> None:
        self.team_name = team_name
        self.team_id = team_id
        self.leagues = leagues

        for stat in _TEAM_STATS:
            setattr(self, '{stat}'.format(stat=stat), 0)

    def __repr__(self):
        return '{name}'.format(name=self.team_name)

    def set_stats(self, data: dict):
        for stat, value in data.items():
            setattr(self, '{stat}'.format(stat=stat), value)

    def set_home_stats(self, data: dict):
        for stat, value in data.items():
            setattr(self, 'home_{stat}'.format(stat=stat), value)

    def set_away_stats(self, data: dict):
        for stat, value in data.items():
            setattr(self, 'away_{stat}'.format(stat=stat), value)

    def set_league_stats(self, data: dict, league: League):
        for stat, value in data.items():
            setattr(self, '{league_name}_{stat}'.format(league_name=league.slug, stat=stat), value)

    def get_stat(self, stat):
        return getattr(self, stat)
