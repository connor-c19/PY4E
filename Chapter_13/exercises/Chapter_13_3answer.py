## PROMPT ##
"""
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
    and retrieve the first plus_code from the JSON. 
An Open Location Code is a textual identifier that is another form of address based on the location of the address.

To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.
http://py4e-data.dr-chuck.net/opengeo?

This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to provide the address that you are requesting as the q= parameter 
    that is properly URL encoded using the urllib.parse.urlencode() function 
    as shown in http://www.py4e.com/code3/opengeo.py


Please run your program to find the plus_code for this location:

Universidad de Buenos Aires
Make sure to enter the name and case exactly as above and enter the plus_code and your Python code below. 
Hint: The first five characters of the plus_code are "48Q3F ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. 
Your program should work with the Google API - but the plus_code may not match for this assignment.
"""


import urllib.request, urllib.parse, urllib.error
import json

# Prompt for a URL 
url = input('Enter URL (or just press enter): \n')

if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/opengeo?'

# The program will prompt for a location
location = input('Enter Location (or just press enter): \n')

if len(location) < 1: 
    location = 'Universidad de Buenos Aires'

# Contact a web service

## provide the address that you are requesting as the q= parameter
params = dict()
params['q'] = location

## attach encoded params to url string
url = url + urllib.parse.urlencode(params)


## Read the JSON data from that URL using urllib 
uh = urllib.request.urlopen(url)
data = uh.read().decode()

# Parse and extract the plus_code
body = json.loads(data)

plus_code = body['features'][0]['properties']['plus_code']
print(plus_code)


## NOTES ##
# Desired input:
# Desired output: 48Q3F(...)
