import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from client.scrapers.whoscored import _BROWSER_OPTIONS
from client.utils import change_empty_df_values
from client.models.common.team_stats import OVERALL_STATS


_TEAM_TABLE_ROW_SELECTOR = '#top-team-stats-summary #top-team-stats-summary-content tr'


def crawl_team_overall_stats(team_id: int, api_delay_term=5):
    """
    crawling team summary data

    parameter -------------------------------------------------------------------
    team_id : (int or str) team_id
    api_delay_term = (optional) 5

    return ----------------------------------------------------------------------
    dict: OVERALL_STATS
    """

    # connect web driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    team_summary_df = pd.DataFrame(columns=OVERALL_STATS)

    # get team data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _TEAM_TABLE_ROW_SELECTOR)
    for element in elements:
        league_dict = {
            'league_name': element.find_elements(By.CSS_SELECTOR, 'td')[0].text,
            'total_games': element.find_elements(By.CSS_SELECTOR, 'td')[1].text,
            'goals': element.find_elements(By.CSS_SELECTOR, 'td')[2].text,
            'yellow': element.find_elements(By.CSS_SELECTOR, 'td')[4].find_elements(
                By.CSS_SELECTOR, 'span')[0].text,
            'red': element.find_elements(By.CSS_SELECTOR, 'td')[4].find_elements(
                By.CSS_SELECTOR, 'span')[1].text,
            'ball_possession': element.find_elements(By.CSS_SELECTOR, 'td')[5].text,
            'pass_accuracy': element.find_elements(By.CSS_SELECTOR, 'td')[6].text,
            'aerial_duels_won_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[7].text,
            'rating': element.find_elements(By.CSS_SELECTOR, 'td')[8].text,
        }

        team_summary_df.loc[len(team_summary_df)] = league_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(team_summary_df)
