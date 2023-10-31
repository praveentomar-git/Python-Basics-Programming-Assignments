#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to find sum of array?

# In[7]:


def sum_of_array(arr):
    result=0
    for i in arr:
        result+=i
    return result
arr=eval(input('enter the array :'))
print('sum_of_array :',sum_of_array(arr))


# ## Q2.	Write a Python Program to find largest element in an array?

# In[11]:


def largest_element(arr):
    le=arr[0]
    for i in arr:
        if i>le:
            le=i
    return le
largest_element([1,2,3,4,5])


# ## Q3.	Write a Python Program for array rotation?

# In[15]:


def array_rotation(arr):
    return arr[::-1]
array_rotation([1,2,3,4,5])


# ## Q4.	Write a Python Program to Split the array and add the first part to the end?

# In[59]:


def split_rotate(arr):
    first_element=arr[0]
    new_arr=arr[1::]
    new_arr.append(first_element)
    return new_arr


# In[63]:


arr=[1,4,4,7,9,9,10]
split_rotate(arr)


# ## Q5.	Write a Python Program to check if given array is Monotonic?

# In[51]:


def check_monotonic(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True


# In[65]:


arr=[1,4,4,7,9,9,10,1]
check_monotonic(arr)

