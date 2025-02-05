# Conditional Steps

- In chapter 1, we mentioned conditional scripts, or scripts with certain parts that run only when a criteria is set. In this chapter, we look at how to implement such a script.

## Boolean type

- Since we are looking at conditional statements, we need to have a way to represent if a certian criteria is met (or not) in order to run code. This can be accomplished with the **boolean** type, which consists of two values: `True` or `False`.

- Once a variable is assigned a `True` or `False` value, it becomes a `bool`:

  - `value1 = True`
  - `type(value1)`
  - <class 'bool'>

## Comparison operators

- We can also produce such boolean values with **comparison operators**, which compare two values and result in either a `True` or `False` value:

  - `1 > 0`
  - True

- The `>` and `<` operators represent greater-than and less-than:

  - `print(1 > 2)`
  - False
  - `print(1 < 2)`
  - True

- The `>=` and `<=` operators are greater-than/less-than or equal to:

  - `print(1 >= 2)`
  - False
  - `print(1 >= 1)`
  - True

- The `==` is an equivalence checker, while `!=` checks if two items are **not** equal to each other.

  - `print('a' == 'c')`
  - False
  - `print('a' != 'c')`
  - True

- You probably noticed that I used strings in the last set of examples. Comparison operators are not just compatible with numbers, but can be used with strings as well. The `==` is commonly used to evaluate whether or not two strings are the same. As for the `>` `<` `>=` `<=` operators, they evaluate based off of the **first** index position of the string. For example:

  - `print('a' < 'c')`
  - True
  - `print('apple' < 'carrot')`
  - True

- When comparing the first character of one string witht the first character of another string, Python looks for the [Unicode](https://unicodelookup.com/#latin/1) value for each character and makes the appropriate comparison. That's why you can have a valid comparison done between `a` (Unicode value `97`) and `c`(Unicode value `99`), or `apple` and `carrot`.

## If statements

- Now that we understand Boolean values and how to produce them using comparison operators, we can begin to make our code **conditional** with the help of the `if` statement:

  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`

- Notice how the second line is farther right than the first line. Since `print("Hi")` is indented once more than `if x == 0:`, `print("Hi")` will run **ONLY IF** `x == 0` evaluates to be `True`. For example:

  - `x = 0`
  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`
  - Hi

- If `x` is not 0, then the code indented under the `if` statement won't run:

  - `x = 1`
  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`

- Nothing is printed out because the value of `x` is `1`, causing `if x == 0` to return `False`.

## Else statements

- With `else` statements, we can now provide an alternative to our `if` statements:

  - `x = 1`
  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`
  - `else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Goodbye")`
  - Goodbye

- When `if x == 0` produces a `False` value, Python looks for an `else` statement to run instead. If one exists, then the code indented under that statement will run.

## Elif statements

- Using `elif` statements, we can create scripts that check a value against multiple criteria:

  - `x = 1`
  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`
  - `elif x == 1:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Nice to see you again")`
  - `else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Goodbye")`
  - Nice to see you again

- Notice that the `else` statement didn't run. This is because `elif` is short for **else-if**, meaning that if the original `if` statement returns `False`, then any `elif` statements will be checked. If they **all** return `False`, then the `else` statement will be run. Otherwise, the first `elif` statement to return `True` will have it's code ran, and all of the other `elif` statements and `else` statement will be skipped:

  - `x = 1`
  - `if x == 0:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi")`
  - `elif x == 1:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Nice to see you again")`
  - `elif x == 2:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Howdy")`
  - `elif x == 3:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Howdy Pardner")`
  - `else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Goodbye")`
  - Nice to see you again

# Error Handling

- Ath this point, I'm sure you've ran into at least one [exception](https://docs.python.org/3/tutorial/errors.html#exceptions). An exception is simply an error that appears while our Python script is running. Here's an example:

  - `float('hello')`
  - Traceback (most recent call last):<br>File "\<stdin>", line 1, in \<module><br>ValueError: could not convert string to float: 'hello'

- In the first line, I attempted to convert the string `'hello'` into a `float`, which ultimately resulted in an error since `'hello'` is not a number. The second line details the error that the first line produced. If we were to correct the script to the one displayed below, we should **not** produce an error:

  - `float('42')`
  - 42.0

- Luckily for us, `try` and `except` statements allow us to decide which code to run when an exception occurs. Similair to `if` and `else`, `try` blocks attempt to run potentially problematic code. If such code throws an exception, the Python code stops at the line of code that produces an error and instead begins to run the code listed in the `except` block. Otherwise, it completes the code in the `try` block, and skips over the `except` block. Here's an example:

  - `x = "four"`
  - `try:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`float(x)`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print('Success!')`
  - `except`:
  - &nbsp;&nbsp;&nbsp;&nbsp;`print('Failure!')`
  - `print("All done")`
  - Failure!
  - All done

- In the `try` block, we attempted to typecast `x` to a `float`. Since `x` contained the value `"four"`, the line `float(x)` threw an exception. This caused Python to skip over the rest of the `try` block and run the `except` block code. Then last line `print("All done")` is run. Let's fix our code so it doesn't cause an error:

  - `x = "4"`
  - `try:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`float(x)`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print('Success!')`
  - `except`:
  - &nbsp;&nbsp;&nbsp;&nbsp;`print('Failure!')`
  - `print("All done")`
  - 4.0
  - Success!
  - All done

- Even though `"4"` is a string, it **only** contains numbers, so typecasting it to a `float` is valid. Since `float(x)` did not throw an error, Python was able to run the remainder of the code in the `try` block before skipping over the `except` block. The last line, `print("All done")`, is still ran because it is not indented under the `except` block.

- Handling errors is especially important for developers because it gives us a chance to keep our scripts running, even if something doesn't behave the way it's supposed to.
