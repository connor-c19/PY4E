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


## NOTES ##
# Desired input: SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Desired output: 416(...)
