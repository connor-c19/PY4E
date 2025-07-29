## PROMPT ##
"""

You are to retrieve the following document using the HTTP protocol 
    in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt

There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL 
    and print out the headers and data. Make sure to change the code to retrieve the above URL,
        the values are different for each URL.

Open the URL in a web browser with a developer console 
FireBug and manually examine the headers that are returned.
"""

import urllib.request, urllib.response

# retrieve the above URL 
url = 'http://data.pr4e.org/intro-short.txt'

# Parameter available to get headers as well as body
response = urllib.request.urlopen(url)

print(response.headers)









## NOTES ##
# Desired input: 
# Desired output: headers