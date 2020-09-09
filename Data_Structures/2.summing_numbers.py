# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:30:33 2020

@author: infom
"""

def mysum(*numbers):
    total = 0
    for number in numbers:
        total += number
        
    return total

print(mysum(10,20,30))