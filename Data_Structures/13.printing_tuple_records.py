# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:46:14 2020

@author: infom
"""

import operator

People = [('Donald','Trump', 7.85),('Vladimir','Putin',3.626),('Jinping','Xi',10.603)]

def format_sort_records(list_of_tuple):
    output = []
    template = "{1:10}{0:10}{2:5.2f}"
    for person in sorted(list_of_tuple,key = operator.itemgetter(1,0)):
        
        output.append(template.format(*person))
    return '\n'.join(output)

print(format_sort_records(People))

    