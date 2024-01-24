from selenium.webdriver.support import expected_conditions

import time
from browser import Driver
from locators import OrionHomePage, OrionCareerPage, CareerResultPage


def main():
    # Initialize the browser driver
    driver = Driver()
    try:
        # Open the Orion website
        driver.browser.get(driver.url)
        # Handle cookie consent if present
        try:
            cookie_decline_button = driver.browser.find_element(*OrionHomePage.COOKIE_DECLINE)
            cookie_decline_button.click()
        except Exception:
            pass

        # Navigate to the Careers page
        perspectives_navbar = driver.browser.find_element(*OrionHomePage.PERSPECTIVES_NAVBAR)
        company_navbar = driver.browser.find_element(*OrionHomePage.COMPANY_NAVBAR)
        driver.action.move_to_element(perspectives_navbar)
        driver.action.move_to_element(company_navbar).perform()
        company_career_drop = driver.browser.find_element(*OrionHomePage.COMPANY_CAREER_DROP)
        company_career_drop.click()

        # Perform actions on the Careers page
        location_dropdown = driver.browser.find_element(*OrionCareerPage.LOCATION)
        location_dropdown.click()
        location_select_vilnius = (driver.waitBrowser.until
                                   (expected_conditions.presence_of_element_located
                                    (OrionCareerPage.LOCATION_SELECT_VILNIUS)))
        location_select_vilnius.click()

        search_button = driver.browser.find_element(*OrionCareerPage.SEARCH_BUTTON)
        search_button.click()

        # Interact with the Career results page
        first_result_title_link = driver.browser.find_element(*CareerResultPage.FIRST_RESULT)
        first_result_title_link.click()

    finally:
        time.sleep(5)
        driver.browser.quit()


if __name__ == "__main__":
    main()
