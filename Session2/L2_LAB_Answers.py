#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author    : Dr Ekaterina Abramova
Lecture 2 : LAB ANSWERS
"""

# -----------------------------------------------------------------------------
#%% Q1 OPERATIONS ON SEQUENCES
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
n = len(L) // 2
L[n]

#%% --- 1b) Slicing
'''
Slicing extracts a subset of the sequence, using L extract the following:
    every 2nd title
    the first half of the data
    the second half of the data
    all titles
    reverse the sequence
'''
L[::2]
L[:n]
L[n:]
L[:]
L[::-1]

#%% --- 1c) Extended Slicing
'''
EXTRA:
(i) 
    Open up L1_Code.py and find the section on Operations on Sequences. 
    There is a list L with 10 elements. Go over 'minus notation section' and 
    'extended slicing section' in that script.
(ii)
    Go over rest of the exampes for operations on sequences in that script.
'''


# -----------------------------------------------------------------------------
#%% Q2 IF-ELIF-ELSE
# --- 2a) If Statement
'''
You are working with a boolean varaible, x = False. 
Write an IF statement to check whether x is equal to 0. 
If the condition is true, print out: 0 is treated as False in Python.
'''
x = False
if x == 0:
    print('0 is treated as False in Python')
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
if x % 2 == 0:
    isEven = True
else:
    isEven = False
print(isEven)    

'''
EXTRA:
You are learning how to code efficiently. Therefore, try to think of a way, to
solve this problem with shorter code, i.e. which only uses the if statement.
'''
isEven = False
if x % 2 == 0:
    isEven = True
print(isEven) 


# -----------------------------------------------------------------------------
#%% Q3 RANGE FUNCTION
'''
We will examine the sequences that range function can generate. Remember that 
typically range produces one number at a time, uses it and discards it, then 
the next number gets generated etc. This is done for memory efficiency and is 
designed to work together with a for loop.

For the above reason range does not create the sequence all at once, rather on 
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
str(range(5))   # 'range(0, 5)'
tuple(range(5)) # (0, 1, 2, 3, 4)
list(range(5))  # [0, 1, 2, 3, 4]
# typecasting to tuple or list reveals the entire sequence generated by range

# --- 3b) 
'''
Give an example of a descending sequence produced by range, ensure to display
the full sequence. 

Produce a descending sequence which starts at 100, stops at 40 and reduces in 
steps of 20. Ensure that you display (print) the entire sequence.
'''
print(list(range(10, 0, -1))) # typecast to a list to observe the sequence.

print(list(range(100, 39, -20))) # [100, 80, 60, 40]
# If try range(100,40,-20) the stop position is auto-incremented to 41

# --- 3c)
'''
Is it correct to say that elements of a sequence generated by range are 
produced all together at once and are kept in the memory available to be 
re-used on many occasions?
'''
# Incorrect:
# Elements are produced on a need by basis and can only be iterated over once
# They are generated 1-by-1, and get discarded 1-by-1 after they have been used

# --- 3d)
'''
Examine output of this command print(list(range(-2, -10, -2))) which uses 
negative numbers for start, stop, step. 
-	Is this an ascending or descending sequence? 
-	Why did you not observe -10 inside the generated sequence?
'''
print(list(range(-2, -10, -2))) # [-2, -4, -6, -8] # this is a descending seq
# which stops at -9 (since Python adds +1 to end of descending range seqs)


# -----------------------------------------------------------------------------
#%% Q4 FOR LOOP
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
numPts = 3 # we use n=3 because there are 3 elements in each list 
for ii in range(numPts): 
    print(names[ii], surnames[ii], holdings[ii])
# LeBron James 45.3
# Kyrie Irving 37.5
# Damian Lillard 31.2


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
for ii in range(10):
    print(L[ii], "%.20f" % L[ii])
'''
0.1  0.10000000000000000555
0.2  0.20000000000000001110
0.3  0.29999999999999998890
0.4  0.40000000000000002220
0.5  0.50000000000000000000
0.6  0.59999999999999997780
0.7  0.69999999999999995559
0.8  0.80000000000000004441
0.9  0.90000000000000002220
1.0  1.00000000000000000000
'''
# 5/10 (exactly)
# 1/10 2/10 3/10 4/10 (2/5) 6/10 (3/5) 7/10 8/10 (4/5) 9/10 (not exactly)

'''
Another example: design a for loop to print out values: 1/10, 1/9, ..., 1/1 
to 20 dp.
'''
# 1/1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10
for ii in range(1, 11):
    x = 1 / ii
    print(round(x, 2), "%.20f" % x)
'''
1.0  1.00000000000000000000
0.5  0.50000000000000000000
0.33 0.33333333333333331483
0.25 0.25000000000000000000
0.2  0.20000000000000001110
0.17 0.16666666666666665741
0.14 0.14285714285714284921
0.12 0.12500000000000000000
0.11 0.11111111111111110494
0.1  0.10000000000000000555
'''

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
for ii in range(10):
    result = L2[ii] + 0.1
    print("%.20f" % result, L[ii] == result)
'''
0.10000000000000000555  True
0.20000000000000001110  True
0.30000000000000004441  False !!!!!
0.40000000000000002220  True
0.50000000000000000000  True
0.59999999999999997780  True
0.69999999999999995559  True
0.79999999999999993339  False !!!!!
0.90000000000000002220  True
1.00000000000000000000  True
'''    
# i.e. the following summations were the problem:
0.2 + 0.1 == 0.3 # False
0.7 + 0.1 == 0.8 # False


# --- TASK 2:
total = 0
c = 0.1
for ii in range(10):
    total = total + c 
    print("%.20f" % total, L[ii] == total)
'''
0.10000000000000000555  True
0.20000000000000001110  True
0.30000000000000004441  False (as above)
0.40000000000000002220  True
0.50000000000000000000  True
0.59999999999999997780  True
0.69999999999999995559  True
0.79999999999999993339  False (as above)
0.89999999999999991118  False !!!!!
0.99999999999999988898  False !!!!!
'''

'''
Perform equality check between variable 'total' and 1.0 (afterall in Task 2 you
summed up 0.1 10 times, so expect to get a 1.0!). Is the result True or False?
'''    
print(total) # 0.9999999999999999
print(total == 1.0) # False !!!!!

# i.e. the following summations were the problem:
0.2 + 0.1 == 0.3 # False
0.7 + 0.1 == 0.8 # False
# And following that we had an accumulation of error when adding 0.1 to 'total'
# when trying to obtain 0.9 and 1.0 (which we didn't).


# --- 4c) EXTRA
'''
You have the following code, state what you exptect to be printed?
Afterwards actually run the code and observe output (if any). 
'''
for ii in []:
    print(ii)
# nothing is printed out as the sequence over which we iterated (list) is 
# actually an empty list, i.e. no elements.


#%% Q5 NESTED FOR LOOPS
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
# --- 5a) 
import numpy as np

# 1)
count = 1
a = np.zeros([3,5])
for ii in range(3):
    print(ii)
    for jj in range(5):
        a[ii, jj] = count
        count = count + 1  
# 2)
count = 1
a = np.zeros([3,5])
for ii in range(3):
    for jj in range(5):
        print(ii,jj)
        a[ii, jj] = count
        count = count + 1   
# 3)        
count = 1
a = np.zeros([3,3])
for ii in range(3):
    for jj in range(3):
        a[ii, jj] = count**2
        count = count + 1
print(a)


# --- 5b) 
'''
Write 2 nested for loops that each iterate over a sequence generated by range(3). 
   (1)  Print out values of ii (outer loop indexing variable) and jj (inner 
        loop indexing variable) in the body of the inner most loop at each 
        iteration.
   (2)  Now re-design the loops such that printed values of jj never exceed ii. 
'''
n = 3
for ii in range(n):
    for jj in range(n):
        print(ii,jj)

n = 3
for ii in range(n):
    for jj in range(n):
        if(jj > ii):
            break
        print(ii,jj)

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
for ii in range(1, 10):     # [1,2,3,4,5,6,7,8,9]
    accumStr = str(ii)
    for jj in range(ii-1):  # note: list(range(0)) returns empty result []
        accumStr += str(ii) # typecast int to str; add strings using + operator
    print(accumStr)   



#%% Q6 COMPREHENSIONS -------------------------------------------------------:
# --- 6a) LIST
'''
Use list comprehension to cube odd numbers from the tuple: T = (1,2,3,4,5,6). 
The result of your operation should be a list.
'''
T = (1,2,3,4,5)
L = [ii**3 for ii in T if (ii % 2 != 0)]
print(L) # note the result is a list! [1, 27, 125]

# --- 6b) Original long way of writing out each letter from string
'''
You are given the code below. Use list comprehension instead of the for loop to
produce the same resulting list L.
'''
L = []
for letter in 'energy':
    L.append(letter)
print(L)      # ['e', 'n', 'e', 'r', 'g', 'y']

# Shorthand version of the above code using list comprehension
L = [letter for letter in 'energy']
print(L)      # ['e', 'n', 'e', 'r', 'g', 'y']

# --- 6c) [EXTRA]
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
L    = ["Practice", "Makes", "us", "100%", "Perfect"]
newL = [x.lower() for x in L if len(x) > 4]

# --- 6d) [EXTRA] SET
'''
Working with the same list L = ["Practice", "Makes", "us", "100%", "Perfect"] 
create a set (call it unique_lenghts) which contains as elements of the set 
lengths each string.

Hint: use set comprehension instead, i.e. {} instead of [].
'''
unique_lengths = {len(x) for x in L}

# --- 6e) [EXTRA] DICTIONARY
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
Create a fn: 
def absVal(x): 
which finds an absolute value of a numeric type (int/float).  
Test the function on: ans = absVal(-10)
'''    
# Function Definition Goes Here:
def absVal(x): 
    if x < 0:
        return -x # note do not use abs() here as we are trying to wrte an abs
    # function ourselves
    else:
        return x
# Function Call Goes Here:
ans = absVal(-10)
print(ans)


# --- 7b) MINIMUM NUMBER 
# Function Definition Goes Here:
def minNum(x, y):
    if x <= y:
        return x
    else:
        return y
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
    return -maxNum(-x, -y)

# Function Call Goes Here:
ans  = minNum(2, 5)
ans2 = minNum2(2, 5)
print(ans, ans2) # 2 2
   

# --- 7d) [EXTRA] MINIMUM NUMBER FROM A LIST OF NUMERICS
# Function Definition Goes Here:
def minList(L):
    minVal = L[0]
    for ii in L[1: ]:
        minVal = minNum(minVal, ii) # calculate current min value and store it
    return minVal
# Function Call Goes Here:
L = [1, 2, 3, 4, 5]
ans = minList(L)
print(ans) # 1

# --- 7e) MAXIMUM NUMBER FROM A LIST OF NUMERICS
# Function Definition Goes Here:
def maxList(L):
    maxVal = L[0] # current max value
    for ii in L[1:]: # compare to each element of list from 1 to end
        ## OPTION 1
#        if ii > maxval:
#            maxval = ii
        ## OPTION 2
        maxVal = maxNum(maxVal, ii)
    return maxVal
# Function Call Goes Here:
L = [1, 2, 3, 4, 5]
ans = maxList(L)
print(ans) # 5



# -----------------------------------------------------------------------------
#%% Q EXTRA SLIDES WHILE LOOP
# a) 
'''
Write a for and a while loop to print numbers 10 to 1 in descending order. 
Which loop has fewer lines of code? 
Which loop is better suited to the task and why?
'''
# for loop is shorter and is better suited since we know number of iterations.    
for ii in range(10,0,-1):
    print(ii)

# while loop
counter = 10
while (counter >= 1):
    print(counter)
    counter -= 1
    
    
# b) 
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
# One way of solving is a for loop
n    = 8 
L    = [0] * n # create a list of length n with 0 entries
L[0] = 1
L[1] = 1
for ii in range(2,n):
    L[ii] = L[ii-1] + L[ii-2]
print(L)    
    

# c) EXTRA 
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
# A different way of solving  is with a while loop
a, b = 1, 1
n    = 8
L    = [0] * n # create a list of length n with 0 entries
L[0] = a
L[1] = b
counter = 1
while counter < (n-1): 
    # Next, each operation is performed before either a or b is overwritten:
    a, b         = b, a+b # a becomes b; b becomes a+b 
    L[counter+1] = b      # remember indexing starts from 0!
    counter     += 1
print(L)

# for loop is shorter and is better suited since we know number of iterations.   


# d) EXTRA 
'''
Use a while loop to print out the first n = 6 elements of the Fib series 
(i.e. up to and including value 8). Use a boolean variable done inside the 
CONDITION statement.
Hint 1: initialise done = False (see Slide 35) and use while not done as the 
        loop header. 
Hint 2: stop execution either using keyword break or setting done = True at the 
        relevant location in code.
'''
#stop printing after n=6 (ie value 8 is printed)
a = 1
b = 1
n = 1
done = False
while not done:
    print(a) 
    if (n == 6):
        break
    n = n + 1
    a, b = b, a+b
    
# e) EXTRA
'''
You have a list L = [1,2,4,5,4,5,6]. The task is to establish the first 
position at which value 5 is in the list using a while loop. If that value is 
not in the list, print a message to that effect. 
'''
L = [1, 2, 4, 5, 4, 5, 6] 
num   = 5 # number to be found  
index = 0
found = False
while not found:
    if L[index] == num:
        found = True
        print("Index:", index)
    elif index == (len(L) - 1):
        print('Number not in list')
        break # come out of current (while) loop
    index += 1    
