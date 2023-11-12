#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.
# In[1]:


def equal(a,b,c):
    if a==b==c:
        return 3
    elif a==b or b==c or c==a:
        return 2
    else:
        return 0
print(equal(3, 4, 3))
print(equal(1, 1, 1))
print(equal(3, 4, 1))

Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order.
# In[14]:


def dict_to_list(dictionary):
    return sorted(dictionary.items())
print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))
print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}))

Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }

mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }

mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase.
# In[18]:


def mapping(lst):
    return {i:i.upper() for i in lst}
print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))

Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
# In[24]:


def vow_replace(string,word):
    vowels="AEIOUaeiou"
    for i in vowels:
        string=string.replace(i,word)
    return string
print(vow_replace("apples and bananas", "u"))
print(vow_replace("cheese casserole", "o"))
print(vow_replace("stuffed jalapeno poppers", "e"))

Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
# In[28]:


def ascii_capitalize(string):
    char=""
    for i in string:
        if ord(i)%2==0:
            char+=i.upper()
        else:
            char+=i.lower()
    return char
print(ascii_capitalize("to be or not to be!"))
print(ascii_capitalize("THE LITTLE MERMAID"))
print(ascii_capitalize("Oh what a beautiful morning."))

