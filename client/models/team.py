from typing import List
from client.models.common.category import RecordCategory
from client.models.league import League


class Team:
    """A team."""

    def __init__(self, name, team_id, leagues: List[League] = None) -> None:
        self.name = name
        self.team_id = team_id
        self.leagues = leagues

    def __repr__(self):
        return '{name}'.format(name=self.name)


class TeamSummary:
    """Team stats summary."""

    def __init__(self, team_id, team_name, leagues: List[League]):
        self.team_id = team_id
        self.team_name = team_name
        self.overall_record = TeamLeagueRecord(
            team_id=team_id,
            team_name=team_name,
            category=RecordCategory.OVERALL
        )
        self.home_overall_record = TeamLeagueRecord(
            team_id=team_id,
            team_name=team_name,
            category=RecordCategory.HOME
        )
        self.away_overall_record = TeamLeagueRecord(
            team_id=team_id,
            team_name=team_name,
            category=RecordCategory.AWAY
        )

        for l in leagues:
            setattr(self, 'overall_{league_name}_record'.format(league_name=l.league_name),
                    TeamLeagueRecord(
                        team_id=self.team_id,
                        team_name=self.team_name,
                        league_id=l.league_id,
                        category=RecordCategory.OVERALL
                    ))
            setattr(self, 'home_{league_name}_record'.format(league_name=l.league_name),
                    TeamLeagueRecord(
                        team_id=self.team_id,
                        team_name=self.team_name,
                        league_id=l.league_id,
                        category=RecordCategory.HOME
                    ))
            setattr(self, 'away_{league_name}_record'.format(league_name=l.league_name),
                    TeamLeagueRecord(
                        team_id=self.team_id,
                        team_name=self.team_name,
                        league_id=l.league_id,
                        category=RecordCategory.AWAY
                    ))

    def set_overall_record(self, data: dict):
        self.overall_record.set_record(data)

    def set_home_overall_record(self, data: dict):
        self.home_overall_record.set_record(data)

    def set_away_overall_record(self, data: dict):
        self.away_overall_record.set_record(data)

    def set_league_overall_record(self, l: League, data: dict):
        getattr(self, 'overall_{league_name}_record'.format(league_name=l.league_name)).set_record(data)

    def set_league_home_record(self, l: League, data: dict):
        getattr(self, 'home_{league_name}_record'.format(league_name=l.league_name)).set_record(data)

    def set_league_away_record(self, l: League, data: dict):
        getattr(self, 'away_{league_name}_record'.format(league_name=l.league_name)).set_record(data)


class TeamLeagueRecord:

    def __init__(self, team_id, team_name, category: RecordCategory, league_id=None):
        self.team_id = team_id
        self.team_name = team_name
        self.league_id = league_id
        self.category = category

        # summary
        self.total_games = None
        self.rating = None

        # offense
        self.goals_scored = None
        self.shots_per_game = None
        self.shots_on_target_per_game = None
        self.dribbles_per_game = None
        self.fouls_won_per_game = None

        # defense
        self.goals_conceded = None
        self.shots_allowed_per_game = None
        self.tackles_per_game = None
        self.interceptions_per_game = None
        self.fouls_conceded_per_game = None
        self.offsides_won_per_game = None

    def set_record(self, data: dict):
        self.set_summary(data)
        self.set_offensive_stats(data)
        self.set_defensive_stats(data)

    def set_summary(self, data: dict):
        self.total_games = data.get('total_games', 0)
        self.rating = data.get('rating', 0)

    def set_offensive_stats(self, data: dict):
        self.goals_scored = data.get('goals_scored', 0)
        self.shots_per_game = data.get('shots_per_game', 0)
        self.shots_on_target_per_game = data.get('shots_on_target_per_game', 0)
        self.dribbles_per_game = data.get('dribbles_per_game', 0)
        self.fouls_won_per_game = data.get('fouls_won_per_game', 0)

    def set_defensive_stats(self, data: dict):
        self.goals_conceded = data.get('goals_conceded', 0)
        self.shots_allowed_per_game = data.get('shots_allowed_per_game', 0)
        self.tackles_per_game = data.get('tackles_per_game', 0)
        self.interceptions_per_game = data.get('interceptions_per_game', 0)
        self.fouls_conceded_per_game = data.get('fouls_conceded_per_game', 0)
        self.offsides_won_per_game = data.get('offsides_won_per_game', 0)
