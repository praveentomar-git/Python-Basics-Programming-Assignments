#!/usr/bin/env python
# coding: utf-8
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
# In[1]:


def divisible_by_5and7(num):
    for i in range(num+1):
        if i%5==0 and i%7==0:
            yield i
n=int(input('enter the number :'))
for i in divisible_by_5and7(n):
    print(i,end=',')

Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
# In[9]:


def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i
num=int(input('enter the number :'))
output=",".join(map(str,even_numbers(num)))
print(output)

Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13
# In[19]:


def fibonacci_sequence(n):
    fib_seq=[0,1]   #initial elements of a fibonacci sequence
    [fib_seq.append(fib_seq[-1]+fib_seq[-2]) for i in range(2,n)]  
    return fib_seq
n=int(input())
output=",".join(map(str,fibonacci_sequence(n)))
print(output)

Question 4:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
# In[28]:


def user_name(email_id):
   split=email_id.split('@')
   return split[0]
email=input('enter the email id :')
print(user_name(email))

Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# In[31]:


class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
shape=Shape()
square=Square(50)
print(shape.area())
print(square.area())

