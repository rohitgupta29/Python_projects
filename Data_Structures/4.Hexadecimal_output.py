# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:46:47 2020

@author: infom
"""


def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    
    for power, digit in enumerate (reversed(hexnum)):
        decnum += int(digit,16) * (16 ** power)
    print(decnum)
    
    
hex_output()