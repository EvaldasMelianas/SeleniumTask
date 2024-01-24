from selenium.webdriver.common.by import By


class OrionHomePage(object):
    COOKIE_DECLINE = (By.CSS_SELECTOR, '#hs-eu-decline-button')
    COMPANY_NAVBAR = (By.XPATH, "//span[normalize-space()='Company']")
    PERSPECTIVES_NAVBAR = (By.XPATH, "//span[normalize-space()='Perspectives']")
    COMPANY_CAREER_DROP = (By.XPATH, '//*[@id="primaryMenu"]/ul/li[5]/div/div/div/div[1]/a[1]')


class OrionCareerPage(object):
    LOCATION = (By.XPATH, '//*[@id="post-108"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/b')
    LOCATION_SELECT_VILNIUS = (By.XPATH, '//ul/li[@data-index="10"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="post-108"]/div[1]/div[1]/div[2]/div[2]/button')


class CareerResultPage(object):
    RESULTS_CONTAINER = (By.CSS_SELECTOR, '.teaser.teaser-search.col-12')
    FIRST_RESULT = (By.CSS_SELECTOR, '.teaser.teaser-search.col-12 .article-title')
