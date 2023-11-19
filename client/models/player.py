import datetime
from typing import List
from client.models.common.player_stats import OVERALL_STATS, OFFENSIVE_STATS, PASSING_STATS, DEFENSIVE_STATS


_PLAYER_STATS = OVERALL_STATS + OFFENSIVE_STATS + PASSING_STATS + DEFENSIVE_STATS


class Player:
    """A player."""

    def __init__(self,
                 name: str,
                 team_id: int,
                 full_name: str,
                 short_name: str,
                 image: str,
                 height: int,
                 weight: int,
                 positions: str,
                 dob: str,
                 transfer_value: str,
                 wage: str,
                 preferred_foot: str,
                 club_name: str,
                 club_logo: str,
                 club_kit_number: str,
                 club_joined: str,
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
        self.date_of_birth = dob
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

    def set_stats(self, data: dict):
        for stat, value in data.items():
            setattr(self, '{stat}'.format(stat=stat), value)

    def get_stat(self, stat):
        return getattr(self, stat)

    def __repr__(self):
        return '{name}, {team}-{position}'.format(name=self.name, team=self.club_name, position=self.positions)
