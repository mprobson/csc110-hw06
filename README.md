**Due: After Lecture 25 midnight**
 
*Note 1: Homework Assignment 6 must be completed individually*


# Objective

The theme of this homework is a **word analysis program**.

In this homework we are going to use nested loops to check if two characters provided by a user are found, in order, inside a list of predefined strings.

The list of pre-defined strings is set and you cannot alter them, they are:

```
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
```

The user will provide one uppercase letter from these options: "A", "B", or "C", and a digit in these options: "1", "2", or "3".

Example: 
if the user provides the letter "B" and the digit "2", then the
word "B@2@" should be printed out because "B" and "2" are found, in that order
inside the string "B@2@". However, the string "@2B" is not printed because "B" does not appear somewhere before the "2" in the string "@2B".


*NOTE*: You are not allowed to use string methods to solve this homework.

## Before you code: A PLAN

I will ask you to **plan before you code.**
If you don't plan the idea before using the keyboard, you might get a bit lost.
If you need any help or want to debug, the FIRST THING I will ask you to show me will be your plan. 

  * Your plan can be a diagram of steps, a set of steps written in bullet-points, even using semi-python notes.
  * You should make this before you start editing the program.
  * You should have also considered potential errors in your logic before you start editing the program.

Try coming up with the solution by yourself. If you get stuck, you can check out the **Hints** provided at the bottom of the instructions: a visualization of the series of steps that your program should complete.

## Your Tasks:

For this homework you need to complete four tasks: 
  1) Make the `get_letter` function with input checking for the requested option.
  2) Make the `get_digit` function with input checking for the requested option. 
  3) Make the `check_pattern` function.
  4) Complete the `main` function

Before we explain the tasks, pay careful attention to the following notes and tips.

Also, read ALL of these notes and instructions before you start your work.

\newpage

### Expected printout:

So you understand what we are shooting for, an example run looks like this: 

```
Give an single uppercase letter: R
Error: You provided the wrong character.
Give an single uppercase letter: ABC
Error: it needs to be a single character.
Give an single uppercase letter: B
Give an single number character: 12
Error: digit needs to be in [1,3].
Give an single number character: 4
Error: digit needs to be in [1,3].
Give an single number character: #
Error: You provided the wrong character.
Give an single number character: 2
Strings with the pattern:
B@2@ 
Try Again? (y/n): n
The End
```

another example is:

```
Give an single uppercase letter: C
Give an single number character: 2
Strings with the pattern:
@C@2 C2C2 
Try Again? (y/n): y
Give an single uppercase letter: A
Give an single number character: 1
Strings with the pattern:
AA@1 
Try Again? (y/n): y
Give an single uppercase letter: C
Give an single number character: 3
Strings with the pattern:

Try Again? (y/n): n
The End
```

Note that:

  1. all matching strings are printed in the same line separated by a space
  2. when no strings match the pattern no strings are printed (only a new line)


# A Note on passing the tests

All tests are very strict with respect to the format of requested prompts and printouts so pay attention to exactly what is requested and replicate it as exactly as possible.

## Using strings, characters, and loops with lists

  * In this homework, we'll be using nested loops to compare a character inside one word to another character inside a second word. remember that the comparison operator is `==`
  * to obtain the length of a word (to help you with loop limits or to check word length) you can use the `len` function. For example : `len(word)` returns the length of the word.
  * to check if a string contains a character you can use the containment operator 'in' as in ``` if "@" in word: ``` 
  * to check if a string character is a digit, you can use the string method "isdigit()". If the string is called "text" then the code ``` text.isdigit() ``` will return "True" only if all characters in the string "text" are digits.
  * To access a value inside a list, use the square brackets access. Example: if the list is called "st_list" and you want to get a **copy** of the contents at index "idx", you can do this: ```val = st_list[idx]```.
  * To access a single character inside a string, use the square brackets access. Example: if the string is called "st" and you want to get a **copy** of the contents at index "idx", you can do this: ```ch = st[idx]```.

## Task 1: get_letter

The `get_letter` function has no input parameters and does the following:

### define the function

For this problem, you need to define the function. 
It needs no input parameters but it returns one string (a single character).
Inside the function, you should repeatedly do the following:


The actions inside the loop should be:
  1. ask for a string with the prompt: `"Give an single uppercase letter: "`
  2. If the length of the provided text is different than 1, you should print the message `"Error: it needs to be a single character."` and make sure the loop repeats by using `continue` to restart the loop. If the length is OK, go to the next check.
  3. If the provided letter is not "A", "B", or "C", you should print the message `"Error: You provided the wrong character."` and make sure the loop repeats by using `continue` to restart the loop. If the character is one of "A", "B", or "C", return the character.

When you are done, remember to call this function from the `main` function to know it is working.

### Testing

We provide three tests to see if the `get_letter` function is correct.

## Task 2: get_digit

The `get_digit` function has no input parameters and does the following:

### define the function

For this problem, you need to define the function. 
It needs no input parameters but it returns one string (a single digit character).
Inside the function, you should repeatedly do the following:


The actions inside the loop should be:
  1. ask for a string with the prompt: `"Give an single number character: "`
  2. If the provided text is not composed of only digits, you should print the message `"Error: your input should be only digits."` and make sure the loop repeats by using `continue` to restart the loop. If the text is digits, go to the next check.
  3. If the provided digit is not "1", "2", or "3", you should print the message `"Error: a single digit needs to be in [1,3]."` and make sure the loop repeats by using `continue` to restart the loop. If the character is one of "1", "2", or "3", return the character.

When you are done, remember to call this function from the `main` function to know it is working.

### Testing

We provide three tests to see if the `get_digit` function is correct. 

## Task 3: check_pattern

The `check_pattern` function receives the letter character, the digit character, and the string list called "st_list" (defined in the main) as input and it:
  
  * checks if any of the words inside the list contain the letter and number (in that order) and 
  * prints any that do contain them.

An example is:

Given this list in main:
```
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
```

And if the user provides the letter "C" and the digit "2", then the
word "@C@2" should be printed out because "C" and "2" are found, in that order
inside the string "@C@2". In addition, the word "C2C2" should be printed **once**, since "C" and "2" are contained in that word in that order.

The resulting full printout for that example is:
```
Give an single uppercase letter: C
Give an single number character: 2
Strings with the pattern:
@C@2 C2C2 
Try Again? (y/n): n
The End
```

Notice that you need to add code to the main function so that all of this is completed.


### define the function

For this problem, you need to define the function.. 
It needs to accept three input parameters, called `letter`, `digit`, and `lst`.

Before checking the list, it prints the following message: "Strings with the pattern:".

Then, you need to come up with the logic so that:

  1. words that contain the pattern (at least once) get printed out.
  2. words that contain the letter and the number, but not in that order (they might have the digit first and then, later, the letter), should not be printed.
  3. words that have the pattern more than once only get printed once.

Notice that the printout needs to be in the same line and separated by a space.
You may use the following example to guide your printout structure:

```
for word in ["one", "two", "three", "four"]:
    print(word, end=" ")
print()
```

In this example, all words are printed in the same line and the new line is added at the end (by the "print()" line).

When you are done, remember to call this function from the `main` function to know it is working.

## Task 4: the main

Note that some of the main function has been provided. Your job is to complete the following steps (after the indicated line):

You must create a loop to repeatedly do the following (until step 4 results in a break):

  1. get a letter and a digit from the user (calling the  get_letter and get_digit functions)
  2. checks the pattern to print the valid strings (calling the check_pattern function)
  3. After any words are printed, asks the user if they want to continue or not like this:
    "Try Again? (y/n): "
  4. if the user does not respond 'y', it ends; otherwise repeat steps 1 - 4.

Lastly (outside the loop): after the user chooses not to try again, print "The End"


## STEPS TO SOLVE THE HOMEWORK

  1. PLAN your solution in paper
  2. test your paper solution with example values
  3. transcribe your paper solution to python in small increments... running the program as you go to make sure you have not introduced syntax errors
  4. once a full function (task) is finished, you should run the tests to see if the function makes sense logically.


# Grading

  * **IMPORTANT**: If your code does not compile, you get a large poitnt reduction, so make sure you run your code often (to avoid syntax or runtime errors) and you always have it in a "running" state, even if it does not get the desired results.
  * [no grade] If you require assistance with debugging, I will ask for a paper version of your functions with the plans for how you wanted to solve each task.
  * 100% of your your grade will be the percentage of tests you pass.

---

## Grading criteria:

### General
The submission:

* includes a header with the name of any peers and any references (or -10%)
* runs without syntax errors (or -50%)
* uses appropriate, informative variable names (or -10%)
* adds a few small but informative comments (or -10%)

### Operations
The program:

  * Passes all 12 tests (or lose 8% per failed test)
