#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ## Q2.	Write a Python program to do arithmetical operations addition and division.?

# In[29]:


def addition(a,b):
    return a+b
def division(a,b):
    if b==0: 
        return 'DIVISION BY ZERO NOT ALLOWED'
    else:
        return a/b


# In[31]:


addition(18,98)


# In[33]:


division(10,2)


# ## Q3.	Write a Python program to find the area of a triangle?

# In[39]:


def triangle_area(base,height):
    area=1/2*base*height
    return area
triangle_area(10,15)


# ## Q4.	Write a Python program to swap two variables?

# In[56]:


def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
swap('praveen','tomar')


# ## Q5.	Write a Python program to generate a random number?

# In[51]:


import random
def random_num(a,b):
    if a>b:
        return 'invalid range'
    else:
        return random.randint(a,b)


# In[52]:


random_num(1,5)

