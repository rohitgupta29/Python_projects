# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:38:30 2020

@author: infom
"""


def run_timing():
    no_of_runs = 0
    total_time = 0
    
    while True:
        one_run = input("Enter 10 km run time: ")
        
        if not one_run:
            break
        
        no_of_runs += 1
        total_time += float(one_run)
        
    average_time = total_time / no_of_runs
    
    print(f' Average of {average_time}, over {no_of_runs} runs')
    

run_timing()