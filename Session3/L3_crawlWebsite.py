#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Dr Ekaterina Abramova
Document : Crawling: Crawl an entire wiki website.

This is an amended and extended code from book: 'Web Scraping with Python', 
2nd Edition, Ryan Mitchell, Ch5. Original code can be found on: GitHub: 
https://github.com/EMitchell/python-scraping
"""

#%% CRAWL WIKI STARTING FROM MAIN PAGE
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set() # create empty set to keep track of links where already been to

def getLinks(pageUrl):
    global pages # allows overwriting variable 'pages' defined outside of the fn
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html.read(), "html.parser")
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            # Did we enounter a new page?
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage) 
    # note that the function calls itself and there is no return statement

# Start from the 'front page of Wikipedia' i.e. passing in empty URL.
getLinks('')

# ENSURE TO PRESS RED SQUARE ONCE YOU ARE READY TO STOP THE  EXECUTION!!!
'''
Where the first 5 links are: 
    
/wiki/Wikipedia
/wiki/Wikipedia:Protection_policy#semi
/wiki/Wikipedia:Requests_for_page_protection
/wiki/Wikipedia:Requests_for_permissions
/wiki/Wikipedia:Protection_policy#extended
'''
