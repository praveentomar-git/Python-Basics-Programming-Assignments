#!/usr/bin/env python
# coding: utf-8
Question 1
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
# In[6]:


def filter_list(list1):
    fil_list=[]
    for i in list1:
        if isinstance(i, int):   # or if type(i)==int and i>=0:
            fil_list.append(i)
    return fil_list
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))

Question 2
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
# In[8]:


def reverse(string):
    rev_str=string[::-1]
    emp_str=''
    for i in rev_str:
        if i.isupper():
            emp_str+=i.lower()
        else:
            emp_str+=i.upper()
    return emp_str
print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))


# or

# In[11]:


string="Hello World"
reverse=string[::-1].swapcase()
print(reverse)

Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]

print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
first  ➞ 1

middle ➞ [2, 3, 4, 5]

last ➞ 6
Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.
# In[4]:


def unpack_list(lst):
    first,*middle,last=lst   # Using destructuring assignment
    return first,middle,last
lst = [1, 2, 3, 4, 5, 6]
first,middle,last=unpack_list(lst)
print(first)
print(middle)
print(last)

Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1
# In[2]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
for i in range(4):
    n=int(input())
    print(factorial(n))

Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
# In[7]:


def move_to_end(lst,num):
    start_lst=[]
    end_lst=[]
    for i in lst:
        if i==num:
            end_lst.append(i)
        else:
            start_lst.append(i)
    start_lst.extend(end_lst)
    return start_lst


# In[11]:


print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))

