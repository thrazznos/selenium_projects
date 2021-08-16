#Synopsis:
#Opens the webdriver and navigates to a page

from selenium import webdriver
import time

PATH = "C:\\tools\\selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)

time.sleep(5)
driver.quit()
#comment