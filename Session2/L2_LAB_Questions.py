#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author    : Dr Ekaterina Abramova
Lecture 2 : LAB QUESTIONS
"""

#%% Q1 OPERATIONS ON SEQUENCES -----------------------------------------------:
# Let's read Hillary Clinton's email titles into a list
f  = open("Subjects.csv")
# f  = open("Subjects.csv", encoding = "utf-8") # in case you have trouble
L  = f.readlines() # each email title is an element of the list
f.close()

# --- 1a) Indexing
'''
Indexing extracts a single element from a sequence using square brackets.
Working with Hillary Clinton's eamil titles list, L, extract the following:
    first title
    2nd title
    title at (approx) half way through position
    last title
'''
L[0]
L[1]
L[int(len(L)/2)]
L[-1]

#%% --- 1b) Slicing
'''
Slicing extracts a subset of the sequence, using L extract the following:
    every 2nd title
    the first half of the data
    the second half of the data
    all titles
    reverse the sequence
'''
len(L[::2])
L[:int(len(L)/2)]
L[int(len(L)/2):]
L
L[::-1]

#%% --- 1c) Extended Slicing
'''
EXTRA:
(i) 
    Open up L1_Code.py and find the section on Operations on Sequences. 
    There is a list L with 10 elements. Go over 'minus notation section' and 
    'extended slicing section'.
(ii)
    Go over rest of the exampes for operations on sequences.
'''


#%% Q2 IF-ELIF-ELSE ----------------------------------------------------------:
# --- 2a) If Statement
'''
You are working with a boolean varaible, x = False. 
Write an IF statement to check whether x is equal to 0. 
If the condition is true, print out: 0 is treated as False in Python.
'''
x = False
if x==0:
    print("0 is treated as False")
# Reminder: 1 is treated as True

#%% --- 2b) If-Else Statement
'''
Write an If-ELSE statement which will test whether a number is even or odd, 
assign the result to a boolean variable called isEven. 
Finally print out the isEven variable after you have completed the test.
Use x = 10 and x = 7 to check your code works correctly.
Hint: think about the possible use of the remainder!!
'''
x = 10
isEven = x%2==0
print(isEven)    

'''
EXTRA:
You are learning how to code efficiently. Therefore, try to think of a way, to
solve this problem with shorter code, i.e. which only uses the if statement.
'''
isEven = False
if x%2==0:
    isEven=True
print(isEven) 


#%% Q3 RANGE FUNCTION --------------------------------------------------------:
'''
We will examine the sequences that range function can generate. Remember that 
typically range produces a number one at a time, uses it and discards it, then 
the next number gets generated etc. This is done for memory efficiency and is 
designed to work together with a for loop.

For the above reason range does not reveal the sequence all at once, rather on 
a one-by-one element basis. In order to observe the sequence we need to 
typecast range to a different data type (e.g. list).
'''

# --- 3a) First check output of (note this won't reveal the sequence itself):
range(5)
range(0, 5)
range(0, 5, 1)

# Next typecast range(5) to a str, tuple, and a list.
# Which command actually revealed the entire sequence?
# What do the numbers in each position inside range(x1, x2, x3) mean?
str(range(5))
tuple(range(5))
list(range(5))

# --- 3b) 
'''
Give an example of a descending sequence produced by range. 

Produce a descending sequence which starts at 100, stops at 40 and reduces in 
steps of 20. Ensure that you display (print) the entire sequence.
'''
list(range(100, 39, -20))

# --- 3c)
'''
Is it correct to say that elements of a sequence generated by range are 
produced all together at once and are kept in the memory available to be 
re-used on many occasions?
'''
# No. It is an iterator that produces objects in it one by one.

# --- 3d)
'''
Examine output of this command print(list(range(-2, -10, -2))) which uses 
negative numbers for start, stop, step. 
-	Is this an ascending or descending sequence? 
-	Why did you not observe -10 inside the generated sequence?
'''
print(list(range(-2, -10, -2)))


#%% Q4 FOR LOOP --------------------------------------------------------------:
# --- 4a) For loop comprehension question
'''
You have 3 lists containing names, surnames and total holdings (in millions) 
of high net worth individuals investing in your fund. 
'''
names = ["LeBron", "Kyrie", "Damian"] 
surnames = ["James", "Irving", "Lillard"]
holdings = [45.3, 37.5, 31.2]
'''
Your task is to print out the name, surname and their holdings on one line for 
each customer, so that you obtain the following result at the end:
LeBron James 45.3 
Kyrie Irving 37.5
Damian Lillard 31.2
Your task is to do so efficiently, hence you need to use the for loop.

Hint1: you can print several items on the same line by separating them with a 
       comma, e.g. print(a, b, c)
Hint2: remember indexing of elements in a list starts from 0.
'''
for i in range(3):
    print(names[i],surnames[i],holdings[i])

# --- 4b) Applied For Loop Example: Float Point Arithmetic! 
'''
https://0.30000000000000004.com 
Your language isn’t broken, it’s doing floating point math. Computers can only 
natively store integers, so they need some way of representing decimal numbers. 
This representation is not perfectly accurate. This is why, more often than not 
'''
0.1 + 0.2 != 0.3
'''
When you have a base-10 system (like humans), it can only express fractions 
that use a prime factor of the base. The prime factors of 10 are 2 and 5. 
So 1/2, 1/4, 1/5, 1/8, and 1/10 can all be expressed cleanly because the 
denominators all use prime factors of 10. 
In contrast, 1/3, 1/6, 1/7 and 1/9 are all repeating decimals because their 
denominators use a prime factor of 3 or 7.

In binary (or base-2 computer systems), the only prime factor is 2, so you can 
only cleanly express fractions whose denominator has only 2 as a prime factor. 
In binary, 1/2, 1/4, 1/8 would all be expressed cleanly as decimals, 
while 1/5 or 1/10 would be repeating decimals. 
So 0.1 and 0.2 (1/10 and 1/5), while clean decimals in a base-10 system, 
are repeating decimals in the base-2 system the computer uses. 

When you perform math on these repeating decimals, you end up with leftovers 
which carry over when you convert the computer’s base-2 (binary) number into a 
more human-readable base-10 representation.
'''

# Examine 0.1 when you print it out with rounding, or to 20 deicmal places:
print(0.1)
print("%.20f" % 0.1)

'''
Design a for loop which will print out values 0.1 0.2 ... 1.0 to 20 decimal 
places (i.e. your loop will need to iterate 10 times). 
Which decimals are represented exactly? 
'''
L = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


'''
Another example: design a for loop to print out values: 1/10, 1/9, ..., 1/1 
to 20 dp.
'''
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


'''
Always worry when testing equality between floats after some arithmetic was
performed. 
'''
# For example, while the following works fine:
0.1 == 0.1       # True
1.0 == 1.0 
# This does not:
0.1 + 0.2 == 0.3 # False

'''
Take a look at the result of the following arthmetic calculations.

TASK 1:
Design a for loop to add 0.1 to values: 0, 0.1, ..., 0.9. 
At each iteration print the following on the same line:
    - result of the addition of 0.1 to the value, to 20 decimal places.
    - equality check between the sum (variable 'result') and the equivalent 
      'L[ii]' float i.e. corresponding float at position given by index 'ii' 
      (i.e. the decimal without arithmetic operation).

TASK 2:
Next, use a for loop to sum up 0.1 ten times (i.e. loop has 10 iterations). 
At each iteration print:
    - result of the sum at each iteration to 20 decimal places.
    - equality check between the sum (variable 'total') and the equivalent 
      'L[ii]' float i.e. corresponding float at position given by index 'ii' 
      (i.e. the decimal without arithmetic operation).
'''
# --- TASK 1:
result = 0
L2 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in range(9):
    print("%.20f" % (L2[i]+0.1), end=" ")
    print(L2[i+1] == (L2[i]+0.1))


# --- TASK 2:
total = 0
c = 0.1
for i in range(10):
    print("%.20f" % total, end=" ")
    print(total == L2[i])
    total += c

'''
Perform equality check between variable 'total' and 1.0 (afterall in Task 2 you
summed up 0.1 10 times, so expect to get a 1.0!). Is the result True or False?
'''    
total == 1.0


# --- 4c) EXTRA
'''
You have the following code, state what you exptect to be printed?
Afterwards actually run the code and observe output (if any). 
'''
for ii in []:
    print(ii)


#%% Q5 NESTED FOR LOOPS ------------------------------------------------------:
# --- 5a)  
'''
You saw how 2 nested loops can be used to fill a numpy array with values by
iterating over rows and cols of the array. Modify code provided on that slide:
   (1)	Write a print statement between the two for loops which will print out 
        current value of ii.
   (2)	Remove the previous print statement. Write a new print statement inside 
        the 2nd for loop which will print out current values of ii and jj.
        This should give you more understanding as to what the value of indices 
        ii and jj are at each iteration. Note: for each ii we execute all jj.
   (3)	Adjust code to fill in a 3 by 3 array with squares of numbers 1 to 9.
'''



# --- 5b) 
'''
Write 2 nested for loops that each iterate over a sequence generated by range(3). 
   (1)  Print out values of ii (outer loop indexing variable) and jj (inner 
        loop indexing variable) in the body of the inner most loop at each 
        iteration.
   (2)  Now re-design the loops such that printed values of jj never exceed ii. 
'''

for i in range(3):
    for j in range(3):
        print(i, j)
        
for i in range(3):
    for j in range(3):
        if j<=i:
            print(i, j)


# --- 5c) EXTRA
'''
Use 2 nested loops to print the following numbers 1 - 9:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''    
for i in range(10):
    print(i*str(i))
    
for i in range(1,10):
    text = ""
    for j in range(i):
        text += str(i)
    print(text)



#%% Q6 COMPREHENSIONS --------------------------------------------------------:
# --- 6a) LIST
'''
Use list comprehension to cube odd numbers from the tuple: T = (1,2,3,4,5,6). 
The result of your operation should be a list.
'''
T = (1,2,3,4,5,6)
T = [i**3 for i in T]

# --- 6b) LIST
'''
You are given the code below. Use list comprehension instead of the for loop to
produce the same resulting list L.
'''
L = []
for letter in 'energy':
    L.append(letter)
print(L)      # ['e', 'n', 'e', 'r', 'g', 'y']

# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# --- 6c [EXTRA]
'''
You are given a list of strings 
L = ["Practice", "Makes", "us", "100%", "Perfect"]. 
Use list comprehension to obtain a new list, which contains only the strings of 
length larger than 4 with all letters converted to lower case.

Hint: you will need to use a string method lower().

Note: you are learning how to quickly process strings stored as a sequence such 
as tuple or list, using just a single line of code. This is a very Pythonic 
approach since it makes coding quicker.
'''
L = ["Practice", "Makes", "us", "100%", "Perfect"]
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# --- 6d) [EXTRA] SET
'''
Working with the same list L = ["Practice", "Makes", "us", "100%", "Perfect"] 
create a set (call it unique_lenghts) which contains as elements of the set 
lengths each string.

Hint: use set comprehension instead, i.e. {} instead of [].
'''
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# --- 6E) [EXTRA] DICTIONARIES (code provided, just run it)
'''
Dictionaries use key:value pairs, therefore any mapping has to come from a 
compatible object. For example: 
-	Investigate the result of the command: enumerate(L). 
In order to check its contents we need to type cast it to a list, same as we 
did when checking sequences generated by range. 
-	With that understanding in mind, examine how we create a dictionary using  
comprehension.
'''
check = list(enumerate(L)) 
# enumerate creates a tuple of list elems with their associated pos in the list
print(check)

# Next, create a lookup map of the strings to their locations in the list L. 
location_mappings = {key:val for val,key in enumerate(L)} 
# mapping strings (key) to their locations (val)
print(location_mappings)
# Notice that I used words as keys and index as (numbers) as values, which is 
# specified by index:val.


#%% Q7 FUNCTIONS USER-DEFINED ------------------------------------------------:
'''
Write code for the functions below without using built-in functions 
abs(), min(), max(). Think of how you can write the code from first principles.     
'''
# --- 7a) ABSOLUTE VALUE FUNCTION FOR A NUMERIC
'''
Create a fn which finds an absolute value of a numeric type (int/float).  
Test the function on: ans = absVal(-10)
'''    
# Function Definition Goes Here:
def absVal(x):  
    # FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Function Call Goes Here:
ans = absVal(-10)
print(ans)


# --- 7b) MINIMUM NUMBER 
'''
Create a function which finds a minimum from 2 numeric types (int/float). 
Test the function on: ans = minNum(2, 5)
'''
# Function Definition Goes Here:
def minNum(x, y):
    # FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
# Function Call Goes Here:
ans  = minNum(2, 5)
print(ans)    
    
# --- 7c) ALTERNATIVE FUNCTION FOR MINIMUM NUMBER 
'''
You are provided a function maxNum() below.  
'''
# Function Definition Goes Here:
def maxNum(x, y):
    if x >= y:
        return x
    else:
        return y
# Function Call Goes Here:
ans = maxNum(2.3, 5.5)
print(ans) # 5.5

'''
Try to create an alternative way of writing the minNum() function, which only 
involves a single function call to maxNum().

Hint1: you can call any function you created from inside another function so 
long as it has already been defined in the code above it.

Hint2: Think of passing in negative inputs to the maxNum() function. 
Try out to see what you get for maxNum(-2, -5).
'''
# Function Call Goes Here:
ans2 = maxNum(-2, -5)
print(ans2) # -2

# Function Definition Goes Here:
def minNum2(x, y):
    # FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Function Call Goes Here:
ans2 = minNum2(2, 5)


# --- 7d) [EXTRA] MINIMUM NUMBER FROM A LIST OF NUMERICS
'''
Create a function 
def minList(L):
to find a minimum number from a list of numeric types (int/float). 

Test the function on: 
L = [1, 2, 3, 4, 5]
ans = minList(L)
'''
# Function Definition Goes Here:
def minList(L):
    # FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    
L = [1, 2, 3, 4, 5]
# Function Call Goes Here:
ans = minList(L)


# --- 7e) MAXIMUM NUMBER FROM A LIST OF NUMERICS
'''
Create a function 
def maxList(L): 
to find a maximum number from a list of numeric types (int/float). 

Test the function on: 
L = [1, 2, 3, 4, 5]
ans = maxList(L)	
'''
# Function Definition Goes Here:
def maxList(L):
    # FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

L = [1, 2, 3, 4, 5]
# Function Call Goes Here:
ans = maxList(L)
print(ans)


# -----------------------------------------------------------------------------
#%% Q EXTRA SLIDES WHILE LOOP
# --- a) 
'''
Write a for and a while loop to print numbers 10 to 1 in descending order. 
Which loop has fewer lines of code? 
Which loop is better suited to the task and why?
'''
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --- b) 
'''
We are now going to bring our knowledge together to solve a task: the famous 
Fibonacci series is the summation of the previous two numbers resulting in the 
next one: 1, 1, 2, 3, 5, 8, 13, 21… 

Use a for loop to store the Fibonacci series up to and including element n = 8 
(i.e. value 21) into a list L. Assume you are given the first 2 elements of 
sequence: 1, 1.
Hint: Remember that using operation on sequences one can create a list of 
length n with zero entries using L=[0]*n i.e. this “repeats” a list [0] n times.
'''
n    = 8 
L    = [0] * n # create a list of length n with 0 entries
L[0] = 1
L[1] = 1
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --- c) EXTRA 
'''
Repeat the Fibonacci task using a while loop.
Hint: solution is likely to require a counter variable which is incremented 
      inside the loop.
Hint: You could also benefit from using a shorthand notation of overwriting 2 
      variables on the same line. This allows updating variables x and y 
      simultaneously:
x = 5
y = 10
x, y = y, x      

Having written both for and while loop, examine which is more suited for to 
solve this kind of task?    
'''
a, b = 1, 1
n    = 8
L    = [0] * n # create a list of length n with 0 entries
L[0] = a
L[1] = b
counter = 1
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --- d) EXTRA 
'''
Use a while loop to print out the first n = 6 elements of the Fib series 
(i.e. up to and including value 8). Use a boolean variable done inside the 
CONDITION statement.
Hint 1: initialise done = False (see Slide 35) and use while not done as the 
        loop header. 
Hint 2: stop execution either using keyword break or setting done = True at the 
        relevant location in code.
'''
a = 1
b = 1
n = 1
done = False
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --- e) EXTRA
'''
You have a list L = [1,2,4,5,4,5,6]. The task is to establish the first 
position at which value 5 is in the list using a while loop. If that value is 
not in the list, print a message to that effect. 
'''
L = [1, 2, 4, 5, 4, 5, 6]
num   = 5 # number to be found  
index = 0
found = False
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



