#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes a string and returns a string in which each character is repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  "
# In[11]:


def double_char(string):
    new_string=""
    for i in string:
        new_string+=i*2
    return new_string
print(double_char("String"))


# or

# In[12]:


def doub_char(string):
    return "".join(i*2 for i in string)
print(doub_char("Hello World!"))
print(doub_char("1234!_ "))

Question2
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
Examples
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"
# In[4]:


def reverse(value):
    if type(value)==bool:    #or isinstance(value, bool)
        return not value
    else:
        return "boolean expected"

print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))

Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)

num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
# In[33]:


def num_layers(n):
    thickness=0.0005   # in meters
    for i in range(n):
        thickness=thickness*2  # double for every value
    return thickness
print(num_layers(1))
print(num_layers(4))
print(num_layers(21))

Question4
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]
# In[4]:


def index_of_caps(string):
    index_list=[]
    for index, char in enumerate(string):
        if char.isupper():
            index_list.append(index)
    return index_list
print(index_of_caps("eDaBiT"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))

Question5
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]
# In[6]:


def find_even_nums(n):
    even_num_list=[]
    for i in range(1,n+1):
        if i%2==0:
            even_num_list.append(i)
    return even_num_list
print(find_even_nums(8))
print(find_even_nums(2))

