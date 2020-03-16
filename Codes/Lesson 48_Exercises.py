# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:38:12 2020

@author: Rodrigo Bernardo Medeiros
"""

# Question 01

def sum_two(num_1,num_2):
    
    # Just calculate the sum between two numbers
    
    return num_1 + num_2

print(f'the sum of 3 and 4 is {sum_two(3,4)}')


'''
Question 02 - Write a funcion that performs the multiplication of two arguments.
By default the function should multiply the first argument by 2. Call it multiply.
'''

def multiply(num_1,num_2=2):

    '''
    Returns the product of num_1 and num_2; if num_2 is not given, returns
    2*num_1.
    '''    
    return num_1 * num_2

print(multiply(1))
print(multiply(1,4))


'''
Question 03 - Write a funcion to calculate num_1 to the power num_2. If num_2 
is not given its default value should be 2. Call it power.
'''

def power(num_1,num_2 = 2):
    
    return num_1 ** num_2

print(power(8))
print(power(2,4))


'''
Question 04 - Create a new file called capitals.txt, store the names of five
capitals cities in the file on the same line
'''

file = open('capitals.txt','w')
file.write('Brasilia, ')
file.write('London, ')
file.write('Santiago, ')
file.write('Paris, ')
file.write('Rome.')
file.close()

'''
Question 5
Ask the user for a new capital and include it ate capitals file
'''

user_input = input('Please enter a capital city :>> ')

file = open('capitals.txt', 'a')
file.write(' ' + user_input + '.')

file.close()

file = open('capitals.txt', 'r')
print(file.read())
file.close()

'''
Question 06 - Write a function tha will copy the contents of one file to a new file.
'''

def copy_file(infile, outfile):
    
    with open(infile,'r') as file:
        with open(outfile,'w') as file_1:
            
            file_1.write(file.read())
    
copy_file('capitals.txt', 'new_capitals.txt')
file = open('new_capitals.txt','r')
print(file.read())
file.close()
    
    
    
    



