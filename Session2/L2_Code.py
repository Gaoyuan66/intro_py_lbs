#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Dr Ekaterina Abramova
Lecture 2, Code from the slides
"""

#%% OPERATIONS ON SEQUENCES
# --- indexing
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # create a seq (list) of 10 elems
print(L[0])       # 0 elem in first position
print(L[1])       # 1 elem in second position
print(L[-1])      # 9 elem in the last position

# --- Slicing
# obtain ALL elements (from start to stop, including stop)    
L[:]     
L[0:] 
L[:len(L)] 
L[:10]
L[0:len(L)]

# obtain chunk seq[start:stop] from start to n-1
L[0:5]  # from 0 to 5-1 [0, 1, 2, 3, 4]
L[2:5]  # from 2 to 5-1 [2, 3, 4] 
L[3:]   # from 3 to end (same as seq[3:len(L)]) [3, 4, 5, 6, 7, 8, 9]
L[3:25] # also works! [3, 4, 5, 6, 7, 8, 9]
L[:1]   # from 0 to 1-1 i.e. from 0 to 0 is just L[0] [0]
L[:9]   # from 0 to 9-1 [0, 1, 2, 3, 4, 5, 6, 7, 8]
L[:0]   # returns empty list [] i.e. from start to elem at index 0 is nothing

# minus notation (still remember that stop-1 is applicable)
L[:-1]  # from start to element (-1-1=-2) i.e. one before last 
# same as L[:-1:1]
# same as L[-10:-1] from 0 to stop-1   [0, 1, 2, 3, 4, 5, 6, 7, 8]
# same as L[-10:-1:1] from 0 to stop-1 in steps of 1 [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
L[:-3]  # from 0 to n-1  [0, 1, 2, 3, 4, 5, 6]
L[-1:]  # from -1 to the end  [9]
L[-3:]  # from -3 to the end [7, 8, 9] (equiv to L[-3::1])

# --- Extended Slicing
L[:5:1]       # from start to 5-1 [0,1,2,3,4]
L[5::1]       # from 5 to the end [5,6,7,8,9]
L[-10:-1:1]   # from -10 to -1-1 (remember stop-1 still applicable) in steps 1.
#
L[0:len(L):2] # from 0 to 10-1, but every 2nd elem [0, 2, 4, 6, 8]
L[::2]        # as above [0, 2, 4, 6, 8]
L[0:5:2]      # from start to 5-1 in steps of 2 [0, 2, 4]
# now stop + 1 is applicable since step size is negative
L[5::-1]      # from 5 to first elem in steps of -1 [5,4,3,2,1,0]
L[5:0:-1]     # from 5 to 0+1 in steps -1 [5,4,3,2,1] (since the end was j + 1)
L[:5:-1]      # from 10 to 5+1 in steps -1 [9,8,7,6]
L[::-1]       # from last elem to first elem in steps -1 (i.e. reverse order of the list)
# same as L[9::-1] 
# same as L[-1::-1] 
#
L[::-2]       # from last elem to first elem in steps -2 [9, 7, 5, 3, 1]
L[5:0:-2]     # from 5 to 0+1 in steps -2 [5,3,1]
# really fancy (and overly complicated way, that you should not use)
L[-9:4]       # from -9 to 4+1, in steps of 1
# same as L[-9:4:1]

# --- concatenation 
S1 = "London Business "
S2 = "School 2021"
S3 = S1 + S2  # Concatenate seq (strings) together
print(S3)     # London Business School 2021

# concatenation
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)     # [1, 2, 3, 4, 5, 6]

# --- making n copies
L7 = [0]     # a list with a single entry 0
L8 = L7 * 5  # replicate list L7 five times
print(L8)    # a list with 5 zeros, i.e. [0, 0, 0, 0 ,0]

# --- string formatting
# used with print() command, for example rounding during printing
x = 15.56755421
print("%.2f" % x) # 15.57
print("%.4f" % x) # 15.5676

# --- membership
year  = "2021" in S3 # Check if STRING 2021 is an element of S3 (True)
year2 = 2021 in L3   # Check if NUMBER 2021 is an element of L3 (False)

city = "London" not in S1 # Check if string London is an element of S1
print(city) # False, London is inside S1

# --- length
n    = len(L) # 10
minL = min(L) # 0
maxL = max(L) # 9

# --- for loop
# to be covered shortly


# --- set operations
A = {1,2,3}
B = {3,4,5}

# Intersection (elements in both A and B)
# i.e. A and B
A & B # {3}

# Union (all elements of A and all elements of B)
# i.e. either A or B
A | B # {1, 2, 3, 4, 5}

# Elements of A that are not in B
A - B # {1, 2}

# Elements of B that are not in A
B - A # {4, 5}


# -----------------------------------------------------------------------------
#%% IF CONDITIONAL EXECUTION 
# if
x = 5
if x == 5:
    print(x)
# 5
  
x = 5
y = "abc"
if (x == 5) and (y == "abc"):
    print(x, y)    
# 5 abc
   
# if-else
x = 7
if x == 5:
    print(x)
else:
    print("x does not equal 5!")

# if-elif-else
x = 10
if x == 5:
    print("x is 5")
elif x == 10:
    print("x is 10")
else:
    print("x is not 5 or 10")
# x is 10
    
# nested
x = 5; L = ["1","2","3"]
if x == 5:
    print("x is 5")
    if (len(L) != 0):
        for ii in L:
            print(ii)
elif x == 10:
    print("x is 10")
else:
    print("x is not 5 or 10")
# x is 5
# "1"
# "2"
# "3"


# -----------------------------------------------------------------------------
#%% RANGE : since range is a generator to see it, you need to convert it to a list first using list(range()) command then print
print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))
print(list(range(2,11,2)))
print(list(range(5,0,-1)))
print(list(range(10,1,-2)))


# -----------------------------------------------------------------------------
#%% ITERATION - FOR LOOP MOTIVATION:
# Motivation 1: if have a tedious way of performing a repetitive task
x = 0**2
print(x)
x = 1**2
print(x)
x = 2**2
print(x)

# Instead use a for loop:
for value in range(3):
    x = value**2
    print(x) 
# 0
# 1
# 4 

# --- We can:
# Iterate over a elements generated by range() function:
for ii in range(5):
    print(ii) 
# 0 
# 1 
# 2 
# 3 
# 4
  
# Iterate over elements of a list:
L = ["a","b","c"]
for ii in L:
    print(ii)
# a
# b
# c


# --- ITERATION OVER DIFFERENT SEQUENCES
# Iterate over elements of a list:
for ii in [1,2,3]:
    print(ii)    
# 1 
# 2 
# 3 

# Iterate over a sequence generated by range() fn using start, stop, step spec:
start = 0; stop = 10; step = 2
for ii in range(start, stop, step):
    print(ii)
# 0 
# 2 
# 4 
# 6 
# 8

# Iterate over a string:
s = "LBS !"
for ii in s:
    print(ii)
# L
# B
# S
# 
# !
    
# Iterate over tuple:
t = (1,"a", (1,2,3))
for ii in t:
    print(ii)
# 1 
# "a" 
# (1, 2, 3)

# Iterate over dictionary (note only keys are what is iterated over):    
d = {"a":1, "b":2}
for ii in d:
    print(ii)
# a 
# b   
    
# Iterate over set:    
S = {1,2,3}
for ii in S:
    print(ii)  
# 1 
# 2 
# 3
    
# Iterate over frozen set:    
F = frozenset(S)
for ii in F:
    print(ii)  
# 1 
# 2 
# 3
    
# Iterate over a sequence by index:
L = [1,2,3,4,5] # assume long list of data   
numPts = len(L) # number of data points
for ii in range(numPts): 
    # access element of L at index ii
    val = L[ii] 
    # use value for analysis


#%% Motivation 2: use a for loop to automate 
L = ['Generation Covid\n', 'Lockdown Eased\n', 'Is the vaccine working?\n']

# --- Novice:
res = [0]*3 # create results list in advance or use append()           
for value in range(3):
    s = L[value] # extract element in position specified by value
    res[value] = s.strip() 

# --- Coder:
res = [0]*3 # create results list in advance or use append()           
for value in range(3):
    res[value] = L[value].strip() # on a single line


# --- print statement INSIDE loop
x = 0
for ii in range(3):
    x += ii**2
    # prints x at every iteration
    print(x)

# --- print statement BELOW loop
x = 0 
for ii in range(3):
    x += ii**2
print(x) # prints final value of x once the for loop is finished


# -----------------------------------------------------------------------------
#%% NESTED for loops
for ii in range(2):
    for jj in range(3):
        print(ii, jj)
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2    
        
import numpy as np
count = 1
a = np.zeros([3,5])
for ii in range(3):
    for jj in range(5):
        a[ii, jj] = count
        count = count + 1
print(a)      


# -----------------------------------------------------------------------------
#%% Building Elements of a List
# Creating results list with appropriate size in advance
'''
data = # list of data
numPts = len(data)
res = [0] * numPts # results list
for ii in range(numPts):
    res[ii] = (data[ii] - mu)/ sigma
    # explicitly control at which position 
    # the result is stored using index ii
'''

# Using Append method to append elements one by one
'''
data = # list of data
numPts = len(data)
res = [] # empty results list
for ii in range(numPts):
    ans = # answer computation 
    res.append(ans)
'''


# -----------------------------------------------------------------------------
#%% Continue and Break Statements
# --- continue
L = [1, 2, None, 4, None, 5]
numPts = len(L)
tot = 0
for ii in range(numPts):
    if L[ii] is None:
        continue
    tot += L[ii]
print(tot) # 12

# --- break
L = [1, 2, 'golden_egg', 4, 5, 6]
numPts = len(L)
tot = 0
ind = 0
val = None
for ii in range(numPts):
    if type(L[ii]) == str:
        val = L[ii]
        ind = ii
        break
    tot += L[ii]
print(tot, ind, val) # 3 2 golden_egg


#%% FUNCTIONS - USER DEFINED
# desired result
def get_ing(a):
    return a + 'ing'
ans = get_ing('abc')

# returns None
def get_ing2(a):
    print(a + 'ing')
ans2 = get_ing2('abc')

# equivalent to above (nothing follows return statement, thus we get back None)
def get_ing3(a):
    print(a + 'ing')
    return
ans3 = get_ing3('abc')


# Return max number  
def maxNum(var1, var2): 
    if (var1 >= var2):  
        return var1
    else:  
        return var2  
a = 1.6
b = 2
ans1 = maxNum(a,b)
# code continues 

# Return max number: if we have 2 outputs
def maxNum(var1, var2): 
    if (var1 >= var2):  
        return var1, "Well done1!" 
    else:  
        return var2, "Well done2!"   

a = 1.6
b = 2
ans1, ans2 = maxNum(a,b)


# Binding Actual to Formal Parameters
def name(firstName, lastName):  
    person = firstName + " " + lastName
    return person
colleague1 = name('John', 'Smith')  
colleague1 = name(firstName = 'John', lastName = 'Smith')  
colleague1 = name(lastName = 'Smith', firstName = 'John')  

# equivalent ways to call the function:
# via binding by position of arguments passed into the funciton
name('John', 'Smith')  
# via binding identifier
name(firstName = 'John', lastName = 'Smith')  
name(lastName = 'Smith', firstName = 'John')  

# NOT LEGAL!!!
# name(firstName='John', 'Smith')


# def add(a, b): # (a, b) are user defined input 
# def add(a, b=1): # specification of b can be omitted


# -----------------------------------------------------------------------------
#%% [EXTRA] WHILE LOOP 
# while loop during optimisation 
eps    = 0.0001 # acceptable error 
diff   = 1e10  # some large number
x      = 0     # to be iteratively updated (current iter)
x_prev = 0     # to be iteratively updated (prev iter)
while diff > eps:
    # x    = # optimisation equation
    diff   = abs(x - x_prev)
    x_prev = x
# once diff is small enough condition fails, exit loop


# boolean variable to control the loop
done = False
counter = 5
ans = 1
while not done:
    ans *= counter
    counter = counter - 1
    if counter == 1:
        done = True
print(ans) # 120


for ii in range(5):
    for jj in range(5):
        print(ii, jj)
        if ii == 3:
            break

"""
while CONDITION1:
    # code chunk 1
    if CONDITION2:
        break 
    # code chunk 2
# main code
"""


# example using break:
x = "abc"        
while True:
    print("while: Line 1")    
    if (x == "abc"):
        print("Just before break")
        break # exits from current for/while loop
        print("Just after break")
    print("while: Line 2")
print("Code below: Line 3")
# while: Line 1
# Just before break
# Code below: Line 3

    
# --- Find 5 factorial (i.e. 5x4x3x2)
# using while loop
counter = 5
ans = 1
while counter > 1:
    ans *= counter
    counter = counter - 1
print(ans) # 120

# using for loop
ans = 1
for ii in range(1,6): # seq 1,2,3,4,5
   ans *= ii
print(ans) # 120


# -----------------------------------------------------------------------------
#%% [EXTRA] FLOATING POINT ARITHMETIC
print(0.1)
print("%.20f" % 0.1)

# --- EQUALITY FOR FLOATS
# Always worry about using == to test for equality between two floats!
total = 0
c = 0.1 # also try 0.2
# Add 0.1 ten times.
for ii in range(10):
    total = total + c
    print(total)
    
print(total) # 0.9999999999999999
print(total == 1.0) # False!

# option 1
print(round(total) == 1.0)  # True
# option 2 (typically used)
eps = 0.001 # define acceptable error term
print(abs(total-1.0) < eps) # True 
