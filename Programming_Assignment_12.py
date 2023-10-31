#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to Extract Unique values dictionary values?

# In[15]:


def unique_dict_values(dictionary):
    a=dictionary.values()
    return set(a)
dictionary={'a':1,'b':2,'c':3,'d':3}
unique_dict_values(dictionary)


# ## Q2.	Write a Python program to find the sum of all items in a dictionary?

# In[24]:


def sum_of_all_items(dictionary):
    a=dictionary.items()
    total=0
    for i,j in a:
        if isinstance(i, int or float):
            total+=i
        if isinstance(j, int or float):
            total+=j
    return total
dictionary={'a':1,'b':2,8:3,'d':3}
sum_of_all_items(dictionary)


# ## Q3.	Write a Python program to Merging two Dictionaries?

# In[32]:


def merge_dicts(dic1,dict2):
    dict1.update(dict2)
    return dict1
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
merge_dicts(dict1,dict2)


# ## Q4.	Write a Python program to convert key-values list to flat dictionary?

# In[48]:


def convert_list_to_dict(lst):
    dictionary={}
    for i,j in lst:
        dictionary[i]=j
    return dictionary
lst=[('a',1),('b',2),('c',3),('d',4)]
convert_list_to_dict(lst)


# ## or

# In[49]:


dict(lst)


# ## Q5.	Write a Python program to insertion at the beginning in OrderedDict?

# In[53]:


from collections import OrderedDict
def insertion_at_beginning(dict1):
    new_dict=OrderedDict(dict1)
    new_dict['new_key']=0
    new_dict.move_to_end('new_key',last=False)
    return new_dict
dict1={'a': 1, 'b': 2, 'c': 3, 'd': 4}
insertion_at_beginning(dict1)


# ## Q6.	Write a Python program to check order of character in string using OrderedDict()?

# In[68]:


from collections import OrderedDict

initial_dict = {'a': 100, 'f': 20, 'd': 30, 'c': 40, 'b': 50, 'e': 60}
print(initial_dict)

order_dict = OrderedDict(sorted(initial_dict.items()))
print(order_dict)


# ## Q7.	Write a Python program to sort Python Dictionaries by Key or Value?

# In[72]:


def sorted_dict(input_dict, sort_type):
    if sort_type == 'key':
        sorted_dict_keys = dict(sorted(input_dict.items()))
        print('Sorted dictionary using keys:', sorted_dict_keys)
    elif sort_type == 'value':
        sorted_dict_values = dict(sorted(input_dict.items(), key=lambda item: item[1]))
        print('Sorted dictionary using values:', sorted_dict_values)
    else:
        print('Invalid sort type')

initial_dict = {'a': 100, 'f': 20, 'd': 30, 'c': 40, 'b': 50, 'e': 60}
sorted_dict(initial_dict, 'key') 
sorted_dict(initial_dict, 'value')


# In[ ]:




