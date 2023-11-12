#!/usr/bin/env python
# coding: utf-8
Question 1
Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True
# In[3]:


a=str(7227)
int(a[::-1])


# In[7]:


def is_symmetrical(number):
    new_num=str(number)
    return number==int(new_num[::-1])
for i in range(5):
    num=int(input())
    print(is_symmetrical(num))

Question 2
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6

multiply_nums("1, 2, 3, 4") ➞ 24

multiply_nums("54, 75, 453, 0") ➞ 0

multiply_nums("10, -2") ➞ -20
# In[20]:


def multiply_nums(string):
    new_num=string.split(sep=",")
    mul=1
    for i in new_num:
        mul*=int(i)
    return mul
print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))

Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181

square_digits(2483) ➞ 416649

square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
# In[29]:


def square_digits(integer):
    new_str=str(integer)
    string=""
    for ele in new_str:
        stri=str(int(ele)**2)
        string+=stri
    return int(string)
print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))

Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

setify([4, 4, 4, 4]) ➞ [4]

setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
# In[32]:


def setify(list1):
    return list(set(list1))
print(setify([1, 3, 3, 5, 5]))
print(setify([4, 4, 4, 4]))
print(setify([5, 7, 8, 9, 10, 15]))
print(setify([3, 3, 3, 2, 1]))

Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
Notes
•	The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
•	The mean will always be an integer.
# In[33]:


num=1234
[int(i) for i in str(num)]


# In[37]:


def mean(num):
    list1=[int(i) for i in str(num)]
    mean_value=sum(list1)/len(list1)
    return f'mean_value of {num} --> {int(mean_value)}'
print(mean(42))
print(mean(12345))
print(mean(666))

