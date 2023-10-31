#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to convert kilometers to miles?

# In[8]:


def kms_to_miles(kms):
    if kms>0:
        miles=kms/1.60934
        return miles
kms_to_miles(10)


# ## Q2.	Write a Python program to convert Celsius to Fahrenheit?

# In[11]:


def Cel_to_Fah(cel):
    fah=(9/5*cel)+32
    return fah
Cel_to_Fah(-10)


# ## Q3.	Write a Python program to display calendar?

# In[17]:


import calendar
def calendar_of_year(year):
    print(calendar.calendar(year))


# In[20]:


calendar_of_year(2024)


# ## Q4.	Write a Python program to solve quadratic equation?

# In[21]:


import math
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    # Checking if the discriminant is positive, negative, or zero
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Two distinct real roots:", root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return "One real root:", root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return "Two complex roots:", complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve_quadratic(a, b, c)

print("Solution:", result)


# ## Q5.	Write a Python program to swap two variables without temp variable?

# In[23]:


def swap(a,b):
    a,b=b,a
    return a,b
swap(10,15)

