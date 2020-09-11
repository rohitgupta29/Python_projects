# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:14:02 2020

@author: infom
"""
import collections
from collections import Counter

words = ['this','is','an','elementary','test','example']


def most_repeating_letter_count(word):
    a = Counter(word).most_common(1)[0][1]
    print (word,a)
    return a


def most_repeating_word(words):
    return max (words, key = most_repeating_letter_count)
    



print(most_repeating_word(words))
    