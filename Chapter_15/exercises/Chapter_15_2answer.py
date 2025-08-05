## PROMPT ##

"""
This application will read the mailbox data (mbox.txt) and 
  count the number of email messages per organization 
  (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement 
  and committing the results to the database as each record is read in the loop, 
  it might take as long as a few minutes to process all the data. 
  The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
"""

import urllib.request, urllib.response
import re
import sqlite3

# retrieve the mbox URL 
url = 'http://www.py4e.com/code3/mbox.txt'

response = urllib.request.urlopen(url)

senders = dict()

# count the number of email messages per organization 
#   (i.e. domain name of the email address)
for line in response:

  line = line.decode()
  pattern = 'From [^ ]*@([^ ]*)'

  try:
    email = re.findall(pattern, line)[0]
  except: continue

  senders[email] = senders.get(email,0) + 1

    
#   use a database with the following schema to maintain the counts.

## Open/create db
con = sqlite3.connect("emaildb.sqlite")
cur = con.cursor()

## Create table
try: 
  cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
except:
  print("Table already exists, moving on...")

## Insert counts
for sender, count in senders.items():

  ### Checks if record exists
  if cur.execute(f'''SELECT * FROM Counts WHERE org = '{sender}' ''').fetchall():
    ### update record with current count
    cur.execute(f'''UPDATE Counts SET count = {count} WHERE org = '{sender}' ''')

  else: 
    cur.execute(f'''INSERT INTO Counts (org, count) VALUES ('{sender}', {count})''')

#cur.execute(f'''DELETE FROM Counts''')
print(cur.execute(f'''SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10''').fetchall())

# Save changes in DB and close connection
con.commit()
con.close()







## NOTES ##
# Desired input: SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Desired output: The top organizational count is 536.

