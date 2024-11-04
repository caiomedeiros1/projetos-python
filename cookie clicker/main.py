from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

items = driver.find_elements(By.ID, 'products')
for item in items:
    print(item)
