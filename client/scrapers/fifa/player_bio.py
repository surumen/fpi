import pandas as pd
from client.models.player import Player

_FIFA_PLAYER_DATA = './data/player_data_full.csv'

_IMAGE_URL = 'https://cdn.futbin.com/content/fifa24/img/players/{profile_id}.png'


def get_player_by_name(player_name='', csv_data: str = _FIFA_PLAYER_DATA):
    df: pd.DataFrame = pd.read_csv(csv_data)
    records = df.loc[df['name'] == player_name].to_dict('records')
    row = records[0] if len(records) > 0 else {}
    player = Player(
        name=player_name,
        full_name=row.get('full_name', player_name),
        short_name=row.get('short_name', player_name),
        image=_IMAGE_URL.format(profile_id=row.get('fc_profile_id')) if 'fc_profile_id' in row else '',
        height=int(row.get('height', 0)),
        weight=int(row.get('weight', 0)),
        positions=row.get('positions'),
        dob=row.get('dob'),
        transfer_value=row.get('transfer_value'),
        wage=row.get('wage'),
        preferred_foot=row.get('preferred_foot'),
        club_name=row.get('club_name'),
        club_logo=row.get('club_logo'),
        club_kit_number=row.get('club_kit_number'),
        club_joined=row.get('club_joined'),
        club_contract_valid_until=row.get('club_contract_valid_until'),
        country_flag=row.get('country_flag'),
        fc_profile_id=row.get('fc_profile_id', None),
        fc_club_id=row.get('fc_club_id', None)
    )
    return player
