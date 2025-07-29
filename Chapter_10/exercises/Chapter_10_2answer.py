## PROMPT ##
"""
10.2 Write a program to read through the mbox-short.txt 
    and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
    and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()

# read through the mbox-short.txt
for line in handle:
    
    # pull the hour out from the 'From ' line
    if 'From ' in line:
        words = line.split()

        # finding the time
        time = words[5]

        # splitting the string a second time using a colon.
        hours_minutes_seconds = time.split(':')

        #figure out the distribution by hour of the day
        hour = hours_minutes_seconds[0]
        hours[hour] = hours.get(hour, 0) + 1
    
    

# print out the counts, sorted by hour
hours_sorted = sorted( [(k,v) for k,v in hours.items() ] )

[print(k,v) for k,v in hours_sorted]


## NOTES ##
# Desired input: mbox-short.txt
# Desired output:
"""
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
