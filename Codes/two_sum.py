# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:09:04 2020

@author: Rodrigo Bernardo Medeiros
"""

def two_sum(numbers,target):
    
    result_list = []
    
    # I used two loops the second one starting from the first index with this
    # I can sum all pairs of numbers without repetition.
    
    for i_num in range(len(numbers)):
        
        for j_num in range(i_num, len(numbers)):
            
            sum_numbers = numbers[i_num] + numbers[j_num]
            
            if sum_numbers == target:
                
                result_list.append(i_num)
                result_list.append(j_num)
                return result_list
            
    
    return -1