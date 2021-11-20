#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Dr Ekaterina Abramova
Document : LAB Questions
"""

#%% Q1
# See PDF

from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
html = urlopen("https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm")
bs = BeautifulSoup(html.read(), 'lxml') 

data = bs.find("div",{"class":"col-xs-12 col-sm-8 col-md-8"}).text.split("\n")[1:6]

ss = "\n".join(data[:4])

#%% Q2
# See PDF

months = {'Jan':1, 'Feb':2, 'Mar':3}
for k in months.keys():
    print(k, ":",months[k])

algo = {}
k=3
N = 100
metric = 'Euclidian'

algo["KNN"] = (k, N, metric)
len(algo)

from L3_Fed_15Mar2020_str import s
import re


words_list = re.sub("[,.-]", "", ss).lower().split(" ")
words_count = {}
for w in words_list:
    words_count[w] = words_count.get(w,0)+1


from lmdict import lmdict
score = 0
for k in words_count.keys():
    if k in lmdict["Positive"]:
        score+=words_count[w]
    elif k in lmdict["Negative"]:
        score-=words_count[w]
print(score/len(words_list))
    

#%% Q3
# See PDF

# FILL IN ANSWER HERE 


#%% Q4
# See PDF

# FILL IN ANSWER HERE 


#%% Q4 NUMPY
import numpy as np
import matplotlib.pyplot as plt
# a) --------------------------------------------------------------------------
'''
This qn is on the simulation of random walks (see wiki page for further info): 
https://en.wikipedia.org/wiki/Random_walk

Let's begin by simulating a simple random walk with 1000 steps, starting at 0 
with steps of 1 and -1 occuring with equal probability. The code uses regular
approach of using for loops and base R methods (together with numpy random 
number generating facility). 
Run this code understand how it works.
'''
np.random.seed(1234) # fix the random number generator
position = 0         # keep track of aggregate steps observed
walk = []            # list
steps = 1000         # number of steps in a single walk
for ii in range(steps):
    # randint(low=0, high=2). Remember max number will be high-1
    if np.random.randint(0, 2): 
        step = 1  
    else: 
        step = -1
    position += step # add observed step to total steps
    walk.append(position) # store current step total 


plt.plot(walk[:100], 'gx-')
plt.title('Random Walk Simulation', fontsize = 20)
plt.xlabel('Step', fontsize = 15)
plt.ylabel('Value', fontsize = 15)
plt.show()

#  b) -------------------------------------------------------------------------
'''
A walk is a cumulative sum of the random steps and therefore could be evaluated
as an array expression, without using for loops. Let's progress to using numpy 
for solving the above task. 
'''
# i) Use appropriate numpy random function to generate integers 0, 1 as many 
#    times as there are steps, call this variable draws:
draws = 

# ii) Next create a variable called steps, that will contain -1 or +1 depending
#    on whether at each respective position draws variable contains 0 or 1. 
#    Hint: review the use of np.where() method on Slide 4. 
steps = 

# iii) Lastly, obtained a single walk using the steps variable, noting that it
#    is the accumulated sum of steps. 
#    Hint: review mathematical methods on Slide 7 to select a suitable one
walk = 

# Use the code provided to plot the first 100 eleemtns of the walk obtained 
plt.plot(walk[:100], 'rx-')
plt.title('Random Walk Simulation', fontsize = 20)
plt.xlabel('Step', fontsize = 15)
plt.ylabel('Value', fontsize = 15)
plt.show()

# iv) Extract min and max observed values from walk. Find the index at which 
#     min and max occur. (see Slide 7 for help)
 



# v) Compute the first time random walk reached over 20 (either +ve or -ve)
#    Hint1: find boolean array of True and False for where element is above
#           20 in absolute value. (see Slide 6)
#    Hint2: find the index at which the first True value is observed (remember
#           False is treated as 0 and True as 1 in programming).
