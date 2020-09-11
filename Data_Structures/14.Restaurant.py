# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:03:46 2020

@author: infom
"""

MENU = {'sandwich': 10, 'tea' : 7, 'salad': 9}

def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip()
        
        if not order:
            break
        
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price},total is {total}')
            
        else:
            print(f'We are fresh out of {order} today')
            
            
    print(f'Your total is {total}')
    
    
restaurant()