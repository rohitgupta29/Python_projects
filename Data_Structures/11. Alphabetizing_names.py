# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:58:46 2020

@author: infom
"""
import operator

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
          {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}]


def alphabetizing_names(list_of_dicts):
    return sorted(list_of_dicts, key = operator.itemgetter('last','first'))


print(alphabetizing_names(PEOPLE))