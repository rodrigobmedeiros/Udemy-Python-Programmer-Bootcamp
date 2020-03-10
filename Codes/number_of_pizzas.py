# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:49:00 2020

@author: DigaoSuplementos
"""

# Bob, Ann, Jane and Ashwin want to order a pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division

# Number of people that will eat pizza
n_people = 4

# Number of slices by person
n_slices = 4

total_slices = n_people * n_slices

total_pizzas = total_slices//6 + 1

slices_left = total_pizzas*6 - total_slices

print('Number of pizzas required is:', total_pizzas, 'there will be', slices_left, 'remaining slices.')

