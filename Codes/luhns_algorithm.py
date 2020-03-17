# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:26:07 2020

@author: Rodrigo Bernardo Medeiros
"""

def luhns_algorithm():
    
    credit_number_string = input('''Please enter a credit card number with 16 digits 
                                 :>> ''')
    list_others = [] # List to store the digits aren't from the second last
    list_numbers = [] # List to store the digits are from the second last
    list_numbers_x2 = [] # List to store the digits x2
    
    # Insert digits into list_others
    
    for ichar in range(len(credit_number_string)-1,-1,-2):
    
        list_others.append(credit_number_string[ichar])
    
    # Insert digits into list_numbers
    for ichar in range(len(credit_number_string)-2,-1,-2):
    
        list_numbers.append(credit_number_string[ichar])
    
    # Insert digits into list_numbers_x2
    for inum in range(len(list_numbers)):
        
        list_numbers_x2.append((str(int(list_numbers[inum])*2)))
    
    # Calculate the sums to total number
    sum_x2 = sum_digits(list_numbers_x2)
    sum_total = sum_x2 + sum_digits(list_others)
    
    # Variable to check if credit card number is valid
    isvalidnumber = False
    
    # Test with division by 10
    division_by_10 = sum_total % 10
    
    if division_by_10 == 0:
        
        isvalidnumber = True
        
    return isvalidnumber
            
    
# Function to sum digits into a list of strings
def sum_digits(list_to_sum):
    
    total = 0
    
    for char_i in list_to_sum:
                
        for char_j in char_i:
            
            total += int(char_j)
            
    return total
        