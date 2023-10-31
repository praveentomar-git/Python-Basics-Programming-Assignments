#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to find sum of elements in list?

# In[105]:


def sum_of_elements_in_list(my_list):
    total=0
    for i in my_list:
        total+=i
    return total
a=[1,2,3,4,5]
sum_of_elements_in_list(a)


# ## or

# In[107]:


sum(a)


# ## Q2.	Write a Python program to  Multiply all numbers in the list?

# In[8]:


def multiply_of_numbers_in_list(my_list):
    multiply=1
    for i in my_list:
        multiply*=i
    return multiply
a=[1,2,3,4,5]
multiply_of_numbers_in_list(a)


# ## or

# In[108]:


import math
math.prod(a)


# ## Q3.	Write a Python program to find smallest number in a list?

# In[110]:


def smallest_number_in_list(my_list):
    smallest=my_list[0]
    for i in my_list:
        if i<smallest:
            smallest=i
    return smallest
a=[1,2,3,4,5,0]
smallest_number_in_list(a)


# ## or

# In[111]:


min(a)


# ### Q4.	Write a Python program to find largest number in a list?

# In[113]:


def largest_number_in_list(my_list):
    if not my_list:
        return None     # Returns None for an empty list
    largest=my_list[0]  # Assume the first element is the largest
    for i in my_list:
        if i>largest:
            largest=i
    return largest
a=[1,2,3,4,5,0,9,8,7,87,15,35,25,6,95,54]
largest_number_in_list(a)


# ## or

# In[114]:


max(a)


# ## Q5.	Write a Python program to find second largest number in a list?

# In[73]:


def second_largest(my_list):
    my_list=sorted(my_list,reverse=True)
    second_largest=my_list[1]
    return second_largest
a=[1,2,3,4,5,0,9,8,7,87,15,35,25,6,95,54]
print(f'second largest number in a list : {second_largest(a)}')


# ## Q6.	Write a Python program to find N largest elements from a list?

# In[117]:


def N_largest_element(my_list,n):
    my_list=sorted(my_list,reverse=True)
    N_largest=my_list[0:n]
    return N_largest
a=[1,2,3,4,5,6,7,8,9,10,15,78,98,0,87]
N_largest_element(a,5)


# ## or

# In[53]:


import heapq
def N_largest_element(my_list,n):
    if n<=0:
        return 'enter positive integer'
    elif n>len(my_list):
        return 'n is greater than list length'
    else:
        nlargest_element=heapq.nlargest(n, my_list)
        return nlargest_element
a=[1,2,3,4,5,6,7,8,9,10,15,78,98,0,87]
N_largest_element(a,5)        


# ## Q7.	Write a Python program to print even numbers in a list?

# In[80]:


def even_number_in_list(my_list):
    even=[i for i in my_list if i%2==0]
    return even
a=[1,2,3,4,5,6,7,8,9,10,15,78,98,0,87]
even_number_in_list(a)


# ## Q8.	Write a Python program to print odd numbers in a List?

# In[81]:


def odd_number_in_list(my_list):
    odd=[i for i in my_list if i%2!=0]
    return odd
a=[1,2,3,4,5,6,7,8,9,10,15,78,98,0,87]
odd_number_in_list(a)


# ## Q9.	Write a Python program to Remove empty List from List?

# In[94]:


def remove_empty(my_list):
    removed_list=[i for i in my_list if i]
    return removed_list 
b=[1,2,3,4,5,list(),9,8,[],65]
remove_empty(b)            


# #### if i --> checks if the item is truthy. This means that it evaluates to True if the item has a value that is not considered "falsy" in Python. In the case of lists, an empty list [] is considered "falsy," so it will be treated as False in a condition.

# ## Q10.	Write a Python program to Cloning or Copying a list?

# In[140]:


def copying_list(my_list):
    copied_list=my_list[:] # Creates a copy of the original list using slicing
    return copied_list
a=[1,2,3,4,5,6,7,8,9,10,15,78,98,0]
copying_list(a)


# ## or

# In[141]:


import copy
copied_list=copy.copy(a)  #shallow copy, changes in original list will affect the copied list
copied_list


# ## or

# In[142]:


import copy
copied_list=copy.deepcopy(a)  #deep copy, changes in original list will not affect the copied list
copied_list


# ## Q11.	Write a Python program to Count occurrences of an element in a list?

# In[151]:


def count_occurances(my_list,num):
    count=0
    for i in my_list:
        if num==i:
            count+=1
    return count
a=[1,2,3,3,4,5,6,6,7,8,9,6]
count_occurances(a,6)


# ## or

# In[148]:


a.count(6)

