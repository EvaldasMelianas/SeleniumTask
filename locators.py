from selenium.webdriver.common.by import By


class OrionHomePage(object):
    COOKIE_DECLINE = (By.CSS_SELECTOR, '#hs-eu-decline-button')
    COMPANY_NAVBAR = (By.XPATH, '//a[@id="menu-27"]')
    PERSPECTIVES_NAVBAR = (By.XPATH, '//a[@id="menu-28"]')
    COMPANY_CAREER_DROP = (By.XPATH, '//a[contains(@class, "menu-item-2580")]')


class OrionCareerPage(object):
    LOCATION = (By.XPATH, '//*[@id="post-108"]//b')
    LOCATION_SELECT_VILNIUS = (By.XPATH, '//ul/li[contains(text(), "Vilnius")]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="post-108"]/div[1]/div[1]/div[2]/div[2]/button')


class CareerResultPage(object):
    RESULTS_CONTAINER = (By.CSS_SELECTOR, '.teaser.teaser-search.col-12')
    FIRST_RESULT = (By.CSS_SELECTOR, '.teaser.teaser-search.col-12 .article-title')
