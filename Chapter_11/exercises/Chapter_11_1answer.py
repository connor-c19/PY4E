## PROMPT ##
"""
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
    and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_2130749.txt (There are 100 values and the sum ends with 45)


Data Format
The file contains much of the text from the introduction of the textbook 
    except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

    Why should you learn to write programs? 7746
    12 1929 8827
    Writing programs (or programming) is a very creative 
    7 and rewarding activity.  You can write programs for 
    many reasons, ranging from making your living to solving
    8837 a difficult data analysis problem to having fun to helping 128
    someone else solve a problem.  This book assumes that 
    everyone needs to know how to program ...

The sum for the sample text above is 27486. 
The numbers can appear anywhere in the line. 
There can be any number of numbers in each line (including none).

The basic outline of this problem is to read the file, 
    look for integers using the re.findall(), 
    looking for a regular expression of '[0-9]+' 
    and then converting the extracted strings to integers and summing up the integers.

"""

import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_2130749.txt"
handle = open(name)

# read the file
text = handle.read()

# looking for a regular expression of '[0-9]+' 
matches = re.findall('[0-9]+', text)

# converting the extracted strings to integers and summing up the integers.
result = sum([int(num) for num in matches])

print(result)



## NOTES ##
# Desired input: regex_sum_2130749.txt
# Desired output: (...)45
