# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:50:06 2020

@author: Rodrigo Bernardo Medeiros
"""

# Question 01

#capitals = {'France':'Paris', 'Spain':'Madrid', 'United Kingdon':'London',
#            'India':'New Delhi', 'United States':'Washington DC', 'Italy':'Rome',
#            'Denmarck':'Copenhagen', 'Germany':'Berlin', 'Greece':'Athens',
#            'Bulgaria':'Sofia', 'Ireland':'Dublin', 'Mexico':'Mexico City'
#            }
#
#print(capitals)
#
#user_input = input('Please enter a country name to check :>> ')

# Make all chars lower case
#user_input = user_input.lower()
#counter = 0
#
#
#for country,city in capitals.items():
#    
#    actual_country = country.lower()
#    
#    if user_input == actual_country:
#        print(f'The {country} is the list and its capital is {city}')
#        counter = counter + 1
#        break
#
#if counter == 0:
#    print('The country is not in the list')

# Question 2

#Fibonacci = {}
#Fibonacci[1] = 0
#Fibonacci[2] = 1
#
#for i in range(3,13):
#    Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]
#    # Fibonacci[i] = Fibonacci.get(i-1) + Fibonacci.get(i-2)
#    # Returns same results but using a different method
#    
#    
#print(Fibonacci)


# Question 03

companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
inside_keys = ['open', 'high', 'low', 'close']
inside_prices = [[12.87, 13.23,11.42,13.10], [23.54, 25.76,21.87, 22.33],
                 [98.99, 102.34,97.21, 100.065],[203.63,207.54,202.43,205.24]]

complete_info = {}


## count through companies
#for count_i in range(4):
#    inside_dict = dict()
#    
#    # count trhough keys
#    for count_j in range(4):
#        
#        inside_dict[inside_keys[count_j]] = inside_prices[count_i][count_j]
#        
#    complete_info[companies[count_i]] = inside_dict
#    
#
#print(complete_info)



# Question 4

#import datetime
#
#today = datetime.date.today()
#print(type(today))
#
#holiday = datetime.date(2020,3,31)
#
#days_to_lastday = holiday - today
#print(days_to_lastday.days)

# Question 5

import matplotlib.pyplot as plt
import random
print()

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_random = dict()

for char in letters:
    letter_random[char] = random.randint(1,100)
    
print(letter_random)
x,y = zip(*letter_random.items())

plt.bar(x,y)
    


    
    


