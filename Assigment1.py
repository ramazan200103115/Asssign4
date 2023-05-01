import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
selenium = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'gLFyf')))
selenium.send_keys('Selenium', Keys.ENTER)
time.sleep(10)

site = driver.find_element(By.CLASS_NAME, 'yuRUbf')
site.click()