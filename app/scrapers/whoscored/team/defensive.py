import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.scrapers.whoscored import _BROWSER_OPTIONS
from app.utils import change_empty_df_values
from app.models.common.team_stats import DEFENSIVE_STATS

_TEAM_TABLE_ROW_SELECTOR = '#top-team-stats-defensive #statistics-team-table-defensive #top-team-stats-summary-content tr'
_TEAM_TABLE_STATS_SELECTOR = '#top-team-stats-options li'


def crawl_team_defensive_stats(team_id: int, api_delay_term=5):
    """
    crawling team summary data

    parameter -------------------------------------------------------------------
    team_id : (int or str) team_id
    api_delay_term = (optional) 5

    return ----------------------------------------------------------------------
    dict: DEFENSIVE_STATS
    """

    # connect web driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # click event for getting data
    _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _TEAM_TABLE_STATS_SELECTOR)[1].find_elements(
        By.CSS_SELECTOR, 'a')[0].click()

    # wait to load page
    time.sleep(api_delay_term)

    # initialize dataframe
    team_defensive_df = pd.DataFrame(columns=DEFENSIVE_STATS)

    # get team data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, _TEAM_TABLE_ROW_SELECTOR)
    for element in elements:
        league_dict = {
            'league_name': element.find_elements(By.CSS_SELECTOR, 'td')[0].text,
            'shots_allowed_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[2].text,
            'tackles_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[3].text,
            'interceptions_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[4].text,
            'fouls_conceded_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[5].text,
            'offsides_won_per_game': element.find_elements(By.CSS_SELECTOR, 'td')[6].text,
        }

        team_defensive_df.loc[len(team_defensive_df)] = league_dict

    # close web driver
    _WEB_DRIVER.close()

    return change_empty_df_values(team_defensive_df)
