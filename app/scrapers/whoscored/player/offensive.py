import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.scrapers.whoscored import _BROWSER_OPTIONS
from app.utils import change_empty_df_values
from app.models.common.player_stats import OVERALL_STATS, OFFENSIVE_STATS, PASSING_STATS, DEFENSIVE_STATS


_PLAYERS_TABLE_ROW_SELECTOR = '#statistics-table-offensive #player-table-statistics-body tr'
_PLAYERS_TABLE_STATS_SELECTOR = '#team-squad-stats-options .in-squad-detailed-view'


def crawl_player_offensive_stats(team_id: int, api_delay_term=5):
    """
    crawling player offensive data

    parameter -------------------------------------------------------------------
    team_id : (int or str) team_id
    api_delay_term = (optional) 5

    return ----------------------------------------------------------------------
    dict: OFFENSIVE_STATS
    """

    # connect web driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # click event for getting data
    _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_STATS_SELECTOR)[1].find_elements(
        By.CSS_SELECTOR, 'a')[0].click()

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    player_offensive_df = pd.DataFrame(columns=OFFENSIVE_STATS)

    # get players data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_ROW_SELECTOR)
    for element in elements:

        # player name
        name = element.find_elements(By.CSS_SELECTOR, 'td')[0].find_elements(By.CSS_SELECTOR, 'a')[0].find_elements(
            By.CSS_SELECTOR, 'span')[0].text

        player_dict = {
            'name': name,
            'goals': element.find_elements(By.CSS_SELECTOR, 'td')[6].text,
            'assists': element.find_elements(By.CSS_SELECTOR, 'td')[7].text,
            'shots_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[8].text,
            'dribbles_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[10].text,
            'fouled_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[11].text,
            'offside_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[12].text,
            'possession_lost_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[13].text,
            'bad_touch_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[14].text,
        }

        player_offensive_df.loc[len(player_offensive_df)] = player_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(player_offensive_df)
