## PROMPT ##
"""
In this assignment you will write a Python program somewhat similar to 
    http://www.py4e.com/code3/json2.py.

The program will prompt for a URL, read the JSON data from that URL using urllib 
    and then parse and extract the comment counts from the JSON data, 
    compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing 
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2130754.json (Sum ends with 65)

You do not need to save these files to your folder 
    since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment 
    - so only use your own data url for analysis.

Sample Data:
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
"""


import urllib.request, urllib.parse, urllib.error
import json

# Prompt for a URL 
url = input('Enter URL (or just press enter): \n')

if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_2130754.json'


# Read the JSON data from that URL using urllib 
uh = urllib.request.urlopen(url)
data = uh.read().decode()

# Parse and extract the comment counts from the JSON data
body = json.loads(data)
comments = body['comments']
print("Count: ", len(comments))

# Compute the sum of the numbers in the file and enter the sum below:
print("Sum: ", sum([int(comment['count']) for comment in comments]))



## NOTES ##
# Desired input:
# Desired output: (...)65
