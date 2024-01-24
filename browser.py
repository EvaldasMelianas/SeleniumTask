from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from config import Settings


class Driver:
    """
    Class for browser drive creation
    """

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(f'--window-size={Settings.BROWSER_WINDOW_SIZE}')
        chrome_options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.waitBrowser = WebDriverWait(self.browser, Settings.TIMEOUT)
        self.action = ActionChains(self.browser)
        self.url = Settings.WEB_URL

    def __str__(self):
        return f'Browser is {Settings.BROWSER}'
