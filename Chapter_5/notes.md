# Loops and Iteration

In Chapter 1, we mentioned repeated code, which allow a segmented of user defined code to be executed for a pretermined number (or infinite number) of cycles. This type of scripting employs **loops**.

## While Loop

- A `while()` loop is a type of function that will run code defined within it repeatedly until it's instructed to stop.In other words, it will **loop** through **iterations** until it is told otherwise. Here's a good example of one in action:

  - `x = 5`
  - `while (x > 0):`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("hi")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`x = x - 1`
  - hi
  - hi
  - hi
  - hi
  - hi

- Let's go through the following code line by line:

  - We've seen `x = 5` before, just a standard variable declaration. We'll use x to help determine when our `while()` loop should stop running
  - `while(x > 0)` is our `while()` loop. Notice how `x > 0` is used as a parameter, this means that our `while()` loop will run for as long as `x` is greater than `0`. This statement is checked with every iteration of the loop.
  - `print("hi")` is the first of the two statements executed in the **body** of the loop, each loop iteration.
  - `x = x - 1` is the second of the two statements executed with each loop iteration. This statement **decrements** `x`, meaning that if `x = 5` in the beginning, the next loop will start with the `while()` loop checking to see if `x > 0` with `x` having the value `4`, not `5`

- Now you can see why the loop will only run 5 times: `x` is updated with each iteration until `x > 0` is false. This is a pretty common way of controlling `while()` loops. You simply:

  - set a loop variable to preferred # of loops
  - update the loop variable with each cycle

- To recap, a `while()` loop:

  - Checks the condition (every single time!)
  - If the condition is **false**, the loop ends

- You're probably wondering: "What if I just don't give it a condition to check, will I get an error?"

  - Nope! You'll create an **Infinite** loop. Infinite loops will just hang out...forever!
  - Test it out in a script, then press **ctrl-c** to make it stop.
  - As you probably noticed, that loop would have kept on running if you hadn't asked it to cut it out.

- There are a couple more ways to terminate a loop:

  - The `break` statement will escape out of the loop immediately
  - The `continue` statement will jump back to the top of the loop **without** executing any remaining lines in the loop body

- An example of `break`:

  - `x = 5`
  - `while (x > 0):`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("ding")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`break`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("dong")`
  - `print(Hello there!)`
  - ding
  - Hello there!

- Notice how the `while()` loop only runs once, even though we have set `x = 5`. This is because the `break` statement doesn't care where we are in the loop, or how many iterations we have run thus far, it is determined to leave the loop immediately and run the rest of the program.

- An example of `continue`:

  - `x = 5`
  - `while (x > 0):`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("1")`
  - &nbsp;&nbsp;&nbsp;&nbsp;`if x == 3:`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `continue`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print("2")`
  - `print(Hello there!)`
  - 1
  - 2
  - 1
  - 2
  - 1
  - 1
  - 2
  - 1
  - 2
  - Hello there!

- If you check the output, you'll notice that `2` is skipped in the third `while()` loop iteration, where `x` has a value of `3`. This makes sense, considering that we have an `if()` statement that, once `x == 3`, executes the `continue` statement, which skips the rest of the loop contents and returns to the top for the next iteration.

## For Loop

- `for` loops are a different type of loop function. They are used when developers want to loop a specific number of times, usually through a collection of objects:

  - `for i in [5,4,3,2,1]:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`print(i)`
  - 5
  - 4
  - 3
  - 2
  - 1

- Let's go through the following code line by line:

  - `for i in [5,4,3,2,1]:` initializes a `for` loop that executes for every item in the list, `[5,4,3,2,1]`. `i` represents the current item in the list. With every iteration of the loop, `i`changes to the next item in the list
  - `print(i)` outputs the current value of `i`. Since there are 5 elements in the list being looped through, this statement will execute 5 times, outputting each value of our list.

## Examples of Loop Usage

- A great example of how `for` loops can be used is to find the largest number in a given list:

  - `largest = None`
  - `for i in [5,4,23,57,1]:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`if (largest == None):`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest = i:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`else:`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if largest < i:`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest = i`
  - `print(largest)`
  - 57

- You probably noticed that we used `None` as the initial value for `largest`. `None` is a built-in constant that represents **Null**, or nothing. It has no value. So why would it be used? In this case, the `largest` variable must be defined before our `for` loop runs, but will not need an actual value.

  - `for i in [5,4,23,57,1]:`
  - &nbsp;&nbsp;&nbsp;&nbsp;`if (largest == None) or (largest < i):`
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest = i:`
    `print(largest)`
  - 57

- See if you can implement the following with `while` or `for` loops:

  - Counting elements in a list object

  - Running total

  - Filtering user input (allow only numbers, strings, etc)

  - Find a specific value within a list object

- The `none` type is useful for making an 'empty' variable to use later in a loop.

- The `is` keyword is stronger than `==`, it basically checks if two items are stored in the same place in memory. `is` will be primarily used to check the equivalence of Booleans and `none` types.
