#synopsis:
#Uses seleniumrequests library to make a web request
#directly to a server
#source: https://pypi.org/project/selenium-requests/

import requests

response = requests.get("https://netrunnerdb.com")
print(response.status_code)

#Grab the xsrf token from headers
#create a headers object with the token
#make request to the login function
response.cookies.