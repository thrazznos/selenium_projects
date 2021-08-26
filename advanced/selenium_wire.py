#Synopsis:
#Makes a request to google using seleniumwire driver,
#the prints a list of all urls and paths
#Source: https://www.dilatoit.com/2020/12/17/how-to-capture-http-requests-using-selenium.html

from seleniumwire import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

for request in driver.requests:
    print(request.url)
    print(request.path)

#Other members:
#status_code
#body
#headers

driver.close()