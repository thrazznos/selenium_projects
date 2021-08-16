#Synopsis:
#Queries google.com with text and prints the first page of results
# with title, body, and url to the console

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
import time

ex_PATH = "C:\\tools\\selenium\\chromedriver.exe"
chrome_Options = Options()
chrome_Options.headless= True
driver = webdriver.Chrome(ex_PATH, options=chrome_Options)

driver.get("https://google.com")
print(driver.title)

searchBox = driver.find_element_by_name("q")
searchBox.send_keys("selenium tutorial")
searchBox.send_keys(Keys.RETURN)

results = driver.find_elements_by_class_name("g")

for result in results:
    print(result.find_element_by_css_selector('.TbwUpd.NJjxre').text)
    print(result.find_element_by_css_selector('.DKV0Md').text)
    print(result.find_element_by_css_selector('.IsZvec').text)
    print('')

time.sleep(5)
driver.quit()