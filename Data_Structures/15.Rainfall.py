# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:20:09 2020

@author: infom
"""


def get_rainfall():
    rainfall = {}
    
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        
        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name,0) + int(mm_rain)
        
        
    for city,rain in rainfall.items():
        print(f'{city}:{rain}')
        
        
get_rainfall()