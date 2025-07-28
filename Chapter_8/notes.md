# List Basics

- Variables: overwritten, single values

- Collections: many values can be stored in a single variable

- List: initialized using [], can hold any permutation of any Python object

## Iterating Through Lists

- Lists are commonly looped through using `for` loops:

  - `list = []`
  - `for item in list:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`do something`

## Properties of Lists

- Lists are **mutable**, meaning that a given index can be changed, or the item can be appended to. Strings are not mutable, a variable re-assignment is needed to change the value. Like strings, lists are **zero indexed**

- `len()` can be used to find the length of a list.

- `range()` takes in an int argument and returns a list of numbers leading up to that number. Most commonly used for `for` loops.

## List operations

- Lists can be made using:

  - `stuff = list()` = list constructor

- Two lists can be concatenated together using the `+` operator

- Lists can be spliced using `[]`

  - `[start:stop:step]`
  - `[-1]`

- List methods: can be found using `dir()` function

  - `.append()` = add elements to a list
  - `x in list` = returns boolean for if value is in list
  - `.sort()` = sorts list

## Strings and lists

- `.split()` = done on a string, splits a string using a delimiter and returns a list containing the split elements.
