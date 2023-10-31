#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python program to check if the given number is a Disarium Number?

# In[4]:


def check_desarium(num):
    num_str=str(num)
    total=0
    for i in range(len(num_str)):
        total+=int(num_str[i])**(i+1)
    if total==num:
        print(f'{num} is a Disarium Number')
    else:
        print(f'{num} is not a Disarium Number')
check_desarium(135)
check_desarium(111)


# ## Q2.	Write a Python program to print all disarium numbers between 1 to 100?

# In[17]:


def check_desarium(num):
    num_str=str(num)
    total=0
    for i in range(len(num_str)):
        total+=int(num_str[i])**(i+1)
    if total==num:
        return True
    else:
        return False
desarium_list=[]
for i in range(1,101):
    if check_desarium(i)==True:
        desarium_list.append(i)
print(desarium_list)


# ## Q3.	Write a Python program to check if the given number is Happy Number?

# In[17]:


def is_happy_number(num, visited=set()):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit) ** 2
    if total == 1:
        return True
    elif total in visited:
        return False
    else:
        visited.add(total)
        return is_happy_number(total, visited) # recursion

a = int(input('Enter an integer: '))
if is_happy_number(a):
    print(f'{a} is a happy number')
else:
    print(f'{a} is not a happy number')


# ## Q4.	Write a Python program to print all happy numbers between 1 and 100?

# ### another approach using while loop because when I was using the above code to find out the happy numbers between 1 to 100, it was returning 1 to 20 correctly but after that directly 100 because of recursive function but for individual numbers it's correct

# In[57]:


def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num_str = str(num)
        num = sum(int(digit) ** 2 for digit in num_str)
    return num == 1

''' the above is same like if num==1:
return True
else is not mendatory it'll consider automatically'''

happy_num = []

for i in range(1, 101):
    if is_happy_number(i):
        happy_num.append(i)

print("Happy numbers between 1 and 100 are:")
print(happy_num)


# ## Q5.	Write a Python program to determine whether the given number is a Harshad Number?

# In[56]:


def is_harshad_number(num):
    num_str=str(num)
    total=0
    for i in range(len(num_str)):
        total+=int(num_str[i])
    if num%total==0:
        return True
    else:
        return False
is_harshad_number(18)


# ## Q6.	Write a Python program to print all pronic numbers between 1 and 100?

# In[55]:


# The below code will give the pronic numbers between 1 to 100
def is_pronic_number():
    pronic_list=[]
    for i in range(1,10):
        pronic_list.append(i*(i+1))
    print(pronic_list)
is_pronic_number()

