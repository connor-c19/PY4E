# File Basics

- A text file can be thought of a series of lines for Python to loop through

- `open()` will return a file handle, or entrypoint to a file, can be opened during the course of a program and will be closed

  - Parameter 1: name of the file (relative path)
  - Parameter 2: (optiona): 'r', or 'w'

- `\n` is the newline character, indicates that another line should be started (`print()` will always add `/n` before completing)

  - Is counted as a character, but is whitespace so it's invisible

- A text file has newlines at the end of each line

# Reading Files

- Most commonly treated as a sequence of lines, and will be iterated through using a `for` loop

- `for` loop uses a line variable to iterate through handle object, one of the massive pro's of Python

  - Print lines in file
    - using `in` or `.startswith()`
  - Count lines in file
  - Search for an item in a file

- `.read()` allows you to read an **entire** file to a variable as a single string

- When searching through files, it might be advantageous to skip lines we are not interested in. This could save us from executing unnecessary code using `continue`, which will start a new loop of the for loop when executed.

- Can use `input()` to get file name

  - `try` and `except` will handle any bad file names

- `quit()` can stop and exit the Python program
