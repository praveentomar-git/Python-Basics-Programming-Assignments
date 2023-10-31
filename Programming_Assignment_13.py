#!/usr/bin/env python
# coding: utf-8
Question 1:

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

# In[31]:


import math
def calculate():
    C=50
    H=30
    sequence=input("enter the sequence :")
    split=sequence.split(',')     # splits the sequence from where , is mentioned
    res=[]              # empty list to store result
    for D in split:     # calculate and append result to the list
        D=int(D)
        Q =int(math.sqrt((2 * C * D)/H))
        result=res.append(Q)
    output=','.join(map(str,res))    # converts into comma seperated string
    return output
print(calculate())

Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1,¡¬Y-1.

Example

Suppose the following inputs are given to the program:

3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# In[36]:


def TwoD_array():
    X, Y = map(int, input("Enter two digits X and Y separated by a comma: ").split(','))
    result = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        result.append(row)
    return result
print(TwoD_array())

Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world

Then, the output should be:

bag,hello,without,world

# In[42]:


def sort_string():
    input_str=input('enter the input string :')
    words=input_str.split(',')
    output_str=','.join(sorted(words))
    return output_str
print(sort_string())    

Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world

# In[49]:


def sorting_duplicate_remover():
    input_str=input().split(' ')
    output_str=' '.join(sorted(set(input_str)))
    return output_str
print(sorting_duplicate_remover())

Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3

# In[54]:


def calculate_number_digits():
    input_str=input()
    letter=0
    digit=0
    for i in input_str:
        if i.isalpha():
            letter+=1
        elif i.isdigit():
            digit+=1
    print(f'LETTERS {letter}')
    print(f'DIGITS {digit}')
calculate_number_digits()

Question 6:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

1. At least 1 letter between [a-z]

2. At least 1 number between [0-9]

1. At least 1 letter between [A-Z]

3. At least 1 character from [$#@]

4. Minimum length of transaction password: 6

5. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

ABd1234@1

# In[56]:


import re
def password_validity():
    passwords = input("Enter comma-separated passwords: ")
    password_list = passwords.split(',')

    valid_passwords = []

    # Defining a regular expression pattern for password validation
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"

    for i in password_list:
        if re.match(pattern, i):
            valid_passwords.append(i)

    print(','.join(valid_passwords))
password_validity()

