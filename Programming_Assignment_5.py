#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to Find LCM?

# In[19]:


def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num+=1
        
lcm(12,18)


# ## Q2.	Write a Python Program to Find HCF?

# In[20]:


#Euclids Algorithm using while
def hcf(m,n):
    #considered that m>=n
    if m<n:
        #if m<n, change the position
        m,n=n,m
    while m%n!=0:
        m,n=n,m%n
    return n


# In[21]:


hcf(15,40)


# ## Q3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[23]:


def decimal_to_others():  
    num=int(input("enter the decimal number :"))
    binary=bin(num)
    octal=oct(num)
    hexadecimal=hex(num)

    print(f'binary no is :{binary}')
    print(f'octal no is :{octal}')
    print(f'hexadecimal no is :{hexadecimal}')
    
decimal_to_others()


# ## Q4.	Write a Python Program To Find ASCII value of a character?

# In[24]:


def chr_to_ascii():
    character=input('enter the character :')
    asci=ord(character)
    print(f'ascii value of {character} is :{asci}' )
chr_to_ascii()


# ## Q5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[25]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Select operation:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")

operation=int(input("Select operation :"))

a,b=float(input('enter first number :')), float(input('enter second number :'))

if operation==1:
    print(f'addition of {a} and {b} is : {add(a,b)}')
elif operation==2:
    print(f'subtraction of {a} and {b} is : {sub(a,b)}')
elif (operation)==3:
    print(f'multiplication of {a} and {b} is : {mul(a,b)}')
elif operation==4:
    print(f'division of {a} and {b} is : {div(a,b)}')
else:
    print('no such operation')

