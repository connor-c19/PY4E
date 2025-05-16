# Function Basics

In Chapter 1, we also mentioned store-then-retrieve code, or **functions**. Functions allow the programmer to write one code block that can be used multiple times at any point in the program.

## Defining a function

- Let's break down the following function definition:

  - `def myFunc():`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi there")`

- `def` is a keyword that tells Python we are going to be defining a function

- `myFunc` is the name of our function

  - the `()` next to `myFunc` is where we put any arguments used by the function

- &nbsp;&nbsp;&nbsp;&nbsp;`print("Hi there")` is ran whenever `myFunc()` is **invoked** (used). Notice how it is indented to the right once more than: `def myFunc():`

## Invoking a function

- Here is how we would invoke `myFunc()`:

  - `myFunc()`
  - Hi there

- We can invoke this function anytime we'd like, as many times as we want:

  - `myFunc()`
  - Hi there
  - `myFunc()`
  - Hi there
  - `print("Top o the morning to ya!")`
  - Top o the morning to ya!
  - `myFunc()`
  - Hi there
  - `myFunc()`
  - Hi there

- As you might expect, the code within a function is only ran when the function is invoked. If the function is never invoked, the code will not run:

  - `def myFunc2():`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("This is function 2!")`
  - <br>
  - `print("Hello, World!")`
  - Hello, World!

## Arguments

- Functions can also be defined to expect an input, or **argument**:

  - `def myFunc3(something):`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`print(something)`

- `something` can be thought of as a placeholder variable. This means that when defining the function, it is understood that `something` is given a value when the function is invoked:

  - `myFunc3("This function is awesome")`
  - This function is awesome

- In this case, the variable `something` is assigned to the string constant `"This function is awesome"`, which is passed as an argument.

- There can also be multiple arguments passed into a function:

  - `def attendance(name1, name2, name3):`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Welcome to class, " + name1)`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Welcome to class, " + name2)`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Welcome to class, " + name3)`
  -
  - `attendance("John", "Mary", "Susan")`
  - Welcome to class, John
  - Welcome to class, Mary
  - Welcome to class, Susan

## Function Return

- Functions can return values using the `return` keyword. Functions that don't return a value are considered **void** functions. All of the function examples before this section were examples of this type, since they lacked a `return` keyword.

- Functions with `return` can be used to set the value of a variable:

  - `def getName():`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`username = input("What is your name?"\n)`
  - &nbsp;&nbsp;&nbsp;&nbsp;`return username`
  -
  - `myName = getName()`
  - What is your name?
  - ->>> Thomas
  - `print(myName)`
  - Thomas

- Functions with `return` can also be used as a parameter for `if` statements:

  - `def isEven(num):`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`if num % 2 == 0: `
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return True`
  - &nbsp;&nbsp;&nbsp;&nbsp; `else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return False`
  -
  - `myNum = 5`
  - `if isEven(myNum):`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Even!")`
  - `else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("Odd!")`
  - Odd!

- If you have code after the `return` keyword in a function, it will not execute. A function will always stop with `return`:

  - `def countUp():`<br>
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("1")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("2")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("3")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`return "All Done!"`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("4")`
  -
  - `## countUp() returns a status string ##`
  - `status = countUp():`
  - 1
  - 2
  - 3
  - `print(status)`
  - All done!

# Built in Functions

- As we've seen before, there are also functions that come predefined with Python. [Here](https://docs.python.org/3/library/functions.html) is a list of those built in functions.

## Example: Min/Max functions

- An example of a built in function, `min()` finds the minimum value in a list of items and returns it:

  - `myList = [2,3,4,5,1]`
  - `min(myList)`
  - 1

- It can also work with strings by finding the minimum Unicode value within the string:

  - `myString = "abcA"`
  - `min(myString)`
  - 'A'
  - `ord('A')`
  - 65
  - `ord('a')`
  - 97

- The `max()` function does the opposite of `min()`:

  - `myList = [2,3,4,5,1]`
  - `max(myList)`
  - 5

- `max()` can also work with strings:
  - `myString = "abcA"`
  - `max(myString)`
  - 'a'
