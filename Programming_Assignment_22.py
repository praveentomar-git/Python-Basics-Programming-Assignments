#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes three parameters where:
•	x is the start of the range (inclusive).
•	y is the end of the range (inclusive).
•	n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]

list_operation(7, 9, 2) ➞ [8]

list_operation(15, 20, 7) ➞ []
# In[7]:


def list_operation(start,end,divisor):
    return [i for i in range(start,end) if i%divisor==0]
print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))

Question2
Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True

simon_says([1, 2], [5, 5]) ➞ False

simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True

simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
•	Both input lists will be of the same length, and will have a minimum length of 2.
•	The values of the 0-indexed element in the second list and the n-1th indexed element in the first list do not matter.
# In[24]:


def simon_says(list1,list2):
    if len(list1)==len(list2)>1:
        return list1[:-1]==list2[1:]
    else:
        return "wrong input"
print(simon_says([1,2], [5,1]))
print(simon_says([1, 2], [5, 5]))
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))

Question3
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) 
# In[35]:


def society_name(name_list):
    society=""
    for i in name_list:
        society+=i[0]
    return "".join(sorted(society)) #or "".join(sorted([i[0] for i in name]))
print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))

Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False
Notes
•	Ignore letter case (should not be case sensitive).
•	All test cases contain valid one word strings.
# In[46]:


def is_isogram(word):
    word=word.lower()
    return len(set(word))==len(word)


# In[47]:


for i in range(4):
    word=input('enter the word to check isogram :')
    print(f'is_isogram {word} ➞ {is_isogram(word)}')

Question5
Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
Examples
is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True
Notes
You don't have to handle empty strings.
# In[48]:


def is_in_order(string):
    return string==''.join(sorted(string))
is_in_order("edabit")


# In[49]:


for i in range(4):
    string=input('enter the word to check isogram :')
    print(f'is_in_order {string} ➞ {is_in_order(string)}')

