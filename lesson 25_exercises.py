# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:07:26 2020

@author: Rodrigo Bernardo Medeiros
"""

# This Code Solves the exercicios from lesson 25 of Python Programmer
# BootCamp

# Question 1
'''
integer_input = int(input('Please enter a string from One to Five \n>>>>> '))


if integer_input == 1:
    print('One is the number')
    
elif integer_input == 2:
    print('Two is the number')
    
elif integer_input == 3:
    print('Three is the number')
    
elif integer_input == 4:
    print('Four is the number')
    
elif integer_input == 5:
    print('Five is the number')
    
else:
    print('The entry', integer_input,'is not acceptable')
    
'''

# Question 2
'''
string_input = input('Please enter a string from One to Five \n>>>>> ')
string_input = string_input.lower()

if string_input == 'one':
    print(1)
    
elif string_input == 'two':
    print(2)
    
elif string_input == 'three':
    print(3)
    
elif string_input == 'four':
    print(4)
    
elif string_input == 'five':
    print(5)
    
else:
    print('Out of range')
    
'''

# Question 3

# Variable to put the right number
'''
right_number = 7

guess = int(input('Please write a integer number from 1 to 10 \n>>>>> '))

if guess == right_number:
    
    print('Congratulations! You Win!')
    
elif guess >=0 and guess < right_number:
    print('The number is too low, try again!')
    
elif guess > right_number and guess <= 10:
    print('The number is too high, try again!')
    
else:
    print('Out of range')
    
'''

# Question 4
'''
name = input('Please enter your name \n>>>>> ')

size_name = len(name)

if size_name > 5:
    print('Your name have', size_name, 'characters')
    
else:
    print('The length of your name is a secret')
'''

# Question 5
'''
num_1 = int(input('Please enter the first integer between 1 and 20 \n>>> '))
num_2 = int(input('Please enter the second integer between 1 and 20 \n>>> '))


if num_1 > 15 and num_2 >= 15:
    print('The product between the numbers is:', num_1*num_2)
    
elif num_1 > 15 and num_2 <= 15:
    print('The sum between the numbers is:', num_1 + num_2)
    
elif num_2 > 15 and num_1 <= 15:
    print('The sum between the numbers is:', num_1 + num_2)
    
else:
    print(0)
    
'''
# Question 6

num_1 = int(input('Please enter the first integer \n>>> '))
num_2 = int(input('Please enter the second integer \n>>> '))
print()

auxiliar_number = 0

auxiliar_number = num_1
num_1 = num_2
num_2 = auxiliar_number

print(num_1)
print(num_2)




