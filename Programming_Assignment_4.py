#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to Find the Factorial of a Number?

# In[1]:


def factorial(n):
    if n==0:                #factorial of 0 is 1
        return 1
    elif n<0:              # negative number's factorila not possible
        return False
    else:
        return n*factorial(n-1)  # recursive formula
n=int(input('enter non-negative integer :'))
print(factorial (n))


# ## Q2.	Write a Python Program to Display the multiplication Table?

# In[9]:


def gen_table(num):
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')


# In[11]:


gen_table(16)


# ## Q3.	Write a Python Program to Print the Fibonacci sequence?

# In[16]:


def fibonacci(num):
    fib_seq=[]
    a,b=0,1                         # intial 2 values
    for i in range(num):
        fib_seq.append(a)
        a,b=b,a+b    # sum of 2 previous values and repeat upto n times
    return fib_seq   


# In[22]:


fibonacci(10)


# ## Q4.	Write a Python Program to Check Armstrong Number?

# In[62]:


def armstrong(num):
    str_num=str(num)   # makes string of the integer
    num_dig=len(str_num) # gives number of digits in a string 
    arm_sum=sum(int(every_dig)**num_dig for every_dig in str_num) #sum of every digit to the power of number of digits
    return arm_sum==num  # if the arm_sum is equal to the number then it's True
armstrong(153)


# ## Q5.	Write a Python Program to Find Armstrong Number in an Interval?

# In[63]:


for i in range(1,1000):
    if armstrong(i):
        print(i)


# ## Q6.	Write a Python Program to Find the Sum of Natural Numbers?

# In[41]:


def sum_of_NN(n):
    return n*(n+1)/2   #formula for the sum of first N natural numbers 
sum_of_NN(10)

