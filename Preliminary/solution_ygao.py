"""
Answers to Q1
b)
  i) environment is the set of hardware (CPU, GPU, etc.) and software (OS, compilers, etc.) to meet requirements of running programs.
  ii) package / library is a set of objects (mainly functions) defined before and can be loaded in other programs.
  iii) now we are using conda as package management system, so conda install is a better choice. conda-forge is a channel instead of package management system.
  iv) IPython Console
  v) No. `not` is reserved in python.
  vi) `=` is for assignment. `==` is for mathematical equality check
c) `conda create -n spider2021 statsmodels`
d) operator precedence defines the order of operations. operators with higher (smaller) precedence shuold be executed first.
   operator associativity defines how operators of same precedence are grouped without parenthesis.
"""

# 2. Operators - Arithmetic

# a)
x = 15
y = 5**3 + x/2.5 # 131.0

# b)
# i)
yPositive = y > 0 #True
# ii)
yEven = y % 2 == 0 # False

# c)
# i)
67/6  # 11.166666
# ii)
71/6 # 11.83333334
# iii)
67//6 # 11
# iv)
71//6 # 11
# it will round up to the largest integer smaller than the actual result

# d)
x1 = (5+9)**2/2%3 # x1 = 2.0
x2 = (((5+9)**2)/2)%3 # x2 = 2.0
# yes they are the same.

# e)
x3 = 17
x3 %= 3 # x3 = 2

# f)
# because the associativity of operator ** is right-to-left.


# 3. Operators - Relaitional

# a)
"abc" == "abcd" # False

# b) 
17.5 == 17.50 # True
5 == 5.0 # True

# c)
5 < 7 < 9 # True
(5 < 7) < 9 # True is 1


# 4) Operators - Logical

# a)
True and True # True
True and False # False
False and False # False

# b)
True or True # True
True or False # True
False or False # False

# c)
not True # False
not False # True

# d)
# i)
(17 != 5) or ((12==12) and (15 < 1))
# comparisons go first, then and, lastly or
# ii)
(17 != 5 or 12==12) and (15 < 1)

















