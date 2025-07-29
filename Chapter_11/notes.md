# Regex Basics

- Regex provides a concise, flexible means for matching strings of text

- Not part of base Python, but library comes standard with Python installation and can be imported using `import re`

- `re.search(pattern, source)` is used like `find` or `startswith()`, depending on the pattern used

  - Ex: `re.search('^From: ', line)`

  - `re.findall()` looks for every occurance of a given pattern and returns a list of match strings

- `\` is used as an escape character for reserved regex characters

```
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
```
