#Synopsis:
#Opens google and types some text in the field and presses enter key

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\tools\\selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)


searchBox = driver.find_element_by_name("q")
searchBox.send_keys("selenium tutorial")
searchBox.send_keys(Keys.RETURN)

time.sleep(5)
#comment