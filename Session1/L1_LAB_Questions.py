#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Dr Ekaterina Abramova
Lecture1 : LAB QUESTIONS
"""

# Load libraries at the top of the file (good coding practice) 
import re # regular expressions library, we will need it for processing strings


#%% Q1 USING LIBRARIES
#%% --- 1a) 
'''
Practice 3 valid ways of importing the math module and using the sqrt() 
function to find sqrt of 25, store result to a varaible called 'x'.

After you finish practicing each import command, delete the current objects
from the session using %reset magic command in the Console. This will ensure
that your previous import command is erased and you are starting fresh. 
'''
# Way 1:
import math
x = math.sqrt(25)

# Run %reset in the Console

# Way 2:
from math import sqrt
x = sqrt(25)
# Run %reset in the Console

# Way 3:
from math import *
x = sqrt(25)
# Run %reset in the Console

# NOTE: when you need to use a library, it is best to make all of the import
# commands at the top of the file, this is good coding practice.

#%% --- 1b) 
'''
Given your knowledge of the mathematical operators, what is another quick way 
of finding the sqrt of 25 without using a library?
'''
25**2

#%% --- 1c) 
'''    
Import both sqrt and pi from the math library. Print the value pi.
'''
from math import sqrt, pi
print(pi)

#%% --- 1d) 
'''
Import the numpy library and list all of the available resources 
(i.e. variables and functions available in the library).
'''
import numpy as np
dir(np)

#%% --- 1e) 
'''  
Next you will practice how to import contents of another file into your Script.
You have an lmdict.py file, which contains a dictionary with positive and 
negative words, to be used in sentiment analysis. 

Import the 'lmdict.py' module into your current Script, using command
import library

List all of the resources (you will see functions with _ _ NAME _ _ these are
meant to be called internally, ignore them). You will also see the varaible 
contained in that file: lmdict (as it happens, variable has the same name as 
                                the file, which is ok).

Store the variable lmdict to a new variable in your Script, call your variable 
sentimentDictionary. 

Hover over the sentimentDictionary variable in your Variable Explorer & double
click on it. The variable will open up. You will see it is a dictionary with 2
elements, each element contains a list of words.

It is now ready for use.
'''
import lmdict
dir(lmdict)
sentimentDictionary = lmdict.lmdict

#%% --- 1f) 
'''
What is the quicker way of importing the variable lmdict from the file lmdict?

i.e so that you can use the varaible directly without first storing it to a new
variable, sentimentDictionary as we did above. 
'''
from lmdict import lmdict


#%% Q2 OBJECTS
#%% --- 2a) 
'''
Make a comment on:
    Can an object's identity, type, value be changed? 
'''
# identity is a address on RAM. it will change when the value changes.
# Type and value also can be changed.

#%% --- 2b)
'''
You have an object baseRateBOE = 0.1. 
Establish what is this object’s identity, type and value.
'''
baseRateBOE = 0.1
id(baseRateBOE)
type(baseRateBOE)
print(baseRateBOE)

#%% --- 2c) [Identity practice] 
'''
You have another object baseRateFED = 0.25. 
Establish if these two objects (baseRateBOE and baseRateFED) point to the same 
location in memory.
'''
baseRateFED = 0.25
id(baseRateFED) == id(baseRateBOE)
baseRateFED is baseRateBOE

#%% --- 2d) [Value practice] 
'''
Perform an equality check to establish if base rate in UK equals that of USA. 
Assign the result to a variable with identifier ratesAreEqual. 
'''
# ratesAreEqual = 

#%% --- 2e) 
'''
Create two lists L1 and L2, such that:
    (version a) alias between two lists is formed.
    (version b) no alias is present.
    
In each case prove that it was done as requested. 
'''
# version a
L1 = []
L2 = L1
L1 is L2

# version b
L1 = []
L2 = []
L1 is L2


#%% --- 2f) [EXTRA] Aliasing (Lists)
'''
You are given two lists L1 and L2.
Examine whether the two variables point to the same object?

The fact that L2 contains a reference to L1 inside of it is important!
Examine whether the L1 and 2nd element of L2, you can access it with L2[1], 
point to the same object?

Mutate an element in L1, e.g. L1[0] = 10
Print contents of L1 and L2. This is an example of aliasing.
'''
L1 = [1,2,3]
L2 = ["abc", L1] # List with 2 elements: 'abc' and [1, 2, 3]


#%% Q3 TYPECASTING
# --- 3a) 
'''
Typecast float 16.7 to an integer, check the answer, why is it 16 and not 17 
'''   
int("16.7")
  
#%% --- 3b)  
'''    
Typecast string “100.76” to a float
'''    
float("100.76")

  
#%% --- 3c) 
'''   
Typecast a string "Data Science" to a tuple, list, set. 
Observe the order of the items in the set – this is what we mean by ‘unordered’
'''    
s = "Data Science"
T = tuple(s)
L = list(s)
S = set(s)
print(T)
print(L)
print(S)


# -----------------------------------------------------------------------------
#%% Q4 FUNDAMENTAL DATA TYPES
#%% --- 4a) None Type 
'''
None is NOT the same as 0, or False or an empty string "". None is a datatype 
of type NoneType. Check for yourself by running commands below (i.e. printing 
out the type of each object: None, 0, False, ""): 
'''
print(type(None)) # it has a type of its own
print(type(0)) 
print(type(False)) 
print(type(""))

#%% --- 4b) Numeric Types
'''
Examine the type of variable created when initialising y1 = 15.0 vs. when using 
brackets y2 = (15.0). Did you create a float and a tuple or was it a float in 
both cases? Understand why.
'''
y1 = 15.0 
y2 = (15.0)
# Check each variable's data type
type(y1)
type(y2)

'''
Try again when using a boolean True, i.e. b1 = True and b2 = (True). Did you 
create a bool and a tuple or was it bool type in both cases? Understand why.
'''
b1 = True
b2 = (True)
type(b1)
type(b2)


# Note above is meant to demonstrate that using brackets is an equivalent 
# (but longer) way of creating scalar types. 

#%% --- 4c) Sequences
'''
Create your own example variables for each sequence type (string, tuple, list). 
Ensure that your containers (tuple, list) store inside as elements all of the 
data types allowed for that container. For example: tuple allows elements of 
any type, e.g.: 
T1 = (1, {}, [1,2]) 
contains 3 elements: int 1, empty dictionary {} and list with two elems [1, 2]. 
'''
# your string example
s = "123"

# your tuple example
T = ((1,),(2,))

# your list example
L = [1,2,3,[]]

'''
Next investigate the following: 
i. Put integers inside a string. What happens to them? i.e. are they still 
   integers or do they become a string?
'''
s = "123"
type(s)

'''
ii.	List is commonly used to store data. If you did not want elements of your 
    container to be altered which sequence type would you use instead?
'''
# tuple

'''
iii. Create a new variable T2 = 1, {}, [1,2]. This also creates a tuple just 
as you did above T1 = (1, {}, [1,2]) i.e. creating tuples does not require 
round brackets. 
'''
T2 = 1, {}, [1,2]
type(T2)

# Another example: create variables and check their type. Which one is a tuple?
T3 = 1,
T4 = 1
type(T3)
type(T4)

# Note: this is not the case for lists. You must use square brackets, i.e. 
L = [1, 2, 3] # you are not allowed to drop the sq brackets
type(L)

'''
iv.	What type do you expect to observe if you execute myList = 1, 2, 3? Check:
'''
myList = 1, 2, 3 
type(myList)


#%% --- 4d) Sets and String Methods
# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
'''
i. Create a set variable containing numeric, string and tuple objects.
Next attempt to create another set which also contains a list. 
Why were you not able to do so? 
(Hint: see Slide on Fundamental Data Types, column called “meaning/use”).
'''
S = set([123,"§§",(1,)])
# S = set([[1,2,3]]) throws an error, list is unhashable

# If you attempted to place a list inside a set, it would not work. 
# Reminder this is because sets only allow elems of immutable type. 
# This is because of the way items are looked up inside a set.
# E.g. try:
# S = {[1,2,3]} 

'''
ii.	Initialise a list L = [1, 1, 1, 2, 3]. Typecast this list to a set using 
    operation set(L). Which list elements feature in your new set? Why were 
    some elements of the list dropped? 
'''
L = [1, 1, 1, 2, 3]
S = set(L)
S
'''
iii. Common uses of set data type in Python include membership testing, 
     removing duplicates from a sequence, and computing standard math 
     operations on sets such as intersection, union, and difference. Let's
     examine these operations using Hillary Clinton's email subjects/titles.
'''
# -----------------------------------------------------------------------------
# Open Hillary Clinton's emails dataset containing email subjects/titles.
f  = open("Subjects.csv") # prepare dataset for reading (create file handle, f)
# f  = open("Subjects.csv", encoding = "utf-8") # in case you have trouble
s  = f.read() # read in the dataset into a single string s, using read() func
f.close()     # close the file handle

# Pre-process data: change all charaters of string s to lower case, creating s2
s2 = s.lower().replace('\n',' ').replace('\n',' ')

# keep only characters a-z and white space from string s2; 
# replace any other character with an empty space " "
# Ensure to import your library 're' at the top of this file.
s3 = re.sub("[^a-z ]", " ", s) # note s3 is still a single string of titles

# split s3 into individual words, with each word becoming an element in a list
L = s3.split(" ")

# Establish num of words in list L (i.e. number of words in all email subjects) 
num_words = len(L) # i.e. length of L 

# Typecast list L to a set - this will remove any duplicates from the list, as
# set only allows for unique entries.
# S = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Check number of words in the set S, i.e. note lots of duplicates were removed
# num_elems = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Let's check for membership, i.e. if a given word occurs in the email subjects
word = "classified"
occured = word in S
word2 = "russia"
occured2 = word2 in S
# Membership allows a quick way of checking whether that variable is contained
# in the set.

# -----------------------------------------------------------------------------
# RUN BELOW LINES ONE BY ONE
# Let us return to the Subjects.csv data again, but read it in differently.
# Now lets read the subjects such that each subject is an element of a list.
# Following that we will work on 2 chosen subects using set operations.
f  = open("Subjects.csv")
# f  = open("Subjects.csv", encoding = "utf-8") # in case you have trouble
L  = f.readlines() # note reads data directly into a list. Each subj is an elem
f.close()
# Note that we needed to re-open the csv file handle, since we have previously
# read in all of the data and closed the handle. 

# --- As example, select the 40th subject
subj40 = L[39] # extract 6th subject (referenced by index 5, to be covered today)
subj40 # note the newline character \n that will need to be removed
'''
'YOU DO GREAT WORK - THANKS FOR MAKING OUR HEROS HAVE THE HOMECOMING THEY DESERVED.\n'
'''
# We will process the string such that each word becomes an element of list L40
subj40 = subj40.lower()
subj40
'''
'you do great work - thanks for making our heros have the homecoming they deserved.\n'
'''
subj40 = re.sub("[^a-z ]", "", subj40)
subj40 # anything but letters has been removed and replaced by a ""
'''
'you do great work  thanks for making our heros have the homecoming they deserved'
'''
L40 = subj40.split()
print(L40) # note this is a list!
'''
['you', 'do', 'great', 'work', 'thanks', 'for', 'making', 'our', 'heros', 
 'have', 'the', 'homecoming', 'they', 'deserved']
'''
S40 = set(L40)
print(S40) # we did not have repeating elements in this case, however convert
#            list to a set to use set operations on 2 titles of interest.
'''
{'have', 'homecoming', 'do', 'you', 'our', 'making', 'for', 'they', 'the', 
 'deserved', 'work', 'great', 'heros', 'thanks'}
'''


# --- Now select 3776th subject. Perform the same pre-processing of the string.
subj3776 = L[3775] # extract 3776th subject
subj3776
'''
'CAN YOU DO UPDATE CALL?\n'
'''
subj3776 = subj3776.lower()
subj3776 = re.sub("[^a-z ]", "", subj3776)
L3776 = subj3776.split()
S3776 = set(L3776)
print(S3776) 
'''
{'do', 'you', 'call', 'can', 'update'}
'''

# --- Next we will perform set operations on the two sets S40 and S3776:
# Find words occuring in both subjects (this is intersection). Syntax a & b
# commonWords = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(commonWords)

# Find words contained in both sets. Syntax a | b
# allWords = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(allWords)

# Find words contained in S40 but not in S3776. Syntax a - b
# s40_only = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(s40_only)

# Find words contained in S3776 but not in S40. Syntax b - a
# s3776_only = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(s3776_only)


#%% --- 4e) Dictionaries
'''
A dictionary is a mapping between a set of objects (unique keys) and a set of 
objects (values). The values that the keys point to can be of any type. Think 
of dictionaries as you would of a regular book: words are ‘keys’ and 
descriptions are ‘values’. You can thus look up a key and extract the 
associated value (explanation or in our case content stored under that key).

Create a dict with 3 months of the year as keys: Jan – Mar and put in numerical 
values 1 - 3 into it corresponding value pair.
'''

# months = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# remember that key:value pairs are separated by a comma


#%% EXTRA  Only complete if finished all of the above.
# --- 4f) List 
'''
List is a container which is used to store elements of any type inside of it. 
You are allowed to store lists as elements of another inside a list. 
Given the following 3 sales prices data from cutomers, create another list L,
where each customer forms an element of that list.
'''

deepmind   = [262.75, 273.26, 271.23, 273.36, 266.38]
openai     = [188.47, 186.30, 187.29, 188.21, 184.70]
neuralink  = [28.18,  27.68,   27.49,  27.93,  27.33]

# L = FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Use command len() to establish the number of elements of the list you created


# --- 4g) Set
'''
Let's return to the example where we had a list and were converting it to set.
Note set() function actually changes the data type of variable to a set. Hence
we were able to typecast a list to a set. 

However if you tried to create a set using S = {elem1, elem2, etc} & put a list 
inside, you would get an error. This is because {} operation creates a set from 
the variables specified inside the command. And remember that we are only 
allowed to place immutable types inside a set.
'''
L1 = [1, 1, 1, 2, 3]
# Try this, you will obtain an error
S = {L1}
# However typecasting to a set works, where set() is a function that performs 
# the type change
S = set(L1)


# -----------------------------------------------------------------------------
#%% Q5 OPERATIONS ON SEQUENCES
# --- 5a) Indexing
'''
Indexing extracts a single element from a sequence using square brackets.
Working with Hillary Clinton's eamil titles list, L, extract the following:
    first title
    2nd title
    title at (approx) half way through position
    last title
'''


#%% --- 5b) Slicing
'''
Slicing extracts a subset of the sequence, using L extract the following:
    every 2nd title
    the first half of the data
    the second half of the data
    all titles
    reverse the sequence
'''


#%% --- 5c) Extended Slicing
'''
EXTRA:
(i) 
    Open up L1_Code.py and find the section on Operations on Sequences. 
    There is a list L with 10 elements. Go over 'minus notation section' and 
    'extended slicing section'.
(ii)
    Go over rest of the exampes for operations on sequences.
'''


# -----------------------------------------------------------------------------
#%% Q6 IF-ELIF-ELSE
# --- 6a) If Statement
'''
You are working with a boolean varaible, x = False. 
Write an IF statement to check whether x is equal to 0. 
If the condition is true, print out: 0 is treated as False in Python.
'''
x = False
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Reminder: 1 is treated as True

#%% --- 6b) If-Else Statement
'''
Write an If-ELSE statement which will test whether a number is even or odd, 
assign the result to a boolean variable called isEven. 
Finally print out the isEven variable after you have completed the test.
Use x = 10 and x = 7 to check your code works correctly.
Hint: think about the possible use of the remainder!!
'''
x = 10
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(isEven)    

'''
EXTRA:
You are learning how to code efficiently. Therefore, try to think of a way, to
solve this problem with shorter code, i.e. which only uses the if statement.
'''
isEven = False
# FILL WITH ANSWER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(isEven) 
