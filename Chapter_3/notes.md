# Defining Values

## Constants

- Constants are fixed values, such as letters, numbers, or strings.

  - `23`, `'c'`, `"cucumber"`

- Letters and strings can be defined with `''` or `""` (they are interchangeable), while numbers are simply entered in as they appear.

## Reserved words

- Constants can be assigned a named place in memory. However, there are some names that are off limits. These are called <strong>reserved words</strong>.

- Some examples include: `if`, `None`, `while`,`break` etc.

## Variables

- Constants that have been allocated a named piece of memory are called <strong>variables</strong>.

  - `variable1 = "cucumber"`

- Once variables are defined, they can have their contents changed later on:

  - `variable2 = "pie"`
  - `print(variable2)`
  - pie
  - `variable2 = "cake"`
  - `print(variable2)`
  - cake

- There are a few rules for naming variables:

  - They must start with letter or underscore. Ideally, you would just use a letter at the start.

  - They must only consist of letters, numbers, and underscores.

  - Variable names are case sensitive, meaning that `dog` and `Dog` would be considered two different variables.

  - It's best practice to use Mnemonic variable names, or names that are easy to remember and correlate to their value, but they can be whatever you want. Python won't care what variable name you use, as long as it isn't a reserved word.

- When assigning variables: we can even use expressions with other variables:

  - `x = 43`
  - `y = 2`
  - `z = x * y`
  - `print(z)`
  - 86

# Expressions

## Numeric expressions

- As you probably noticed in the section above, we can do math with numbers we have defined! While there are libraries out there that do additional calculation, our standard Python operators are: `+` `-` `*` `/` `**` `%` `//`

- The `+` and `-` operators do pretty much what you'd expect:

  - `print(4+2)`
  - 6
  - `print(4-2)`
  - 2

- The `*` operator multiplies numbers together:

  - `print(4*2)`
  - 8

- The `**` is the exponential operator:

  - `print(4**2)`
  - 8

- In order to determine how the `/` `%` `//` operators work, let's breifly discuss <strong>type</strong> in Python.

## Type

- We breifly touched on type earlier when we discussed defining different sorts of constants. Type is what it sounds like: the <strong>type</strong> of value that a constant or variable is. Let's run through a few types:

  - <strong>int</strong>: Integers in Python are stored as this type.

    - Ex: `4`

  - <strong>float</strong>: Similair to integers, but instead of a value being stored as a single digit, it's stored as a decimal, or [floating point value](https://learn.microsoft.com/en-us/cpp/c-language/type-float?view=msvc-170).

    - Ex: `4.0`, `3.65`, or `22.222222`.

  - <strong>str</strong>: Single characters to large strings of text are stored as this type. Strings are denoted by using either `''` or `""`, either one will do.

    - Ex: `"c"`, `'Python'`, or `"Man, I love Python!"`

  - There are more types in Python, but these should enough for the rest of this chapter.

- You can check what type of value a variable contains by using the `type()` function:

  - `type(4)`
  - <class 'int'>
  - `type(4.0)`
  - <class 'float'>
  - `type('c')`
  - <class 'str'>

- Also, sometimes the type of a variable can be changed. This is called <strong>typecasting</strong>:
  - `var1 = 4`
  - `type(var1)`
  - <class 'int'>
  - `var1 = float(var1)`
  - `type(var1)`
  - <class 'float'>

## Back to numeric expressions

- Now that we understand types in Python, let's cover how the `/` `%` `//` operators work.

- The `/` operator performs float division. Even if you divide one integer by another, the result will always be a float:

  - `print(4/2)`
  - 2.0
  - `print(2/4)`
  - 0.5
  - `print(1/3)`
  - 0.3333333333333333

- The `%` operator returns the remainder of a division operation:

  - `print(4%2)`
  - 0
  - `print(2%4)`
  - 2
  - `print(1%3)`
  - 1

- The `//` operator is the same as the `/` operator, but truncates the result. This means that if you end up with a decimal after dividing two numbers, say: `0.99`, then you can expect `0` as a result. If the result is initially `4.23` with the `/` operator, then the result would be `4` with the `//` operator:

  - `print(4//2)`
  - 2
  - `print(2//4)`
  - 0
  - `print(4//3)`
  - 1

- The `()` characters act as they would in a normal math expression:

  - `print(2 * (4 + 3) )`
  - 14

- As with regular math, some operators have precedence over others. `()` are always executed first, with the following operators having descending precedence:

  - `**`
  - `*` or `/`, `%`, and `//`
  - `+` or `-`
  - Operators of equal precedence are evaluated left to right.

- Interestingly enough, you can use the `+` operator to concatenate, or combine, two strings:
  - `print("Hello" + "World")`
  - HelloWorld
  - `print("Good " + "Bye")`
  - Good Bye

# User input

- By now, we should be pretty familiar with the `print()` function. We've seen how it gives our programs a way to <strong>output</strong> information for the user. Believe it or not, there exists a similar function that gives users a way to <strong>input</strong> information for our program to use with the `input()` function. Here's how it's used:

  - `name = input("hello there, what is your name?")`
  - hello there, what is your name?
  - ->>> Charlie
  - `print("Hello, "+ name)`
  - Hello, Charlie

- Let's break that down line by line:

  - `name = input("hello there, what is your name?")`
    - `name` is a variable we are using to store what the `input()` function grabs from the CLI.
    - `input("hello there, what is your name?")` is the `input()` function that grabs what a user types in the CLI. A message can be initialized to show when user input is required, like `"hello there, what is your name?"`, by putting it inside of the `input()` function.
  - hello there, what is your name?
    - This is the message printed out on the CLI, indicating that user input is required. This is another example of <strong>output</strong>.
  - ->>>Charlie
    - This is what the user typed in the CLI. From now on, I'll use `->>>` to indicate when a user is typing something in the CLI.
  - `print("Hello, "+ name)`
    - This `print()` function takes the result from the previous `input()` function and adds it to the end of the string `"Hello, "`, then outputs it to the CLI to make it look like our program is greeting the user.
  - Hello, Charlie
    - This is simply the result of the previous line.

- One important thing to note about the `input()` function is that even if the user types in a number, the `input()` function will return it as a string. For example:

  - `num1 = input("Please type in your favorite number")`
  - Please type in your favorite number
  - ->>> 42
  - `type(num1)`
  - <class 'str'>

- In order to do numerical operations on a user input, we can use typecasting to convert the input to the type we need it to be in:
  - `num_fav = input("Please type in your favorite number, then I will increment it")`
  - Please type in your favorite number, then I will increment it
  - ->>> 42
  - `num_fav = int(num_fav)`
  - `num_fav = num_fav + 1`
  - `print(num_fav)`
  - 43

## Comments

- Now that we are starting to get into programs that actually do something, most developers use a tool that helps them plan and organize their code. This tool is known as the <strong>comment</strong>, and is pretty much exactly what it sounds like: a way for developers to leave little hints, notes, or messages in their code. Comments are denoted by using the `#` character. Here's an example of how one might be used:

  - `#Takes in user's name, prints greeting`
  - `name = input("hello there, what is your name?")`
  - `print("Hello, "+ name)`

- As you can see, the three lines of code above compose a script that takes in user input, then prints it out in the form of a greeting. You'll notice that the first line starts with a `#`, denoting a comment. The cool thing about comments is you can say **whatever** you want in them. As long as there is a `#` character before what you said, the Python interpreter won't see it, and more importantly, won't throw any syntax errors.

- While you wouldn't want to overdo it, using comments is considered best practice when constructing Python scripts so that other developers who want to read, rewrite, or use your code can understand what is happening.

- You shouldn't rely on comments to justify confusing code, though. Python is constructed in a way that even without comments, the meaning should be reasonably apparent. So if you have variable names that sound more like serial numbers than the real-world values they represent, consider restructuring your code to make it more readable.

# A Word About Chapter Exercises

- For this (and future) chapter's exercises, you'll see that there is a `## PROMPT ##` section that details the goal of the script, and a `## NOTES ##` section with more comments below. These detail the certian inputs and outputs expected once the script has been corrected. Again, the goal is to correct the script so that when the user inputs the expected input, the script returns the expected output.
