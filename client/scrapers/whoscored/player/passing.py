import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from client.scrapers.whoscored import _BROWSER_OPTIONS
from client.utils import change_empty_df_values
from client.models.common.player_stats import PASSING_STATS


_PLAYERS_TABLE_ROW_SELECTOR = '#statistics-table-passing #player-table-statistics-body tr'
_PLAYERS_TABLE_STATS_SELECTOR = '#team-squad-stats-options .in-squad-detailed-view'


def crawl_player_passing_stats(team_id: int, api_delay_term=5):
    """
    crawling player passing data

    parameter -------------------------------------------------------------------
    team_id : (int or str) team_id
    api_delay_term = (optional) 5

    return ----------------------------------------------------------------------
    dict: PASSING_STATS
    """

    # connect web driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # click event for getting data
    _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_STATS_SELECTOR)[2].find_elements(
        By.CSS_SELECTOR, 'a')[0].click()

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    player_passing_df = pd.DataFrame(columns=PASSING_STATS)

    # get players data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_ROW_SELECTOR)
    for element in elements:

        # player name
        name = element.find_elements(By.CSS_SELECTOR, 'td')[0].find_elements(By.CSS_SELECTOR, 'a')[0].find_elements(
            By.CSS_SELECTOR, 'span')[0].text

        player_dict = {
            'name': name,
            'key_passes_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[7].text,
            'passes_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[8].text,
            'pass_accuracy': element.find_elements(By.CSS_SELECTOR, 'td')[9].text,
            'cross_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[10].text,
            'long_pass_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[11].text,
            'through_pass_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[12].text,
        }

        player_passing_df.loc[len(player_passing_df)] = player_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(player_passing_df)
