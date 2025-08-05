## PROMPT ##

"""
This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);


If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
The ZIP file contains the tracks.csv file to be used for this assignment. 
You can export your own tracks from iTunes and create a database, 
  but for the database that you turn in for this assignment, only use the tracks.csv data that is provided. 
  You can adapt the tracks_csv.py application in the zip file to complete the assignment.

To grade this assignment, the program will run a query like this on your uploaded database 
  and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
"""

import urllib.request, urllib.parse
import re
import sqlite3

# Initialize DB

con = sqlite3.connect("itunes.sqlite")
cur = con.cursor()

## Create tables

query = """
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
"""
try:
    cur.executescript(query)
except:
    print("Tables already exist, moving on...")


# Open data source file
try:
    fhand = open("tracks/tracks.csv")
except:
    print("Please navigate to the 'Chapter_15/exercises' directory before running this program.\n Quitting...")
    quit()

# For each line of data
for line in fhand:

    ## Separate out elements
    elements = line.strip().split(',')

    title, artist, album, count, rating, length, genre = elements


    ## If it does not exist, insert new record into Artist table
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))

    ## Grab artist_id for foreign key in album
    artist_id = cur.fetchone()[0]


    ## If it does not exist, insert new record into Genre table
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))

    ## Grab genre_id for foreign key in album
    genre_id = cur.fetchone()[0]

    ## If it does not exist, insert new record into Album table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))

    ## Grab album_id for foreign key in Track
    album_id = cur.fetchone()[0]

    ## insert new record or replace old record in Track table
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( title, album_id, length, rating, count, genre_id ) )



# Query DB to see if information is present
check_query = """SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3"""

results = cur.execute(check_query).fetchall()

for row in results:
    print(row)


# Save changes and close connection

con.commit()
con.close()


## NOTES ##
# Desired input: 
# Desired output: Table found on https://www.py4e.com/tools/sql-intro/
