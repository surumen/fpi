import time
from selenium.webdriver.common.by import By

from utils.scrapers.whoscored import _WEB_DRIVER


def crawl_player_summary(team_id: int, api_delay_term=5):
    """
    get player summary data: team_name, team_id

    parameter ---------------------------------------------------------------
    url : (str) base url
    api_delay_term = (optional) 5

    return ------------------------------------------------------------------
    dict
    """

    # connect driver
    url = 'https://www.whoscored.com/Teams/{team_id}'.format(team_id=team_id)
    _WEB_DRIVER.get(url)

    # wait to load page
    time.sleep(api_delay_term)

    # make pandas dataframe
    league_teams = list(dict)

    # extract team data
    elements = _WEB_DRIVER.find_elements(By.CSS_SELECTOR, '#teams option')
    for el in elements:
        team_name = el.text
        team_id = el.get_attribute("value").split("/")[2]
        league_teams.append({
            'team_id': team_id,
            'team_name': team_name
        })

    # close driver
    _WEB_DRIVER.close()

    return league_teams

