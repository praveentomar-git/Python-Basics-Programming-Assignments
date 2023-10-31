#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to find words which are greater than given length k?

# In[27]:


def word_greater_than_lengthk(string,k):
    words=string.split()
    for i in words:
        if len(i)>k:
            print(i)
a='my name is praveen tomar'
word_greater_than_lengthk(a,2)


# ## Q2.	Write a Python program for removing i-th character from a string?

# In[9]:


def remove_character(string,i):
    new_string=string[:i]+string[i+1:] #it will remove ith character
    return new_string
a='my name is praveen tomar'
print(remove_character(a,5))


# ## Q3.	Write a Python program to split and join a string?

# In[13]:


def split_join(string):
    split=string.split()
    join=" ".join(split)
    return join
a='my name is praveen tomar'
print(split_join(a))


# ## Q4.	Write a Python to check if a given string is binary string or not?

# In[8]:


def binary_string(string):
    bin_str=['0','1']            #valid binary characters
    for i in string: 
        if i not in bin_str:
            return False
    return True
a='10110011'
print(binary_string(a))


# ## Q5.	Write a Python program to find uncommon words from two Strings?

# In[11]:


def uncommon_words(string1,string2):
    words1=set(string1.split())
    words2=set(string2.split())
    uncommon=words1.symmetric_difference(words2)
    return uncommon

string1="my name is praveen tomar"
string2="my brother's name is sachin tomar"
print(uncommon_words(string1,string2))


# ## Q6.	Write a Python to find all duplicate characters in string?

# In[15]:


def duplicate_characters(string):
    lst=[]
    dup_lst=[]
    for i in string:
        if i not in lst:
            lst.append(i)
        else:
            dup_lst.append(i)
    return set(dup_lst)
string1='my name is praveen tomar'
duplicate_characters(string1)


# ## Q7.	Write a Python Program to check if a string contains any special character?

# In[54]:


def special_character(string):
    spl_chr=set('[({/?<>;:\|`~!@#$%^&*-_})]')
    lst=[]
    for i in spl_chr:
        if i in string:
            lst.append(i)
    return set(lst)                           #removes the duplicates

if 
string='my name is --__!@#$ praveen tomar'
special_character(string)

