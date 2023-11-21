import os
import time
import pandas as pd
from functools import reduce
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models.team import Team
from app.scrapers.whoscored import _BROWSER_OPTIONS
from app.scrapers.whoscored.team import crawl_team_overall_stats, crawl_team_defensive_stats, \
    crawl_team_offensive_stats


_TEAMS_SELECTOR = '#teams option'
_WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
_PL_TEAMS_DATA = os.path.join(_WORKING_DIR, '/data/Premier League.csv')


def crawl_league_teams(url: str, api_delay_term=5):
    """
    get league teams info: team_name, team_id

    parameter ---------------------------------------------------------------
    url : (str) base url
    api_delay_term = (optional) 5

    return ------------------------------------------------------------------
    dict
    """

    # connect driver
    _WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # make pandas dataframe
    league_teams = list(dict)

    # extract team data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _TEAMS_SELECTOR)
    for el in elements:
        team_name = el.text
        team_id = el.get_attribute('value').split('/')[2]
        league_teams.append({
            'team_id': team_id,
            'team_name': team_name
        })

    # close driver
    _WEB_DRIVER.close()

    return league_teams


def get_league_stats_by_team(league_name: str,
                             league_data: str = _PL_TEAMS_DATA
                             ) -> pd.DataFrame:
    df = pd.DataFrame(columns=[
        'team_name', 'total_games', 'goals', 'yellow', 'red',
        'ball_possession', 'pass_accuracy', 'aerial_duels_won_per_game',
        'rating', 'shots_allowed_per_game', 'tackles_per_game',
        'interceptions_per_game', 'fouls_conceded_per_game',
        'offsides_won_per_game', 'shots_per_game', 'shots_on_target_per_game',
        'dribbles_completed_per_game', 'fouls_won_per_game'
    ])
    league_teams_df = pd.read_csv(league_data)

    for idx, row in league_teams_df.iterrows():
        # execute team data crawling functions
        overall_df = crawl_team_overall_stats(int(row.team_id))
        defensive_df = crawl_team_defensive_stats(int(row.team_id))
        offensive_df = crawl_team_offensive_stats(int(row.team_id))

        # merge dataframes
        team_df = reduce(lambda x, y: pd.merge(x, y, on='league_name', how='outer'),
                         [overall_df, defensive_df, offensive_df])

        league_row = team_df.loc[team_df['league_name'] == league_name].to_dict('records')
        if len(league_row) > 0:
            league_row[0]['team_name'] = row.team_name
            df.loc[len(df)] = league_row[0]

    return df
