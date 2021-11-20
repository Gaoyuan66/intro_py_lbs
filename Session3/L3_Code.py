#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Dr Ekaterina Abramova
Lecture 3 : Lecture Slides Code
"""

import numpy as np

#%% DICTIONARIES
# Two ways to create an empty dictionary
d1 = {}
d2 = dict()

months = {'Jan':1, 'Feb':2, 'Mar':3}
dist   = months['Mar'] - months['Jan'] # i.e. 3 - 1 = 2

months['Dec'] = 12            # add entry
months['Jan'] = 'BEST MONTH!' # change entry
print(months) # {'Jan': 'BEST MONTH!', 'Feb': 2, 'Mar': 3, 'Dec': 12}

for ii in months:
    print(ii)
# Jan Feb Mar Dec
    
print(months.keys()) 
# dict_keys(['Jan', 'Feb', 'Mar', 'Dec'])


#%% NUMPY 
a = np.array([np.nan])
a.dtype # ﻿dtype('float64')


#%% NUMPY CREATING ARRAYS
# can create nd array using a tuple
T = (1 ,2, 3)
a = np.array(T)
type(a)

#can create nd array using a list
L = [1, 2, 3]
a = np.array(L)
a2 = np.array([1, 2, 3]) # equivalent to creating a
type(a)
a[0] # 1
a[1] # 2
a[2] # 3
print(a) # [1 2 3]
a        # array([1, 2, 3])

L2 = [L, L, L]           # list of lists 3x3
b1 = np.array(L2)        # the shape & data type is inferred from the data
b2 = np.array([a, a, a]) # equivalent to creating b1
""" both b1 and b2 are:
array([[1, 2, 3],
       [1, 2, 3],
       [1, 2, 3]])
"""

L3 = [L2, L2]    # 2 x (3 x 3)
c = np.array(L3)
"""
array([[[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]],

       [[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]])
"""

a = np.zeros(10)        # vector of 10 0s, note contents are float type 
b = np.zeros((10, 2))   # 10 rows, 2 columns
b2 = np.zeros([10, 2]) # equivalent way of defininig b
c = np.zeros((2, 3, 3)) # 2 depth, 3x3 matrices

a = np.empty(10) # vector of 10 uninitialised elems; contents are float type
# these typically are 0 but do not have to be. returns uninitialised values.
# This way of creating a is the quickest, so should be used where speed is imp.
b = np.empty([10, 2]) # 10 rows, 2 columns equivilenatly np.empty((10,2))
'''
array([[1.28822975e-231, 1.28822975e-231],
       [4.94065646e-323, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000,             nan],
       [1.28822975e-231, 1.28822975e-231],
       [1.28822975e-231, 3.11108686e+231],
       [4.33592627e-311, 1.39067116e-308]])
'''

a = np.ones(10)      # vector of 10 1s, note contents are float type 
b = np.ones((10, 2)) # 10 rows, 2 columns of 1s equivilenatly np.ones([10,2])

a = np.arange(6)     # array range function (equivalent range for arrays)

# ensure indended shape is compatible with original
b = np.arange(6).reshape(2, 3) 
c = np.arange(18.0).reshape(2, 3, 3) # depth 2, matrix 3x3


c = np.arange(10)   # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
d = np.where(c < 5) # single elem tuple with indices for which cond. was True 
print(d) # (array([0, 1, 2, 3, 4]), ) 

e = np.where(c < 5, 1, -1) # similar to excel, if true ans 1, else -1
print(e) # array([ 1,  1,  1,  1,  1, -1, -1, -1, -1, -1])

f = np.arange(6)
g = np.where(f < 5, 1, -1) # array([ 1,  1,  1,  1,  1, -1])


#%% VECTORIZATION
x = np.array([[1,2],[3,4]])
x ** 2 # square each element without needing for loops
x > 2  # returns boolean array where condition is True
x - x  # element-wise again

# Element-wise boolean operations for arrays of equal lengths
y = np.array([[True, True], [False, False]])
z = np.array([[False, True], [False, True]])
~ z   # boolean not for arrays (reverse the logic of z)
y & z # boolean and for arrays (only True where both operands are True)
y | z # boolean or for arrays (for each elem: True if either operand is True)


#%% UNIVERSAL FUNCTIONS
x = np.array([1,2,3,4])
np.square(x) # returned values are: array([ 1,  4,  9, 16])
x # note x is unchanged: array([1,2,3,4])
np.square(x, out = x) # optional arguement out means affect array in-place
x # note x is changed straight away: array ([[1,4,9,16])


a = np.arange(1,10).reshape(3,3)
b = np.arange(1,10).reshape(3,3)
"""
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
"""
# unary universal functions
np.sqrt(a)
np.square(a)
np.abs(a)
np.exp(a)
np.log(a)
np.sign(a)
np.isnan(a)
np.isfinite(a)
np.isinf(a)
np.logical_not(a)
# binary universal functions
np.power(a,b)
np.multiply(a,b)
np.divide(a,b)
np.floor_divide(a,b)
np.add(a,b)
np.subtract(a,b)
np.maximum(a,b)
np.fmax(a,b)
np.minimum(a,b)
np.fmin(a,b)
np.logical_and(a,b)
np.logical_or(a,b)


#%% MATHEMATICAL / STATISTICAL AND BOOLEAN METHODS
a = np.array([[0,1,2], [3,4,5], [6,7,8]])
"""
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
"""
a_sum  = a.sum()         # 36 (note result is an int)
a0_sum = a.sum(axis=0)   # array([ 9, 12, 15])
a1_sum = a.sum(axis=1)   # array([ 3, 12, 21])

a_mean  = a.mean()       # 4.0 (note result is a float)
a0_mean = a.mean(axis=0) # array([3., 4., 5.])
a1_mean = a.mean(axis=1) # array([1., 4., 7.])

a_std  = a.std()         # 2.581988897471611
a0_std = a.std(axis=0)   # array([2.44948974, 2.44948974, 2.44948974])
a1_std = a.std(axis=1)   # array([0.81649658, 0.81649658, 0.81649658])

a_cumsum  = a.cumsum()   # array([ 0,  1,  3,  6, 10, 15, 21, 28, 36])
a0_cumsum = a.cumsum(axis=0) # column-wise
# array([[ 0,  1,  2],
#        [ 3,  5,  7],
#        [ 9, 12, 15]])
a1_cumsum = a.cumsum(axis=1) # row-wise
# array([[ 0,  1,  3],
#        [ 3,  7, 12],
#        [ 6, 13, 21]])

np.min(a_cumsum)    # 0
np.argmin(a_cumsum) # 0
np.max(a_cumsum)    # 36
np.argmax(a_cumsum) # 8


# --- Below we will take a look at how a.sort() compares to np.sort(a) --------
np.random.seed(1234)
b = np.random.randn(5) 
# array([ 0.47143516, -1.19097569,  1.43270697, -0.3126519 , -0.72058873])
b.sort() # b changes directly without re-assignment (method operats in-place)
# array([-1.19097569, -0.72058873, -0.3126519 ,  0.47143516,  1.43270697])

np.random.seed(1234)
b = np.random.randn(5) 
b_sorted = np.sort(b)
b # b is unchanged (top level numpy function does not act in-place)
# array([ 0.47143516, -1.19097569,  1.43270697, -0.3126519 , -0.72058873])
b_sorted # we had to assign result to a new varaible to store stored values
# array([-1.19097569, -0.72058873, -0.3126519 ,  0.47143516,  1.43270697])

bools = np.array([False, False, True, False])
bools.any() # (is at least 1 elem True?) True
bools.all() # (are ALL elems True?) False


#%% RANDOM NUMBER GENERATION
np.random.seed(1234)

# --- Permutations ------------------------------------------------------------
# Function takes a single input and shuffle numbers 0 to n-1
np.random.permutation(5) # array([4, 0, 1, 2, 3])

a = np.array([1, 4, 9])
# Function can also receive array as input:
np.random.permutation(a) # shuffle elements randomly array([4, 9, 1])
a # array([1, 4, 9]) original a unchanged, as permutation does not act in-place

# --- Shuffle -----------------------------------------------------------------
a = np.array([1, 4, 9])
np.random.shuffle(a)
a # array([1, 9, 4]) # shuffle performs operation in-place, original a changed

np.random.rand(2,3) # takes tuple as input to specify dimensions of output arr
# remember that both 2,3 and (2,3) are tuples. 
'''
array([[0.86066977, 0.15063697, 0.19851876],
       [0.81516293, 0.15881535, 0.11613783]])
'''

# --- Randint -----------------------------------------------------------------
np.random.randint(low=3, size = 10) # highest value allowed is low-1    
# array([0, 0, 0, 1, 0, 1, 2, 2, 2, 0])

np.random.randint(low=3, high=10, size = 10)# highest value allowed is high-1  
# array([6, 7, 8, 5, 9, 5, 6, 6, 3, 4])

np.random.randint(5, size = (2, 5))
'''
array([[3, 0, 3, 2, 3],
       [4, 1, 3, 3, 3]])
'''
np.random.randint(5, 10, size = (2, 4))
'''
array([[7, 6, 8, 9],
       [7, 8, 9, 6]])
'''

# --- Distributions -----------------------------------------------------------
np.random.randn(5) 
# array([-0.31162665,  0.50359176,  0.28529568,  0.48428811,  1.36348151])
np.random.randn(2, 5) 

np.random.normal(loc = 0, scale = 0.25, size = (2,3))
'''
array([[-0.20810577,  0.02851485,  0.30455072],
       [-0.22264814,  0.04136115, -0.28186743]])
'''

n, p = 10, 0.5
np.random.binomial(n, p, 100)

np.random.uniform(-1, 5, 100)
