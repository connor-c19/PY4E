# Tuple Basics

- Much like lists, but are immutable
  - This means that they are much more efficient than lists. So if you have values that have no need to be sorted or worked upon, they should be stored within a tuples.
- Initialized with `()` or `tuple()`
- Multiple variables can be initialized with tuples: `(x, y) = (4, 'fred')`
- For comparison operations `<|>`, it compares the first numbers that are different and returns a value

# Sorting Lists of Tuples

- A dictionary can be sorted by key items by:

  - calling `d.items` to get a list of key, value tuples
  - using `sorted()` on the list of key,value tuples

- A dictionary can be sorted by value items by:
  - Looping through through the dict using dual-variable assignment
  - Append a value, key pair tuple to a temporary list
  - Use `sorted()` to sort the list of value,key tuples

## List Comprehension

- Creates a dynamic list
- Ex:
  - `c = {'a':10, 'b':1, 'c':22}`
  - `print( sorted( [(v,k) for k,v in c.items() ] ) )`
- Shows data in the format you'd like to see it rather than the steps you'd like to take
