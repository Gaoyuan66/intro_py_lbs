#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Group 5
AM02 Group Assignment 2 
"""

#%% a) LOAD LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   # main plotting library
import re # regular expressions (string matching)
# preprocess tweets to remove: URLs, emojies, smileys, hashtags, mentions
import preprocessor as p 
from PIL import Image # Python Imagining Lib (we will import image)
# natural language processing library (nat. lang. toolkit)
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer #sentiment analysis
from nltk.corpus import stopwords # remove meaningless words for wordcloud plot
from wordcloud import WordCloud   


#%% TWEETS PREPROCESSING -----------------------------------------------------:
# b) Load the data from pickle (these were stored as a dataframe)
df_all = pd.read_pickle("Tesla_Share_Tweets_1Mth")

# c) Examine df_all
# Number of downloaded tweets (approx 3,488), with 21 attributes

# d) store text into a list
tweets = list(df_all['text']) # will allow us to use both pandas and numpy fns

# e)
N = len(tweets)

# f) the 5th tweet
print(tweets[4])

# g) remove duplicates
# Remove duplicate tweets from the list (re-tweets; news repeats)
twsUnclean = set(tweets)

# h) number of distinct tweets - 3062
print(len(twsUnclean))

# --- CLEAN DATA
# Based on which libraries will be used afterwards, some of the below data 
# preprocessing may be needed. 
# Note: the sentiment analysis library handles the below for you, however
# let's understand how to do it in case you need to:

# i) learn how to clean help(p.clean)
# 1) --- Use preprocessor library (which we called 'p') to clean data from:
# URLs, emojies, smileys, hashtags, mentions 
# (note the simple senitment lib does not recognise emojies, or #hashtags)

# Test string to see how preprocessing library p works:
# s = 'Tesla cybertruck is great! #awesome 👍 https://www.tesla.com/en_gb/cybertruck'
# ans = p.clean(s)
# print(ans) # Tesla cybertruck is great!
# print(s)   # remember original string will be unchaned as it is immutable

# j) Clean all tweets using list comprehension
tws1 = [p.clean(text) for text in twsUnclean]

# Check how the first 5 tweets look like now:
print(tws1[:5])

# k) Clean tweets using regular expressions.
# Keep only letters and replace everything else with a space. Syntax is:
# re.sub(what you keep, what you repalce it with, string)
tws2 = [re.sub("[^a-zA-Z]", " ", x) for x in tws1] 

# Let's check how the first 5 tweets look like now:
print(tws2[:5])

# Strip all tweets of start/end white spaces and place all text to lower case 
# Use string methods to:
# strip characters of all start/end white spaces
# place all text to lower case
tws3 = [text.strip().lower() for text in tws2]

# Let's check how the first 5 tweets look like now:
print(tws3[:5])
# Delete any empty tweets (perhaps they only contained emojies)
tws4 = [text for text in tws3 if len(text)>0]

#%% Q1 II. PERFORM SENTIMENT ANALYSIS -----------------------------------------------:
# a) sentiment analysis
nltk.download('vader_lexicon') # only necessry for Mac machines
# initisalise VADER sentiment analysis lexicon, such that its ready for use
sid = SentimentIntensityAnalyzer() 

'''
Each word in a tweet is analysed for its negative / neutral / positive valence.
Then sentiment analyser produces a 'polarity score', standardized to range 
-1, +1, which gives the overall affect of the entire text.
'''

# Let's test out some strings
# score = sid.polarity_scores('i love my awesome car, absolutely beautiful')
# print(score) # 'compound': 0.9259

# score = sid.polarity_scores('awesome car i will buy it')
# print(score) # 'compound': 0.6249

# score = sid.polarity_scores('not good')
# print(score) # 'compound': -0.3412

# score = sid.polarity_scores('something neurtral')
# print(score) # 'compound': 0.0

# b) TASK: WRITE CODE WHICH WOULD PRODUCE AV. 'compound' SCORE FOR TESLA TWEETS
compound_scores = [sid.polarity_scores(text)["compound"] for text in tws4]
average_compound_score = np.mean(compound_scores)
print("Average Compound Score is:", average_compound_score)

# c) Comment on the final score
# I am a little skeptical with the average score.
# Taking average on the score is with the underlying assumption that the score has additive property.
# Otherwise, two tweets with 0.3 and 0.7 do not mean the average is 0.5.
# -0.5 and 0.5 do not mean neutral average either.
# In reality, negative scores are generally more affective than positive ones.
# Furthermore, the texts we are analysing are only a sample from twitter. Great selection bias may exist.

#%% III. WORDCLOUD ----------------------------------------------------------------:
# Obtain words that should not be plotted as they are not of much interest
nltk.download('stopwords') # download stopwords 
sw = set(stopwords.words('english'))
print(sw) # common Engish stopwords 

# Obtain all tweets as a single string to be used inside WordCloud function
allTweets = " ".join(tws4) # join all tweets into single string 

# Make standard Wordcloud
worC = WordCloud(width = 1000, height = 700, margin = 0, max_font_size = 170, min_font_size = 25, stopwords = sw).generate(allTweets)
plt.figure(figsize=(8, 6))
plt.imshow(worC, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

# Make a wordcloud in a shape of the Tesla Cybertruck!
# Open up the Console wide to allow full image to display
wave_mask = np.array(Image.open("cybertruck.jpeg"))
wordcloud = WordCloud(width = 1000, height = 700, max_font_size = 50, min_font_size = 5, mask = wave_mask).generate(allTweets)
plt.figure(figsize=(14, 12))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


#%% Q2 FED RESERVE STATEMENT -------------------------------------------------:
# September statement's important sentence phrasing
fomc_sep2018 = ["the", "committee", "expects", "that", "further", "gradual", "increases", "in", "the", "target", "range"]
# December statement's important sentence phrasing
fomc_dec2018 = ["the", "committee", "judges", "that", "some", "further", "gradual", "increases", "in", "the", "target", "range"]
   
# a) they are both lists
print(type(fomc_sep2018),type(fomc_dec2018))

# b) words have already been seperated out as elements
print(fomc_sep2018[:5])
print(fomc_dec2018[:5])

# c) check lengths
print(len(fomc_sep2018))
print(len(fomc_dec2018))

# d e f g) sentence analysis function

def compare_sentence(old_state, new_state):
    """
    Parameters
    ----------
    old_state : list/set
        list of words in older statement sentence.
    new_state : list/set
        list of words in later statement sentence.

    Returns
    -------
    all_words : list
        All words occurring in two sentences.
    common_words : list
        Words which were common for both sentences.
    old_words : list
        Words which were NOT used in the latest sentence.
    new_words : list
        Words which were NEW in the latest sentence.

    """
    old_state = set(old_state)
    new_state = set(new_state)
    all_words = old_state.union(new_state)
    common_words = old_state.intersection(new_state)
    old_words = old_state - common_words
    new_words = new_state - common_words
    
    return list(all_words), list(common_words), list(old_words), list(new_words)

# h) call the function
all_words, common_words, old_words, new_words = compare_sentence(fomc_sep2018,fomc_dec2018)

# i) docstring for grading

"""
d) All words:
    ['target',
     'further',
     'that',
     'gradual',
     'range',
     'expects',
     'committee',
     'some',
     'increases',
     'in',
     'the',
     'judges']

e) Common words:
    ['target',
     'range',
     'further',
     'that',
     'committee',
     'increases',
     'gradual',
     'in',
     'the']
f) Words NOT used in latest sentence:
    ['expects']
g) NEW words in latest sentence:
    ['some', 'judges']
    
"""












