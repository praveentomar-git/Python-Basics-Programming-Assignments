#!/usr/bin/env python
# coding: utf-8
Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
# In[7]:


def evenly_divisible(a,b,c):
    total=0
    for i in range(a,b+1):
        if i%c==0:
            total+=i
    return total
a,b,c=1,10,3
print(evenly_divisible(a,b,c))

Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
# In[28]:


def correct_signs(string):
    result=eval(string)
    return result
arg='13 > 44 > 33 > 1'
print(correct_signs(arg))

Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
# In[49]:


def replace_vowels(string,character):
    vowels='aeiouAEIOU'
    for vowel in vowels:
        string=string.replace(vowel,character)
    return string


# In[52]:


print(replace_vowels('the aardvark', "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))

Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1
# In[3]:


def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)


# In[4]:


for i in range(4):
    n=int(input())
    print(f'factorial {n} -> {factorial(n)}')

Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
# In[21]:


def hamming_distance(string1, string2):
    distance=0
    for i,j in zip(string1,string2):
        if i==j:
            distance+=0
        else:
            distance+=1
    return distance


# In[22]:


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))

