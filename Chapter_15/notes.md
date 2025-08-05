# Database Basics

- Problem: How could data be accessed/updated instantaneously and randomly in the 70's/80's?

- Solution: Databases, which allow data to be read, modified, and updated quickly while ensuring data integrity through using advanced programming techniques and clever math

- Relational Databases: model data by storing data in columns of tables

- Terms:

  - Database: contains many tables
  - Relation (or table): contains tuples and attributes
  - Tuple (or row): a set of fields that generally represent an object
  - Attribute (column or field): represent a quality or element of a tuple/row/object

- SQL (structured query language) is an imperative language used to issue commands to the database

  - CRUD commands (create, read, update, delete data)

- Database model/schema: the structure or format of a database

- SQLite: is known as an embedded database, it can be directly used in a peice of software.

- SQL commands:

```
  CREATE TABLE "Users" ("name" TEXT, "email" TEXT)`
  INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')
  DELETE FROM Users WHERE email='ted@umich.edu'
  UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
  SELECT \* FROM Users WHERE email='csev@umich.edu'
```

# Multiple SQL Tables

- A data model can be used to represent mutliple tables and the relationships between them

- Basic **normalization**:

  - Never put the same string data in twice
  - Use integers for keys and references

- For each piece of info:

  - Is the column an object or an attribute of another object?
  - Once we define objects, we need to define the relationships between objects

- It's a good idea to come up with one or a small number of foundational objects

- **Primary keys** are generally an integer auto-incremented

- **Logical keys** are used by the outside world, plain text values

- Relationships between tables are defined by **foreign keys**, or an integer id that is associated to that attribute's table

  - Foreign keys make databases able to represent a large swath of data more efficiently. A singe integer ID that points to a record in another table is much more efficient to store (especially across big data) than string (or other) values that are replicated.

## One-to-Many

- **Join** operation links several tables to return logical keys:
  - `SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id`
  - The above example represents several **many-to-one** relationships, where **many** records can be associated to one **genre**, but **many** genres cannot be associated to **one** record

## Many-to-Many

- In order to represent many-to-many relationships, a **junction** table is used:
  - No primary keys, only foreign keys that explain a relationship between two (or more) other tables, can also have logical keys with other attributes.

# Database Handout

```

Python for Everybody Database Handout

https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt

Download and Install: http://sqlitebrowser.org/

Single Table SQL

CREATE TABLE "Users" ("name" TEXT, "email" TEXT)

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu')
INSERT INTO Users (name, email) VALUES c('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')

DELETE FROM Users WHERE email='ted@umich.edu'

UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'

SELECT * FROM Users

SELECT * FROM Users WHERE email='csev@umich.edu'

SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name DESC

Multi-Table SQL:

CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER,
    "title" TEXT, "count" INTEGER)

INSERT INTO Artist (name) VALUES ('Led Zepplin')
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;

SELECT Album.title, Artist.name FROM Album JOIN Artist
    ON Album.artist_id = Artist.id

SELECT Album.title, Album.artist_id, Artist.id, Artist.name
    FROM Album JOIN Artist ON Album.artist_id = Artist.id

SELECT Track.title, Track.genre_id, Genre.id, Genre.name
    FROM Track JOIN Genre

SELECT Track.title, Genre.name FROM Track JOIN Genre
    ON Track.genre_id = Genre.id

SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id
    AND Album.artist_id = Artist.id


Many-Many Relationship

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;

INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
  FROM User JOIN Member JOIN Course
  ON Member.user_id = User.id AND Member.course_id = Course.id
  ORDER BY Course.title, Member.role DESC, User.name


```
