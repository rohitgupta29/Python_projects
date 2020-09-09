# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:12:22 2020

@author: infom
"""


def ubbi_dubbi(word):
    output = []
    
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
            
            
    return ''.join(output)

print(ubbi_dubbi("Winner"))