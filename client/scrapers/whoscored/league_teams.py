import time
from selenium.webdriver.common.by import By

from client.scrapers.whoscored import _WEB_DRIVER

_TEAMS_SELECTOR = '#teams option'


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
