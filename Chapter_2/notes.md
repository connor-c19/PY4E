# Why Program?

## Philosophy behind learning to program

- It's necessary to learn how computers work due to their everyday importance. (They're literally everywhere!)

- In order to do this, we must transition from user to programmer, or view our devices FROM the inside TO the outside.

## Why be a programmer?

- Learn some tools to make solving an arbitrary task easier, or to solve a problem for yourself.

- On a larger scale, create something that others can use, either as a creative outlet or to pay the bills. (Think open source projects for the former, Software Engineering for the latter)

## What is code?

- A sequence of stored instructions that can be run at any time within a computer.

- Syntax is important! Any error made in source code can't be interpreted by the computer, only explicit instructions work.

# Hardware Architecture

## CPU

- Arguably the computer part with the healthiest work ethic.
- Essentially asks "Whats the next instruction" 3-6 billion times a second. (Depending on the computer)
- Can only do one process at a time (not actually, but lets pretend for now), but is useful because it can execute 3-6 billion processes a second.

## Main memory (RAM)

- Acts as immediate storage, it feeds the CPU with instructions. (Answers the "What's next" question)

- Super fast access time for the CPU, but is also expensive, and doesn't have nearly as much storage as the secondary storage. (Hard drive)

- If you lose power, all of the data in RAM is lost.

- Where your program that you wrote is stored while it is running.

  - Your code is transformed from Python (the programming language) to 1's and 0's (machine language) that can be understood by the CPU.

## Hard drive (Secondary Storage)

- Your programs (along with everything esle) are stored here before being 'copied' to RAM to be ran by the CPU.

- Much slower access time, but much more space!

- Unlike RAM, your computer could lose power and all of your data remains intact.

## Input Devices/Output Devices (I/O)

- Input devices allow for user input; think keyboard, mouse, trackpad, microphone, camera, etc.

- Output devices allow for the computer to display data; think screens, speakers, lights, etc.

## Motherboard

- Connects all of the things we mentioned above together

# Python as a Language

## Python Backstory

- Invented by Guido van Rossum in 1991, the name comes from Monty Python's Flying Circus

- Was designed to be a fun, approachable language that is powerful enough under the hood to complete complex tasks.

- Readability is king for Python, meaning that it was created to make code that is easy to understand without excessive scrutiny. (That means that even you or I could begin to understand it at our current point in this course)

## Syntax Errors

- A mistake that is made when the rules of the coding language are not followed

- Python is read by an interpreter that expects you to follow certain rules when writing a program.

- Python doesn't hate you if this happens, it just means the interpreter cannot understand what you wanted to say

# What Do We Say? (How do we start coding in Python?)

## Reserved Words

- Words that already mean something in Python.

- These words cannot be used as variable names or identifiers.
  - I can't write a line that says 'if = 1', since the word 'if' is used by Python already. I can, however, write a line that says 'x = 1', since the word 'x' is NOT used by Python.

## Sentences

- A program is a series of statements that are executed IN ORDER. (CPU does Line 1, Line 2, Line 3, etc...)

- EX: 'x = x + 2' is a sentence (line) that assigns the value 'x' with itself + 2. (This code would only work if 'x' is defined in a previous line, such as 'x = 2')

## Python Scripts

- A python script is created when you put a series of python instructions into a file (with the .py extension) that can be called and run later.

- Scripts have a few patterns they can follow:

  - Sequential: The script consists only of instructions that are executed in the order that they appear

  - Conditional: The script contains an 'if' statement, where some parts of the code are run only if a certain parameter is met

  - Repeated: The script contains a block of code that runs repeatedly. How many times it will run is usually determined by a variable, which we will look at later.

  - Store-then-retrieve: A segment of code is stored under a name, and can be called at any point during the program. This mainly helps your code be more efficient, since otherwise you would have to write the same code in several different places if you needed it again.

- One script can contain multiple different types of patterns as many times as you'd like, depending on it's intended function. The only limit is your creativity.
