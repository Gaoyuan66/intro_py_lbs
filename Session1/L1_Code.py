#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Dr Ekaterina Abramova
Lecture 1, Code from the slides
"""

# Optional Settings Instructions:
"""
Open Python Preferences (on mac top left button, called 'python'; for Windows
                         it is called Tools)
 
1. 'Appearance' 
    set editor settings such as background colour, text size.
    
2. 'Editor -> Advanced Settings -> Edit Template for new files'
    set welcome docstring string (first few lines of code isndie the quotes).
    Enter your name and year etc. Press SAVE. Close template.

3. 'Current Working Directory' -> Startup
    Go to 'The following directory' option, andnavigate to our folder called 
    Code which you created during preliminary work.
    Press Apply, OK.
"""


#%% 1. I am a Cell (it gets highlighted in yellow)

# Comment: Viewing output in Console/ Recalling variable content
# Run lines 1-by-1 by clicking anywhere on the lin & pressing black button (F9)
15       # output created but 15 not stored into memory
x = 15   # create a variable which is stored into memory. It contains value 15 
x        # recalling variable content (way 1)
print(x) # recalling variable content (way 2)

# Now can perform operations on the variable which you have stored into memory
y = x**2 + 3/2 - 5**3 # using x in an expression


#%% 2. Python Help from Console
""" 
INSTRUCTIONS:
In Console type an object you would like to read documentation on followed by ?
object?

Examples:
   x?   # help on the variable you created (it will tell you it contains value 
          15 and describe what is an integer)

For a more detailed information, use the help facility
   help(x)
"""


#%% POOR PROGRAMMING PRACTICES !!!! 
# THIS SECTION NEEDS CORRECTING (i.e. comment out the errors)

#1. BAD INDENTATION. 
# Only indent code when you know is it necessary - loops, functions, classes.
   x3 = "Hello World!" # Here we get a warning triangle, but code still runs. 
# Bad indentation can cause in Error.
 
#2. BAD VARIABLE NAMES 
# Attempting to use reserved words causes an ERROR!
for = 15 
and = "abc"


# QUESTIONS FOR THE CLASS:
'''
a)	What are two different ways of documenting code? 
b)	When should each way of documenting code be used?
c)	Give an example of keyword. Why is it important to know what keywords are? 
d)	In Spyder where do you type code (Script or Console) in order to save it as 
    a file?
e)	What language does the Console of Spyder interpret?
'''














'''
ANSWERS:
a) 
Comments - the hash # sign – everything after the hash will be ignored by the 
   Python Interpreter for that line only e.g. 
# I am a comment line
    
Docstrings - use triple quotes, we call this a doc string: everything in 
   between quotes is ignored by the Python Interpreter. 

b) 
Comments should be used to remind yourself/others what that a line of code does

Doc string should be used to give instructions on how to use a function /object 
   you have programmed (to be covered) – typically given at the top of the code

Another use of doc string is to debug code – if you do not know which line of 
   code failed, comment out e.g. 2nd half of code and re-run. Keep uncommenting 
   code and you will see at which stage the bug re-appears.

c) for, and

d) Script: we type all of the code / answers etc in the Script, becasue the 
   code can be saved to a file and re-loaded for later use.
   
   Console: use to observe output of executed commands from Script pane; also
   use for quick one line checks, e.g. print(x) or x**2 etc

e) Python syntax only. Note it does not interpret commands you would execute in 
   your Terminal (black window) as that is machine command line interpreter.
   
   However, when using line magic commands we can make it iterpret command line 
   commands also.
'''


# -----------------------------------------------------------------------------
#%% MAGIC COMMANDS
'''
Copy paste one command at a time into console and execute:
%quickref
%magic
%reset
%clear
%ls
%pwd
%time
%timeit
%who 
%whos
%conda --version
'''


# -----------------------------------------------------------------------------
#%% IMPORTING LIBRARY
#1. import PACKAGE -> load a whole package (good practice)
import numpy                # load numpy package
y1 = numpy.array([1, 2, 3]) # create an array 

#2. import PACKAGE as SHORTHANDNAME -> load a whole package (good practice)
import numpy as np          # load numpy module and give it a shortered name
y2 = np.array([1, 2, 3])    # create an array 

#3. from PACKAGE import NAME -> statement specific import (good practice)
from numpy import array     # load a particular function from numpy package
y3 = array([1, 2, 3])       # create an array 

#4. from PACKAGE import * -> import all items (BAD practice)
from numpy import *
z1 = round(6.7)    # rounds float to 7         
# here Python uses base distribution's round() function which results in an int
# i.e. we may not get the intended answer (e.g. wanted float but got int!)
# If we actually wanted to avoid the clash, do not do wild card imports, i.e.
z2 = np.round(6.7) # answer is 7.0 float

# List components of the loaded library
dir(np)

# Example package math (access number pi from the package)
import math # load package
dir(math)   # check available resources
math.pi     # access number pi


# -----------------------------------------------------------------------------
#%% SCIENTIFIC FLOAT NOTATION
x1 = 10000000000   # 10,000,000,000   (10 billion) 
type(x1)           # int
x2 = 10e9          # 10,000,000,000.0 (note by default this is a float)
type(x2)           # float

eps1 = 0.0001 # 0.0001
eps2 = 1e-4   # 0.0001


# -----------------------------------------------------------------------------
#%% LOAD MODULE EXAMPLE
# Say in our current script we have a variable:
covid19_uk_total = 9.1e+06 
print(covid19_uk_total)

# Load speedOfLight's contents:
import covid
print(covid.covid19_uk_total)

error = covid19_uk_total - covid.covid19_uk_total
print(error)


# -----------------------------------------------------------------------------
#%% OBJECTS (ID) 
# --- IMMUTABLE OBJECT TYPES (e.g. integer)
id(15) # 4423820800 (you'll have a diff num)
id(15) == id(15) # True 

x = 15 
y = x  # Does not create another object!
id(x)  # 4423820800
id(y)  # 4423820800
x is y # True (i.e. x and y refer to same obj)

z = "abc"
z is y # False

# --- MUTABLE TYPES (e.g. list)
# Guaranteed to refer to 2 unique, diff lists
L1 = []   # empty list 1
L2 = []   # empty list 2
L1 is L2  # False 

# Caution: assigns the same object to both L1 and L2!
L1 = L2 = [] # Assignment on the same line
L1 is L2  # True

#%% OBJECTS (TYPE) - column in Variable Explorer
print(type(1))    
print(type("abc")) 
print(type(5.3))   
print(type(True))  

#%% OBJECTS (VALUE)
# relational operator checks value equality 
7 == 7
"abc" == "abc" 


# --- Mutability and Aliasing
myList = [1,2,3]
id(myList)    # 4875452168
myList[0] = 10
id(myList)
print(myList) # same id kept: 4875452168 showing lists are mutable

s = "abcdef"
s[0] = "z"    # causes an error since strings are immutable types
id(s)
s = "zbcdef"
id(s)         # (not as before therefore is a new object)


# --- MUTATING LISTS
# Mutate a list by overwriting a value to a new value
L = [1,2,3] # lists are mutable types
id(L)       # 4954068864
L[0] = 10   # change element 0 to 10
print(L)    # [10,2,3]
id(L)       # 4954068864 id did not change

# Mutate a list by extending the list using append() method (function)
L = [1,2,3] 
id(L)        # 4960011840
L.append(10) # change element 0 to 10
print(L)     # [1,2,3,10]
id(L)        # 4960011840 id did not change

# NO MUTATION:
L1 = [1,2,3] 
id(L1)       # 4960011584
L2 = [4,5,6] 
id(L2)       # 4959997824
L3 = L1 + L2 # concatenate 2 lists (put them together)
id(L3)       # 4953986304 (i.e. a new object, no mutation)


# --- ALIASING
# immutable types
a = 5
b = a # an alias is created
id(a) == id(b) # True (both identifiers reference the same obj)

a = 5
b = a
b = 3 # the alias is broken
id(a) == id(b) # False


# mutable types
L1 = [1,2,3]
L2 = L1 # alias created
print(L1 is L2) # True (both reference the same object)

L1 = [1,2,3]
L2 = list(L1) # typecasting L1 to a list breaks alias
L2 is L1 # False

L1 = [1,2,3]
L2 = [1,2,3] # creating a new list guarantees a unique object
L2 is L1 # False


# EXAMPLES OF ALIAS BEHAVIOUR
# --- ALIASING EXAMPLE 1
L1 = [1,2,3]
L1 = L2    # create an alias
L1[0] = 10 # mutate element 1 in L1
print(L1)  # [10, 2, 3]
print(L2)  # [10, 2, 3]

# No aliasing if create to different objects
L1 = [1,2,3]
L2 = [1,2,3] # assign explicitly
print(L1 is L2) # False (variables point to different objects)
L1[0] = 10 # mutate element 1 in L1
print(L1)  # [10, 2, 3]
print(L2)  # [1, 2, 3]

# --- ALIASING EXAMPLE 2
L1 = ["LBS", "Imperial", "Oxford"]
L2 = [1,2,3, L1] # [1, 2, 3, ['LBS', 'Imperial', 'Oxford']]
L1.append("Cambridge")
print(L1) # ['LBS', 'Imperial', 'Oxford', 'Cambridge']
print(L2) # [1, 2, 3, ['LBS', 'Imperial', 'Oxford', 'Cambridge']]

# --- No alias when obtaining chunks:
L1 = [1,2,3,4,5]
L2 = L1[0:2]
L2.append("abc") # only seen in L2


# --- [EXTRA] MUTABILITY 
'''
Containers: objects that contain references to other objects e.g. tuples, lists 
and dictionaries. The references are part of a container’s value. 

The value of an immutable container object that contains a reference to a 
mutable object can change when the latter’s value is changed; however the 
container is still considered immutable, because the collection of objects 
it contains cannot be changed.

So, immutability is not strictly the same as having an unchangeable value, it 
is more subtle.

In most cases, when we talk about the value of a container, we imply the values 
not the identities of the contained objects; however, when we talk about the 
mutability of a container, only the identities of the immediately contained 
objects are implied. So, if an immutable container (like a tuple) contains a 
ref to a mutable object, its value changes if that mutable object is changed.
'''

# immutable type (tuple) contains refernces to mutable objects in this ex
# when mutable object is mutated, the change is reflected in tuple too.
L1 = [1,2,3]
T = (14, L1)
L1.append(11)
print(T) # (14, [1, 2, 3, 11])


# --- [EXTRA] HASH 
'''
In addition to ‘value’, some objects have ‘hash value’, which means they can be 
used as dictionary keys (and stored in sets). 

hash(a) -  returns a number based on the object's value. 

The hash of an object must remain the same for the lifetime of the object, so 
it only makes sense for an object to be hashable if its value is immutable 
(either because it's based on the object's identity, or because it's based on 
contents of the object that are themselves immutable).
'''

L = [1,2,3]
hash(L) # unhashable type: 'list'

T1 = (1,2,3)
hash(T1) # 529344067295497451

# However if a list is inside the tuple, cannot have a hash.
T2 = (1,2,3,[4,5,6])
hash(T2) # unhashable type: 'list'


#%% FUNDAMENTAL DATA TYPES
# ----------------------- None type -------------------------------------------
x1 = None
type(x1)      # NoneType

# ----------------------- Numeric types ---------------------------------------
x2 = 1
x3 = (1)      # round about way of defining an integer 1
type(x3)      # int

b1 = True 
b2 = False 
b3 = (True)
type(True)    # bool

x4 = 1.
x5 = 1.0
x6 = (1.2)
type(x6)      # float

# ----------------------- Sequences -------------------------------------------
s = "abc def" # string - characters
type("I am a string") # str 

# tuple - immutable
T1 = () 
T2 = (1,) 
T3 = (1,"a")
T4 = 1,"a"
T5 = (11,13,7)
type(T4)      # tuple 

# list - mutable
L = []
L = [1]
L = [1,None]
listL = [1,2,3]
type(listL)   # list 

# empty frozen set
S = frozenset()

# set
S = set() 
# S={1,"a",[]} # note: this generates an error since a set can only contain immutable types, but list is a mutable type.
mySet = {"Cat", "Cat", 15, 12.5, (1,2,3)}
print(mySet)  # items cannot be repeated (unordered)
type(mySet)   

# Example of mutating a set
S1 = set([1, 2, 3])
id(S1)   # 5049453024
S2 = set([4, 5, 6])
id(S2)   # 5049453248
S2 |= S1 # find union between S1 and S2 but mutate S2
id(S2) # 5049453248

# Mapping - dictionary
D = {}    
D = {"A":1,"B":2}
stockDict = {'Open':10.5, 'High':11.3, 'Low':9.9, 'Close':11.1}
type(stockDict) # dict (unordered)


#%% TYPECASTING - built-in types

# from float to int
x1 = 15.9
y1 = int(x1) # 15
# from bool to int
x2 = True
y2 = int(x2) 
# from str to int
x3 = "5"
y3 = int(x3) 

# from str to float
type(float("4.0")) # type is float

# from float to string
type(str(4.0)) # type is str

# from range to list
type(list(range(10)))

x4 = range(5)
print(list(x4)) # [0, 1, 2, 3, 4]

t1 = (('a',1),) # a tuple t1 containing a tuple ('a',1). Note need a comma otherwise will end up with a tuple t1 with 2 elements: 'a' and 1.
dict(t1)

t2 = (('a',1),('b',2)) # a tuple t2, containing 2 tuples: ('a',1) and ('b',2)
dict(t2)


# -----------------------------------------------------------------------------
#%% BUILT-IN FUNCTIONS - FILES -----------------------------------------------:

# Equivalent ways to open a file for READING. 
fileHandle = open("USD.csv") # Note name 'fileHandle' is up to you.
f = open("Subjects.csv")  # default is 'reading'.

f = open("Subjects.csv") 
contentsStr = f.read()    # one long string with all contents

f = open("Subjects.csv")  # reload file, since f.read() reads whole contents 
lineStr = f.readline()    # one line from file

f = open("Subjects.csv") 
linesList = f.readlines() # one string per list entry

# close file handle to free up memory 
f.close()


# -----------------------------------------------------------------------------
#%% METHODS FOR STRINGS ------------------------------------------------------:
# Remember strings are immutable type! Assign all results to new a string.
s = "daddad"
print(s.strip('d'))  # adda
print(s.rstrip('d')) # dadda
print(s.lstrip('d')) # addad
print(s)             # daddad (s is immutable! Unchanged)

s = 'Today is a great day!'
L = s.split() # split by whitespace, result is a list: 
              # ['Today', 'is', 'a', 'great', 'day!']
print(s)      # s is immutable, therefore original string is unchanged:
              # 'Today is a great day!'

s    = 'KING ABDULLAH NAMES PRINCE CROWN PRINCE\n'
s2   = s.lower()      # move all letters to lower case
s3   = s2.strip('\n') # removes '\n'
L    = s3.split(' ')  # we could explicitly write in the character by which
# we want to split, in this case a space. Result is a list:
# ['king', 'abdullah', 'names', 'prince', 'crown', 'prince']


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
L4 = [0]     # a list with a single entry 0
L5 = L4 * 5  # replicate list L7 five times
print(L5)    # a list with 5 zeros, i.e. [0, 0, 0, 0 ,0]

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
x = 5; L = [1,2,3]
if x == 5:
    print("x is 5")
    if (len(L) != 0):
        print(L)
elif x == 10:
    print("x is 10")
else:
    print("x is not 5 or 10")
# x is 5
# [1, 2, 3]


#%% [EXTRA] PRINT FUNCTION - OVERVIEW
print('Hello World')
print("Hello World") # Note: enclosing quoatation marks are not printed

x = 13.772
print("String 1 " + "String 2") # Note space is needed after 1
print("Universe is", x, "Billion Years Old!") # Use comma to separate output
print("Age of the universe is: " + str(x)) # Type cast float to string first

print('Bank\'s Address') # use \' for single quote inside a 'string'
print("Bank's Address")  # use  ' for single quote inside a "string"
print("Was it a \"great\" idea?") # use \" for double quotes inside a "string"


# ---- Continue on same line
x = 2
print("Input x is:", x, end=" ")
y = x**2
print("Output y is:", y)
# Input x is: 2 Output y is: 4

for ii in range(3):
    print('Number is:', ii, end="! ")
# Number is: 0! Number is: 1! Number is: 2! 
    

# Splitting across lines is not allowed:
#print("This is a very long string that I wish to
#      extend all the way to the next line")
# Allowed if use a Doc String:
print("""This is a very long string that I wish to
      extend all the way to the next line""")
# Use newline character \n to place characters following it to next line
print("Contents of first line; \nContents of second line.")

# --- FORMAT WITH % OPERATOR
# 1. To print out rounded floats use %.nf
x = 15.56755421
print("%.2f" % x) # 15.57
print("%.4f" % x) # 15.5676


#%% ASCII TABLE --------------------------------------------------------------:
ord("A")  # 65
ord("B")  # 66
ord("a")  # 97
"A" < "B" # True
"a" > "A" # True
