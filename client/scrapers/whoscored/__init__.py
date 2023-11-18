from selenium import webdriver
from selenium.webdriver.firefox.options import Options


_BROWSER_OPTIONS = Options()
_BROWSER_OPTIONS.add_argument('-headless')

_WEB_DRIVER = webdriver.Chrome(options=_BROWSER_OPTIONS)

