# String Basics

## String review

- `+` means to concatenate, or add two strings

- `print()` outputs to the terminal

## String indexes

- Each character has a specific index in a string, starting at 0

`[]` = index operator, allows us to reference a specific index

- `len()` = a built-in Python function that returns the length of an iterable object

## Looping through strings

- Loops and indexes can be combined to parse through a string (and iterable object)

- Can use a `while` loop, but `for` loop is preferred since it is a determinate loop, that uses the elements present in the string.

- Such parsing can include:
  - Counting
  - Searching

## String slicing

- With `[:]`, we can **splice**, or pull a subsection out of, a given string.
- Ex: `my_string[0:4]` returns from index 0 up to (but not including) index 4

- Interestingly enough, referencing an end position outside of the string will not cause a traceback

- `my_string[4:]` will return the remainder of the string **from** position 4

- `my_string[:4]` will return the beginning of the string **up to (but not including)** position 4

- `my_string[:]` will return the whole string

## 'in' operator alternative useage

- `in` can be used as a 'within..?' operator

- Example: `'m' in 'maniac'` returns `True`

## String comparison

- Using the `==` operator, two strings can be compared. Equivalent strings return `True`, `False` is returned otherwise.

- Depending on the character set used by a certain computer, `<` and `>` can be used to compare strings. This is done by comparing the ASCII/Unicode values between the first two letters, and generating the appropriate response

# String Object Methods

- Objects usually have methods accessible by the `.` operator

- Such string methods will return a new string, rather than alternating the original value

- Example: `'HELLO'.lower()` will return `hello`

- `type()` will return the object type (review)

- `dir()` will return the associated methods with an object

## Common methods

- `find()` searches for a substring in parent string

- `upper()`/`lower()` self-explanatory

- `replace()` takes two arguments: old value and new value. Returns a new string with the replaced values

- `lstrip()`/`rstrip()` removes whitespace on either the left or right side

  - Whitespace includes space, tab, newline, or any 'transparent' character

- `strip()` is used to remove whitespace at both the beginning and end of a string

- `startswith()` determines if a string starts with a certain substring

## Unicode

- All internal strings are unicode. Cool!
