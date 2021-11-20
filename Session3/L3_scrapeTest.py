#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Dr Ekaterina Abramova
Year   : Simple scraping example of a webpage.

This is an amended and extended code from book: 'Web Scraping with Python', 
2nd Edition, Ryan Mitchell, Ch5. Original code can be found on: GitHub: 
https://github.com/EMitchell/python-scraping
"""


#%% READ IN SIMPLE WEBSITE
# standard Python library contains functions for requesting data across the web
from urllib.request import urlopen 

# open a remote object across a network and read it
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

'''
b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>
An Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, 
consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'
'''


#%%  READ IN WAR AND PEACE WEBSITE
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'lxml')

# --------------------- Extract first occurance of tag: -----------------------
# APPROACH 1 find first occurance using bs.name
# bs.h1 # <h1>War and Peace</h1>
bs.find('h1')

type(bs.find('h1')) # bs4.element.Tag i.e. h1 is a tag

# APPROACH 2: find first occurance using bs.find('name') where name is tag name
tag_1 = bs.find('span')
print(tag_1)
'''
<span class="red">Well, Prince, so Genoa and Lucca are now just family estates 
of the Buonapartes. But I warn you, if you don't tell me that this means war,
if you still try to defend the infamies and horrors perpetrated by
that Antichrist- I really believe he is Antichrist- I will have
nothing more to do with you and you are no longer my friend, no longer
my 'faithful slave,' as you call yourself! But how do you do? I see
I have frightened you- sit down and tell me all the news.</span>
'''

# consdier a tag object as a dictionary
# tag_1 looks like: <span class="red">Well, Prince, so Genoa … ﻿the news.</span>
tag_1['class'] # using dict key 'class' access value 
# ['red'] i.e. we accessed 'dictionary' content through 'key'. Value is ['red']

# access attributes of a tag using:
tag_1.attrs # {'class': ['red']}

# APPROACH 3: find first occurance using bs.find('name', attrs')
# Positonal binding
tag_2 = bs.find('span', {'class':'green'}) 
print(tag_2) # <span class="green">Anna Pavlovna Scherer</span>

# Equivalently using keyword binding
tag_3 = bs.find(name='span', attrs={'class':'green'}) 
print(tag_3) # <span class="green">Anna Pavlovna Scherer</span>

# -------------------- Extract all occurances of the tag: ---------------------
names = bs.find_all('span', {'class':'green'})
print(names[0]) # <span class="green">Anna Pavlovna Scherer</span>

# We can chain above operations to extract tags of interest from specific parts 
# of the document only: e.g. first find article body, then find all paragraphs
# Hypothetical example of some elaborate HTML file: 
'''
x    = bs.find('div', {'id':'article'}) # get article body only
data = x.find_all('p') # find all paragraphs within article body only
'''

# ---------------------- Extract text from bs object: -------------------------
# Obtain the String inside the tag:
ans1a = tag_2.get_text() # 'Anna\nPavlovna Scherer'
type(ans1a) # str (normal Python Unicode string)

# Equivalently use tag.text 
ans1b = tag_2.text # 'Anna\nPavlovna Scherer'
type(ans1b) # str (normal Python Unicode string)

# Separate content from tags using method get_text() 
# (usually is  the last step before saving data):
for n in names:
    print(n.get_text())
'''
Anna Pavlovna Scherer
Empress Marya Fedorovna
Prince Vasili Kuragin
Anna Pavlovna
St. Petersburg
the prince
Anna Pavlovna
Anna Pavlovna
the prince
the prince
the prince
Prince Vasili
Anna Pavlovna
Anna Pavlovna
the prince
Wintzingerode
King of Prussia
le Vicomte de Mortemart
Montmorencys
Rohans
Abbe Morio
the Emperor
the prince
Prince Vasili
Dowager Empress Marya Fedorovna
the baron
Anna Pavlovna
the Empress
the Empress
Anna Pavlovna's
Her Majesty
Baron
Funke
The prince
Anna
Pavlovna
the Empress
The prince
Anatole
the prince
The prince
Anna
Pavlovna
Anna Pavlovna
'''

# We can also extract text from the whole bs object
ans2 = bs.text
print(ans2)
'''
'\n\n\n\n\nWar and Peace\nChapter 1\n\n"Well, Prince, 
...
Anna Pavlovna meditated.\n\n\n\n'
'''
type(ans2) # str


# Obtain the Navigable String inside the tag:
ans2 = tag_2.string
type(ans2) # bs4.element.NavigableString
# NavigableString object will give us the text within a tag as a Unicode
# string, together with diff methods for searching and navigating the tree.
# NOTE: with a normal Python Unicode string, searching and navigation methods 
# will not work.


#%% [EXTRA] READ IN SIMPLE WEBSITE PRINT OUT VARIOUS COMPONENTS
from urllib.request import urlopen
from bs4 import BeautifulSoup # (nonstandard library - needs installing)
# If you've not installed it yet, run in terminal: conda install beautifulsoup4

html = urlopen('http://pythonscraping.com/pages/page1.html')
# transform HTML content to BeautifulSoup object
bs = BeautifulSoup(html.read(), 'lxml') # alternative parser: 'html.parser'
type(bs)

# Exgract items from bs by tag:
print(bs.find('h1')) # bs4.BeautifulSoup
'''
<h1>An Interesting Title</h1>
'''

print(bs.head)
type(bs.head) # bs4.element.Tag
'''
<head>
<title>A Useful Page</title>
</head>
'''


# ----------------------------- EXTRACT TEXT BODY: ----------------------------
# Find tag of interest
res1 = bs.div
'''
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.
</div>
'''
type(res1) # bs4.element.Tag

# To extract just the string out of the bs tag, use command:
ans1 = res1.text 
type(ans1) # str (successfully extract text content as string)
ans1
'''
'\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n'
'''
