from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.orioninc.com/')
driver.maximize_window()
action = webdriver.ActionChains(driver)
driver.find_element(By.CSS_SELECTOR, '#hs-eu-decline-button').click()
action.move_to_element(driver.find_element(By.XPATH, "//span[normalize-space()='Perspectives']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//span[normalize-space()='Company']")).perform()
driver.find_element(By.XPATH, '//*[@id="primaryMenu"]/ul/li[5]/div/div/div/div[1]/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="post-108"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/b').click()
WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//ul/li[@data-index='10']"))
).click()
driver.find_element(By.XPATH, '//*[@id="post-108"]/div[1]/div[1]/div[2]/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="teaser-27950"]/div/a').click()
