## PROMPT ##
"""
9.4 Write a program to read through the mbox-short.txt 
    and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines 
    and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
    to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary 
    using a maximum loop to find the most prolific committer.
"""

# Use the file name romeo.txt as the file name

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()

# read through the mbox-short.txt
for line in handle:

    # looks for 'From ' line
    if 'From ' in line:
        
        words = line.split()

        # takes the second word of those lines as the person who sent the mail
        email = words[1]

        # creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
        senders[email] = senders.get(email, 0) + 1
    
maximum = None
sender = ''
# reads through the dictionary
for email in senders:
    if maximum:
        if maximum < senders[email]:
            sender = email
            maximum = senders[email]
        
    else:
        sender = email
        maximum = senders[email]

# using a maximum loop to find the most prolific committer.
print(sender, maximum)












## NOTES ##
# Desired input: mbox-short.txt
# Desired output: cwen@iupui.edu 5