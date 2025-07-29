# Dictionary Basics

- Dictionaries are a linear collection of key-value pairs

- Construciton can be done with `dict()` or `{}`

- Insert values using `dict_name['key'] = value`

# Dictionary Usage

- Creating histograms with dicts is quite common. Keys are either inserted with the first mention of a term, or have their value incremented upon any other mentions

- The `in` operator can determine whether or not a key is in an operator

- The `.get()` method checks if a key is present. If it isn't, then it creates an entry with a given default value

- Histogram Idiom: `dict['key'] = dict.get('key',0) + 1`

- `list()` function or `.keys()` method returns a list of the dict keys

- `.values()` method returns a list of the dict values

- `.items()` method returns a list of tuples containing `(key, value)`

- In a for loop, multiple iteration values can be used:
  - `for key, value in dict.items():`
