# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:46:11 2020

@author: Rodrigo Bernardo Medeiros
function: caesar_cipher
"""

def caesar_cipher(text,num):
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
               24,25,26]
    
    numbers_code = []
    
    for number in numbers:
        
        
        if number - num <= 0:
            
            numbers_code.append(number - num + 26)
            
        else:
            
            numbers_code.append(number - num)
            
    
    # In this part, I have a list with normal sequence and code sequence
    
    # Create dicts to save the relation between letters and numbers
    
    normal_sequence = {}
    encrypted_sequence = {}
    
    for i in range(26):
        
        normal_sequence[letters[i]] = numbers[i]
        encrypted_sequence[numbers_code[i]] = letters[i]
        
    
    # Part to return the encoded text
    
    encrypted_text = ''
    
    for char in text:
        
        encrypted_text = encrypted_text + encrypted_sequence[normal_sequence[char.upper()]]
        
        
    return encrypted_text.lower()
        
    
    
    
        
        
        
        