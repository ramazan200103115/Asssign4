from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver: WebDriver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
time.sleep(2)

app = driver.find_element(By.ID, 'email')
time.sleep(2)

app.send_keys("Ramazan")
time.sleep(2)

app = driver.find_element(By.ID, 'pass')
time.sleep(2)

app.send_keys("12345678")
app.send_keys(Keys.ENTER)
time.sleep(2)


products = driver.find_element(By.TAG_NAME, 'Selenium').click()
time.sleep(10)