#!/usr/bin/env python
# coding: utf-8

# ## Q1.	Write a Python Program to Add Two Matrices?

# In[3]:


matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[7, 8, 9],
           [6, 5, 4],
           [3, 2, 1]]

def sum_matrix(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): #checks that dimnesions are same
        result = []                   # takes input as matrix
        for i in range(len(m1)):
            row = []                  # takes input as rows
            for j in range(len(m1[0])):
                row.append(m1[i][j] + m2[i][j])
            result.append(row)
        return result
    else:
        return 'Dimensions are not the same'


# In[4]:


sum_matrix(matrix1,matrix2)


# ## Q2.	Write a Python Program to Multiply Two Matrices?

# In[5]:


def mult_matrix(m1, m2):
    if len(m1[0]) == len(m2):  #checks if the matrics can be multiplied (m1 columns * m2 rows)
        result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j]+=m1[i][k] * m2[k][j]
        return result
    else:
        return 'Matrix Multiplication Not Possible'


# In[6]:


matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[7, 8, 9],
           [6, 5, 4],
           [3, 2, 1]]
mult_matrix(matrix1,matrix2)


# ## Q3.	Write a Python Program to Transpose a Matrix?

# In[7]:


def transpose_matrix(matrix):
    # To get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # To create a new matrix with swapped rows and columns
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Looping through the original matrix and populating the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# To store the transposed matrix as a result
result = transpose_matrix(matrix)

# To print the transposed matrix
for row in result:
    print(row)


# ## Q4.	Write a Python Program to Sort Words in Alphabetic Order?

# In[16]:


def sorted_words():
    sentence=input("Enter the Sentence :").title()
    words=sentence.split(' ')
    sort_words=sorted(words)
    print(' '.join(sort_words))
sorted_words()


# ## Q5.	Write a Python Program to Remove Punctuation From a String?

# In[19]:


import string

def remove_punctuation(input_string):
    # Creates a translation table to remove punctuation characters
    translator = str.maketrans('','',string.punctuation)

    # Uses the translation table to remove punctuation
    clean_string = input_string.translate(translator)

    return clean_string


input_string = "Hello, World! This is a simple python program."

# Removes punctuation from the string
result = remove_punctuation(input_string)

# Displays the cleaned string
print("Original String:")
print(input_string)
print("\nString without Punctuation:")
print(result)

