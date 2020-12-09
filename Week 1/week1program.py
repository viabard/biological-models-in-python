#SECTION 1 ---------------------------
print("SECTION 1 ---------------------------")
#adding the numbers from 1 to 10
print("Sum of numbers 1 to 10: " + str(sum(range(11))))
#adding up 10 strings
a = ("a" + "d" + "e" + "f" + "g" + "h" + "i" + "j" + "c" + "b")
print("Sum of single letters: " + a)
#adding two lists together
b = [1, 2, 3]
c = [4, 5, 6]
print(b + c)
#SECTION 2 ---------------------------
print("SECTION 2 ---------------------------")
#calling dir() function for a list and assigning a variable to the return value
d = dir(b)
#printing the type of this variable
print(type(d))
#printing the variable
print(d)
#SECTION 3.1 ---------------------------
print("SECTION 3.1 ---------------------------")
#printing the length of the list
print(len(d))
#sorting
d.sort()
#printing sorted list with number of items in list
print(d, len(d))
#reverse sort
d.sort(reverse = True)
print(d, len(d))
#appending
d.append("test")
print(d)
#SECTION 3.2 ---------------------------
print("SECTION 3.2 ---------------------------")
#variable of a new list of numbers 1 to 100 using list comprehension
num_list = [i for i in range(1, 101)]
print(num_list)
#new list
new_num_list = num_list[38:69] #depending on how we count?
print(new_num_list)
#find the positoin of value 45
new_num_list_index = new_num_list.index(45)
print(new_num_list_index)
#new list with the last 10 values of the 100 element list
final_num_list = num_list[-10:]
print(final_num_list)
#SECTION 3.3 ---------------------------
print("SECTION 3.3 ---------------------------")
#name variable
name = "Josh Schaaf"
#list of symbols in the string
name_symbols = list(name)
print(name_symbols)
#sorting and printing
name_symbols.sort()
print(name_symbols)
#SECTION 4.1 ---------------------------
print("SECTION 4.1 ---------------------------")
#importing math, making a string of math.pi, and printing types
import math
pi = str(math.pi)
print(type(math.pi), type(pi))
#SECTION 4.2 ---------------------------
print("SECTION 4.2 ---------------------------")
#practice with string.upper(), slicing, and string.split()
name1 = "Joshua Schaaf"
print(name1, name1.upper())
print(name1[1:5])
print(name1.split())
#SECTION 5 ---------------------------
print("SECTION 5 ---------------------------")
#dictionaries
friends = {"John": "Johnny", "Jar": "Jared", "Biyle": "Kyle", "Tay": "Taylor", "Gab": "Gabriella"}
print(friends.keys())
print(friends.values())
print(friends.items())
#days of the week
week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
print(week.items())
friends.update(week)
print(friends)
junk = {"XX": "junk"}
friends.update(junk)
print(friends)
#SECTION 6 ---------------------------
print("SECTION 6 ---------------------------")
#using functions in a module
from week1module import logsum
pos_numbers = [1, 2, 3, 4, 5]
logsum(pos_numbers)
logsum_pos_numbers = logsum(pos_numbers)
print(pos_numbers, logsum_pos_numbers)
some_strings = ["this", "is", "a", "list", "of", "strings"]
from week1module import joinwords
joined_some_strings = joinwords(some_strings)
print(some_strings, joined_some_strings)
#SECTION 7 ---------------------------
print("SECTION 7 ---------------------------")
#using the os module
import os
cd = os.getcwd()
os.chdir('.')
print(os.listdir())
os.chdir(cd)
print(os.chdir(cd))
#Section 8 ---------------------------
print("SECTION 8 ---------------------------")
#getting input form users
floating_point_variable = float(input("Enter a number: "))
print(type(floating_point_variable))
sentence = input("Enter a sentence: ")
print(sentence)