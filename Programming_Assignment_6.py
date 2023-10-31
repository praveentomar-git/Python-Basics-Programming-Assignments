#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[4]:


def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_list=fibonacci(n-1)
        fib_list.append(fib_list[-1]+fib_list[-2])
        return fib_list
n=int(input('enter the number of sequences that you want to print :'))
print(fibonacci(n))


# ## Q2.	Write a Python Program to Find Factorial of Number Using Recursion?

# In[48]:


def factorial(n):
    if n==0:                # base case
        return 1
    else:
        return n*factorial(n-1) #recursion
n=int(input('enter non-negative number :'))
print(factorial(n))


# ## Q3.	Write a Python Program to calculate your Body Mass Index?

# In[8]:


def BMI(weight,height):
    return weight/(height**2)
weight=float(input('enter the weigth in kgs :'))
height=float(input('enter the height in meters :'))
bmi=BMI(weight,height)
print(bmi)
if bmi<18.5:
    print('you are underweight')
elif 18.5<=bmi<24.9:
    print('you are healthy')
elif 24.9<=bmi<29.9:
    print('you are overweight')
else:
    print('you are obese')


# ## Q4.	Write a Python Program to calculate the natural logarithm of any number?

# In[31]:


import math
def nat_log(n):
    if n>0:
        return math.log(n)
    else:
        return "The natural logarithm is undefined for non-positive numbers."
n=float(input('enter the number :'))
print(nat_log(n))


# ## Q5.	Write a Python Program for cube sum of first n natural numbers?

# In[65]:


def cub_sum_of_NN(n):
    if n<=0:
        return False
    else:
        result=0                  # variable created to add the values
        for i in range(1,(n+1)):
            result+=i**3
        return result
n=int(input('enter the number :'))
print(cub_sum_of_NN(n))

