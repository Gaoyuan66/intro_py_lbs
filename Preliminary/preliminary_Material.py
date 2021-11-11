#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Dr Ekaterina Abramova
Preliminary Materials : Operators 
"""

# -----------------------------------------------------------------------------
# %% 1. ----------- ARITHMETIC OPERATORS
x1 = 2 + 6 ** 2  # gives 38
x2 = (2 + 6) ** 2  # Change default precedence with (); gives 64

# when operators of the same precedence are on 1 line:
x3 = 2 ** 2 ** 4  # ** operator has right-to-left associativity, gives 65536
x4 = (2 ** 2) ** 4  # use brackets to override default associativity, gives 256

x5 = 3 * 3 % 2  # equivalent to (3*3)%2 NOT 3*(3%2), gives 1
x6 = 3 * (3 % 2)  # use brackets to override default associativity, gives 3

x7 = 12 % 2  # remainder is 0 (i.e. had an even number)
x8 = 13 % 2  # remainder is 2 (i.e. had an odd number)

x9 = 23 // 7  # floor division: divide then round down: 23/7 = 3.2857, round down to 3

# Practice running sub-parts of a long line of code:
# highlight parts of the line then press 'run selection; F9', check output in Console 
# i.e. hihglight each part on line 30 below and press F9, where could be:
# 11 // 3
# (58 - 5) % 3
# (58 - 5) % 3 * 11
x10 = (58 - 5) % 3 * 11 // 3  # gives 7

# %% #2. ----------- RELATIONAL OPERATORS
# Here we are not assigning output to a variable
1 == True  # remember 1 is treated as True (note result is not stored into a variable)

# Here we are assigning output to variable a with different names
a = True  # assigning True to variable called 'a'
a1 = 15 <= 100  # compare 2 numerical values
a2 = 15 < 15
a3 = 15 <= 15
a4 = 15 == 15
a5 = "abc" == "abc def"  # compare character by character
a6 = 10 >= 15
a7 = 5 != 5
a8 = True != True  # compares 1 not equal to 1
a9 = "True" != "True"  # compares characters not equal to characters
a10 = (33 >= 10) * 2  # first evaluates bracket to True (i.e. 1), then 1 * 2
a11 = 33 >= (10 * 2)  # equivalent to 33 >= 10 * 2 , i.e. compares 33 >= 20
a12 = "Brain" == "Brain"  # compares characters one-by-one for equality
a13 = False == True  # i.e. 0 == 1

# %% #3. ----------- LOGICAL OPERATORS
b = True and True
b1 = False and False
b2 = True or True
b3 = True or False
b4 = not False

# 4. Lets combine relational and logical operators in the same expression. Recommended to PARENTHESISE!
b5 = ("abc" == "ABC") and ("abc" == "abc")  # False
b6 = (25 >= 0 and "LBS" == "LBS") or ((not True) and 15 == 0)  # True
b7 = ((25 >= 0 and "LBS" == "LBS") or (not True)) and (15 == 0)  # False

# [Extra: Advanced] self-reading: documentation on Logical operators
# https://docs.python.org/3/reference/expressions.html#boolean-operations
# Key take aways: lazy evaluation; and / or return last evaluated argument.
0 and 1 and False  # 0     (i.e. returns last evaluated argument, between 0 and 1)
False and 1 and 0  # False (... between False and 1)

1 and 'abc'  # 'abc'
1 and 'abc' and True  # True  (... between 'abc' and True)
1 and True and 'abc'  # 'abc' (... between True and 'abc')
