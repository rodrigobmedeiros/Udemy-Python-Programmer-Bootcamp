# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 08:13:20 2020

@author: DigaoSuplementos
"""
# This Program will calculate the circulus area using a radius value given for 
# an user

# The user gives a radius value
radius_string = input('Please enter with the radius value \n ===> ')

# This value must be converted from string to float
radius_float = float(radius_string)

# Value of pi
pi = 3.14159

# Area Calculus
area = pi * radius_float ** 2


print(' You entered the radius \n =====> ', radius_float, '\n The area of the circle is \n =====> ', area)
