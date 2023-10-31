#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[154]:


def pos_neg_zero(num):
    if num==0:
        print("number is zero")
    elif num>0:
        print(num, ": is positive number")
    else:
        print(num, ": is negative number")
num=int(input('enter the number :'))
pos_neg_zero(num)


# ## Q2.	Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


def even_odd(num):
    if num==0:
        print(num,': is an even number')
    elif num%2==0:
        print(num,': is an even number')
    else:
        print(num,': is an odd number')


# In[8]:


even_odd(1987654)


# ## Q3.	Write a Python Program to Check Leap Year?

# In[75]:


def check_leap_year(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')


# In[81]:


check_leap_year(2023)


# ## Q4.	Write a Python Program to Check Prime Number?

# In[201]:


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# In[202]:


number=int(input('enter the number :'))
is_prime(number)


# ## Q5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[203]:


prime_num_list=[]
for i in range(1,10001):
    if is_prime(i):
        prime_num_list.append(i)


# In[204]:


print(prime_num_list)


# In[ ]:




