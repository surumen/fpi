import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.scrapers.whoscored import _BROWSER_OPTIONS
from app.utils import change_empty_df_values
from app.models.common.player_stats import DEFENSIVE_STATS


_PLAYERS_TABLE_ROW_SELECTOR = '#statistics-table-defensive #player-table-statistics-body tr'
_PLAYERS_TABLE_STATS_SELECTOR = '#team-squad-stats-options .in-squad-detailed-view'


def crawl_player_defensive_stats(team_id: int, api_delay_term=5):
    """
    crawling player defensive data

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
    _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_STATS_SELECTOR)[0].find_elements(
        By.CSS_SELECTOR, 'a')[0].click()

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    player_defensive_df = pd.DataFrame(columns=DEFENSIVE_STATS)

    # get players data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_ROW_SELECTOR)
    for element in elements:

        # player name
        name = element.find_elements(By.CSS_SELECTOR, 'td')[0].find_elements(By.CSS_SELECTOR, 'a')[0].find_elements(
            By.CSS_SELECTOR, 'span')[0].text

        player_dict = {
            'name': name,
            'tackles_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[6].text,
            'interceptions_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[7].text,
            'fouls_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[8].text,
            'clearances_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[10].text,
            'dribbled_past_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[11].text,
            'blocks_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[12].text,
            'own_goals': element.find_elements(By.CSS_SELECTOR, 'td')[13].text,
        }

        player_defensive_df.loc[len(player_defensive_df)] = player_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(player_defensive_df)
