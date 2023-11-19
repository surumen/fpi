import time
import pandas as pd
from selenium.webdriver.common.by import By
from client.scrapers.whoscored import _WEB_DRIVER
from client.utils import change_empty_df_values
from client.models.common.player_stats import OVERALL_STATS


_PLAYERS_TABLE_ROW_SELECTOR = '#player-table-statistics-body tr'


def crawl_player_overall_stats(team_id: int, api_delay_term=5):
    """
    crawling player summary data

    parameter -------------------------------------------------------------------
    team_id : (int or str) team_id
    api_delay_term = (optional) 5

    return ----------------------------------------------------------------------
    dict: OVERALL_STATS + DISCIPLINE_STATS
    """

    # connect web driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    player_summary_df = pd.DataFrame(columns=OVERALL_STATS)

    # get players data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _PLAYERS_TABLE_ROW_SELECTOR)
    for element in elements:

        # split full time games and halftime games
        games = element.find_elements(By.CSS_SELECTOR, 'td')[4].text
        games = games.split('(')
        full_time, half_time = games[0], '0'
        if len(games) > 1:
            half_time = games[1].replace(')', '')
        else:
            half_time = '0'

        # player name
        name = element.find_elements(By.CSS_SELECTOR, 'td')[0].find_elements(By.CSS_SELECTOR, 'a')[0].find_elements(
            By.CSS_SELECTOR, 'span')[0].text

        player_dict = {
            'name': name,
            'total_apps': full_time + half_time,
            'starting_apps': full_time,
            'sub_apps': half_time,
            'mins_played': element.find_elements(By.CSS_SELECTOR, 'td')[5].text,
            'yellow': element.find_elements(By.CSS_SELECTOR, 'td')[8].text,
            'red': element.find_elements(By.CSS_SELECTOR, 'td')[9].text,
            'motm': element.find_elements(By.CSS_SELECTOR, 'td')[13].text,
            'rating': element.find_elements(By.CSS_SELECTOR, 'td')[14].text,
        }

        player_summary_df.loc[len(player_summary_df)] = player_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(player_summary_df)
