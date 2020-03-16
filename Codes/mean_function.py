# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:59:09 2020

@author: Rodrigo Bernardo Medeiros

"""

def mean(*numbers):
    
    mean_numbers = sum(numbers)/len(numbers)
    return mean_numbers

print(mean(1,1,1,1,1,1,1,1,1,1))