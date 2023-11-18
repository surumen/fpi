import datetime
from typing import List


_OVERALL_STATS = [
    'total_apps', 'starting_apps', 'sub_apps', 'mins_played',
]

_OFFENSIVE_STATS = [
    'goals', 'assists', 'shots_per_game', 'possession_lost', 'bad_touch',
]

_PASSING_STATS = [
    'pass_accuracy', 'passes_per_game', 'key_passes_per_game',
    'dribbles_per_game', 'fouls_won_per_game', 'offsides_per_game',
]

_DEFENSIVE_STATS = [
    'tackles_per_game', 'interceptions_per_game', 'clearances_per_game', 'blocks_per_game',
    'clearances_per_game', 'own_goals', 'dribbled_past'
]

_DISCIPLINE_STATS = [
    'fouls_conceded_per_game', 'yellow', 'red'
]

_PLAYER_STATS = _OVERALL_STATS + _OFFENSIVE_STATS + _PASSING_STATS + _DEFENSIVE_STATS + _DISCIPLINE_STATS


class Player:
    """A player."""

    def __init__(self,
                 name: str,
                 full_name: str,
                 short_name: str,
                 image: str,
                 height: int,
                 weight: int,
                 positions: List[str],
                 date_of_birth: datetime.date,
                 transfer_value: str,
                 wage: str,
                 preferred_foot: str,
                 club_name: str,
                 club_logo: str,
                 club_kit_number: int,
                 club_joined: datetime.date,
                 club_contract_valid_until: str,
                 country_flag: str,

                 fc_profile_id: int,
                 fc_club_id: int

                 ) -> None:
        self.name = name
        self.full_name = full_name
        self.short_name = short_name
        self.image = image
        self.height = height
        self.weight = weight
        self.positions = positions
        self.date_of_birth = date_of_birth
        self.transfer_value = transfer_value
        self.wage = wage
        self.preferred_foot = preferred_foot
        self.club_name = club_name
        self.club_logo = club_logo
        self.club_kit_number = club_kit_number
        self.club_joined = club_joined
        self.club_contract_valid_until = club_contract_valid_until
        self.country_flag = country_flag

        self.fc_profile_id = fc_profile_id
        self.fc_club_id = fc_club_id

        for stat in _PLAYER_STATS:
            setattr(self, '{stat}'.format(stat=stat), 0)

    def set_stats(self, data: dict, stats: List[str]):
        for stat in stats:
            setattr(self, '{stat}'.format(stat=stat), data.get(stat))

