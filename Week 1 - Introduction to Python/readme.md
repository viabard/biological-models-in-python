# Week 1 - Introduction to Python
For this week, we needed to follow certain steps in order, making a single python file (week1program.py)
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

What your program should do:
1. Addition and printing:
    o add up the numbers from 1 to 10 and print the result to the screen
    o add up 10 strings, each with a single, different letter in it, to
        make one string, and print the result to the screen
    o make two lists and try adding them together and print the result.
2. Using dir, assignment, type() and print()
    o call the dir() function for a list (e.g. use: dir([])) and assign a
        variable to what the dir() function returns.
    o Print the type of this variable to the screen using the print
        function and the type() function (it should be a list)
    o Print this variable to the screen
3. Working with lists
o 3.1
                                                                11 Copyright by Jody Hey 2020
     Using the list from part 2, print the length of the list to the
        screen (use the len() ) function
     Do a sort of the list using the sort() function that comes with
        lists.
     Print the sorted list to the screen followed on the same line
        by the number of items in the list
     Do a reverse sort of the list using the sort() function that
        comes with lists.
     Print the sorted list to the screen followed on the same line
        by the number of items in the list
     Append to the list the string: “test” and print the list to the
        screen
o 3.2
     Make a variable of a new list of the numbers from 1 to 100
        using list comprehension (look it up) and print the list to
        the screen
    • Make a new list that has the 39th element up to but not
        including the 70th element by taking a slice of the list
        and print the list
    • In this new list, find the position of the value 45 using
        the index() method that belongs to lists. Print this
        position and the value in the list at this position.
    • Make a new list that has the last 10 values of the 100
        element list by using slice notation with negative
        values and print the list
o 3.3
     Create a variable that is a string with your name in it,
        • e.g. a = “Jody Hey”
     Make a new list of the symbols in this string by using the
        list() function
     Print the list
     Sort the list, and print the sorted list.
4. Working with strings
o 4.1
     Import the math module and make a variable that is a string
        of math.pi using the str() function
     Print the type of math.pi and the type of the variable you
        created using str()
o 4.2
                                                                12 Copyright by Jody Hey 2020
     Make a variable that is a string with your name with a space
        separating the first and last names
     Print this variable and an upper case version of the string
        using the upper() method.
     Print a slice of this string that includes the 2nd thru 5th
        characters
     Make a list of the two parts of your name, by using the
        split() method that belongs to strings and print the list.
5. Working with dictionaries
    o Create a dictionary using curly braces that has as values the
        names of 5 of your friends and as keys your nicknames for them
        (you can’t make up names if you like).
    o Print the keys of the dictionary
    o Print the values of the dictionary
    o Print the items in the dictionary
    o Make another dictionary with the days of the week as values and
        integers 0 thru 6 as keys.
    o Print the items in the second dictionary.
    o Create a new dictionary by adding the two previous dictionaries.
        Print this dictionary.
    o To this last dictionary add another dictionary that you’ve made
        using the key “XX” and the value “junk” and print the new
        dictionary.
6. Using functions in a module
    o Get the week1module.py program from Canvas and put it in the
        same directory where your program is.
    o In your program import this module
    o In your program, create a list of positive numbers (any numbers,
        as many as you want)
    o Edit the logsum() function to return, rather than print, the log of
        the sum.
    o Create a variable that has the log of the sum of the values by
        calling the logsum() function in week1module by passing to it this
        list of numbers.
    o Print the list and the log of the sum
    o In your program create a list of strings (any strings, as many as
        you want). 
                                                                13 Copyright by Jody Hey 2020
    o Create a variable that is a string with the words of the list joined
        by spaces by calling the joinwords() function in the week1module
        by passing to it this list of strings.
    o Print the list and the string of joined strings.
7. Using the os module
    o Import the os module and use it to get the name of the current
        directory. Assign a variable to this directory name.
    o Use the os.chdir() function to make the current directory be the
        root directory of your current hard drive.
    o Figure out how to get a listing of all the files that are contained in
        the current directory. (use help() and/or dir() to find any
        function that belong to the os module that can be used for listing
        the contents of a directory), and print the listing to the screen.
    o Use the os.chdir() function to return to the original directory
        (using the saved name).
    o Print the value returned by os.chdir()
8. Getting input from users
    o Write a line of code that instructs the user to type a number as
        input from the python command line (read about the input())
        function)
    o Create a floating point variable from that number.
    o print the type of the variable (use type()) and the value of it to the
        screen
    o Write a line of code that instructs the user to type a sentence and
        assigns a variable to that sentence.
    o Print the sentence.



Be sure to run your program to make sure it does everything that it is
supposed to do. The instructor should be able to just run it and have all the
correct output printed to the screen.
Some things that may help:
• Put print statements in your code for each part of the assignment (e.g.
before you do part 3.2 print(“part 3.2”)
• Try things out at the python command line before putting them in your
program. 
14 Copyright by Jody Hey 2020
• use the dir() and help() functions to find out about what belongs to
things and about how they work. Also don't hesitate to look things up
on the internet.
• Be sure to include comments in your code so that a person (i.e. me)
reading the file can understand what you are doing