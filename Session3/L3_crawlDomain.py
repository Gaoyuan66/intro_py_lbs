#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Dr Ekaterina Abramova
Document : Crawling: Transverse a single domain (only links from Kelvin Baker)

Code begins a project on 'Six Degrees of Separation on Wikipedia'.
This is an amended and extended code from book: 'Web Scraping with Python', 
2nd Edition, Ryan Mitchell, Ch5. Original code can be found on: GitHub: 
https://github.com/REMitchell/python-scraping
"""

 #%% Extract All Links
from urllib.request import urlopen  # import function urlopen
from bs4 import BeautifulSoup       # import function BeautifulSoup

html  = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon') # open website
bs    = BeautifulSoup(html.read(), 'lxml') # convert html to bs object
type(bs)  # bs4.BeautifulSoup
print(bs) # entire HTML page which you have read into beautiful soup object

# Obtain all tags with <a> which identifies website links
links = bs.find_all('a') # <a> href attribute (i.e. link)
# <a> tag defines a hyperlink, used to link from one page to another, example:
# <a href="/wiki/Sosie_Bacon" title="Sosie Bacon">Sosie Bacon</a>

links[6] # check 7th element from extracted links: 
# <a class="mw-redirect" href="/wiki/Philadelphia,_Pennsylvania" title="Philadelphia, Pennsylvania">Philadelphia, Pennsylvania</a>

# access attributes of a tag using:
links[6].attrs
'''
{'href': '/wiki/Philadelphia,_Pennsylvania',
 'class': ['mw-redirect'],
 'title': 'Philadelphia, Pennsylvania'}
'''

# print 3 of the 905 obtained links 
for link in links[6:9]: # I chose links at index 6,7,8 because they are short :-)
    print(link)
'''
<a class="mw-redirect" href="/wiki/Philadelphia,_Pennsylvania" title="Philadelphia, Pennsylvania">Philadelphia, Pennsylvania</a>
<a href="/wiki/Kyra_Sedgwick" title="Kyra Sedgwick">Kyra Sedgwick</a>
<a href="/wiki/Sosie_Bacon" title="Sosie Bacon">Sosie Bacon</a>
'''    

# print out ALL URLs that Wikipedia article on Kevin Bacon links to.
for link in links[0:5]:
    print(link.attrs)
'''
{'id': 'top'}
{'href': '/wiki/Wikipedia:Protection_policy#semi', 'title': 'This article is semi-protected to promote compliance with the policy on biographies of living persons'}
{'class': ['mw-jump-link'], 'href': '#mw-head'}
{'class': ['mw-jump-link'], 'href': '#searchInput'}
{'href': '/wiki/Kevin_Bacon_(disambiguation)', 'class': ['mw-disambig'], 'title': 'Kevin Bacon (disambiguation)'}
'''

# We only want to print out elements of links which contain href i.e. links.
# For example the first element's attribute was an 'id' without href.
# <a id="top"></a> (does not contain href, and is a placeholder for a link)
# <a href= ...
for link in links[0:5]:
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''
Where the first href links are: [MY COMMENTS IN SQ BRACKETS]:
    /wiki/Wikipedia:Protection_policy#semi [PROTECTION POLICY NOT INTERESTING]
    #mw-head                               [OTHER UNINSTERESTING LINK]
    #searchInput                           [NOT INTERESTING]
    /wiki/Kevin_Bacon_(disambiguation)     [FINALLY SOME INTERESTEING LINKS]
'''
# Note only 4 links obtained, even though 5 requested, since the first one was 
# skipped as it did not have a link.


#%% Omit Unnecessary Links (sidebar, footer, privacy policy etc)
from urllib.request import urlopen
from bs4 import BeautifulSoup

import re # Regular Expressions Operations library
# A regular expression specifies a set of strings, e.g. '^(/wiki/)((?!:).)*$' 
# Functions in this module allow to check if a particular string matches a 
# given regular expression.

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon') # open website
bs = BeautifulSoup(html.read(), 'lxml') # convert html to bs object

regExp = '^(/wiki/)((?!:).)*$' # Wikipedia article URL of the form 
# /wiki/<Article_Name> i.e. internal article links only. 
# Prints out only ARTICLE URLs that Wikipedia article on Kevin Bacon links to.
'''
Further reading about regular expressions here:
    https://docs.python.org/3/library/re.html
'''

# Look just inside bodyContent (avoid footer, sidebar, privacy policy etc) 
x = bs.find('div', {'id':'bodyContent'}) # <div> is division / section
links = x.find_all('a', href = re.compile(regExp)) # find all hrefs with /wiki

for link in links[0:5]:
    if 'href' in link.attrs:
        print(link.attrs['href'])

'''
Where the first 5 links are: 
[NOTE ALL ONLY CONTAIN WIKI LINKS, NO DISINTERESTING LINKS!]

/wiki/Kevin_Bacon_(disambiguation)
/wiki/Philadelphia,_Pennsylvania
/wiki/Kyra_Sedgwick
/wiki/Sosie_Bacon
/wiki/Edmund_Bacon_(architect)
'''


#%% RANDOMLY SELECT NEXT ARTICLE (UNTIL ALL ARTICLES IN DOMAIN ARE VISITED)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now()) # fix random number generator

def getLinks(articleUrl):
    # Attach the article of iterest to enwikipedia.org address
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl)) 
    bs = BeautifulSoup(html.read(), 'lxml') # convert html to bs object
    # Wiki article URL of form /wiki/<Article_Name> linked from K Bacon's URL)
    regExp = '^(/wiki/)((?!:).)*$' # i.e. find internal wiki links only 
    # Obtain links matching with regExp only
    x = bs.find('div', {'id':'bodyContent'}) # <div> is division / section
    links = x.find_all('a', href = re.compile(regExp)) # find all hrefs with /wiki
    return links

# Obtain all links on the given page matching regular expression /wiki/
links = getLinks('/wiki/Kevin_Bacon')

# In this case using while so that you can stop running the loop at any time by
# pressing the red square button on the console. (If we used the theoretically
# correct for loop, we would have had to loop all the way over 412 links!)
# ENSURE TO PRESS RED SQUARE ONCE YOU ARE READY TO STOP THE EXECUTION!!!
while len(links) > 0:
    # obtainr random number between 0 and number of elements in links
    r = random.randint(0, len(links) - 1)
    # extract random href attribute from a link, corresponding to r
    newArticle = links[r].attrs['href']
    print(newArticle) # print new webpage given by new Article
    links = getLinks(newArticle) # extract all links from newArticle

