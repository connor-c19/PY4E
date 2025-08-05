## PROMPT ##

"""
If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, 
    and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Lovell', 14);
INSERT INTO Ages (name, age) VALUES ('Aayat', 20);
INSERT INTO Ages (name, age) VALUES ('Arissa', 35);
INSERT INTO Ages (name, age) VALUES ('Maia', 26);

Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
"""


import sqlite3
# create a SQLITE database 
## create a connection, or implicitly create it if it does not exist:
con = sqlite3.connect("ex1.db")


# create a table in the database called "Ages"

## In order to execute SQL statements and fetch results from SQL queries, 
##  we will need to use a database cursor
cur = con.cursor()
try:
  cur.execute(
  """CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
              )""")
except:
  print("Table already exists, moving on...")

# insert these rows and only these rows with the following commands
## executescript allows us to run multiple sql statements
cur.executescript(
"""DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Lovell', 14);
INSERT INTO Ages (name, age) VALUES ('Aayat', 20);
INSERT INTO Ages (name, age) VALUES ('Arissa', 35);
INSERT INTO Ages (name, age) VALUES ('Maia', 26);
""")

# run the following SQL command 
# Find the first row in the resulting record set

results = cur.execute(
"""SELECT hex(name || age) AS X FROM Ages ORDER BY X
""")

list_of_results = results.fetchall()

for result in list_of_results: print(result)

# Save changes in DB and close connection
con.commit()
con.close()



## NOTES ##
# Desired input: SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Desired output: 416(...)
