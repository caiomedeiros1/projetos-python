from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

# search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
# search_button.click()

# search_bar = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input'))
# )

# search_bar.send_keys("Python", Keys.ENTER)

first_field = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_field.send_keys('Caio')

second_field = driver.find_element(By.XPATH, '/html/body/form/input[2]')
second_field.send_keys('Medeiros')

third_field = driver.find_element(By.XPATH, '/html/body/form/input[3]')
third_field.send_keys('caio@gmail.com')

sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.click()