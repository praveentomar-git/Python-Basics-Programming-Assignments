#!/usr/bin/env python
# coding: utf-8
Question 1:

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# In[8]:


class divisible_by_seven_generator:
    def __init__(self,num):
        self.num=num
    def divisible_by_seven_generate(self):
        for i in range(self.num+1):
            if i%7==0:
                yield i
output=divisible_by_seven_generator(50)
for i in output.divisible_by_seven_generate():
    print(i, end=' ')

Question 2:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2

3.:1

3?:1

New:1

Python:5

Read:1

and:1

between:1

choosing:1

or:2

to:1

# In[45]:


def frequency_of_the_words():
    supplied_input=input('enter the input :')
    words=supplied_input.split()
    frequency={}
    for word in words:
        if word in frequency:     
            frequency[word]+=1    #It takes words as keys and counts as values
        else:
            frequency[word]=1
    sorted_words=sorted(frequency.keys())
    for word in sorted_words:
        print(f'{word}:{frequency[word]}')
frequency_of_the_words()

Question 3:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
# In[48]:


class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print('Male')
        
class Female(Person):
    def getGender(self):
        print('Female')
        
Male().getGender()
Female().getGender()

Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
# In[51]:


def genereate_all_sentences():
    sub=["I", "You"]
    verb=["Play", "Love"]
    obj=["Hockey","Football"]
    for s in sub:
        for v in verb:
            for o in obj:
                print(f'{s} {v} {o}')
genereate_all_sentences()

Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
# In[53]:


import zlib

original_string = "hello world!hello world!hello world!hello world!"

compressed_data = zlib.compress(original_string.encode())

decompressed_data = zlib.decompress(compressed_data).decode()

print("Original String:", original_string)
print("Compressed Data:", compressed_data)
print("Decompressed String:", decompressed_data)

Question 6:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# In[60]:


def binary_search(lst, ele):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == ele:
            return mid
        elif lst[mid] < ele:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Returns -1 if the item is not found in the list

# Example usage:
sorted_list = [1,2,3,4,5,6,7,8,9,10]
element_to_find = 8

result = binary_search(sorted_list, element_to_find)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")


# ### or

# In[58]:


not_sorted_list = [1,2,3,4,5,6,7,8,9,10,15,14,13,12,11]
not_sorted_list.index(12)


# ### However, the index() method uses linear search, which means it scans through the list sequentially until it finds the value. For larger lists, binary search is generally more efficient because it reduces the search space by half with each comparison, resulting in faster search times, especially in sorted lists. If the list is not sorted, the index() method is often the go-to choice for finding elements' indexes.
