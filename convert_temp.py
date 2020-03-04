# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:01:37 2020

@author: DigaoSuplementos
"""

# This program will convert temperatures from Fahrenheit to Celsius


# User enters with temperature in °F
temp_f = float(input('Please enter the temperature in Fahrenheit \n =====> '))


# Expression to convert temperature com °F to °C
temp_c = 5*(temp_f-32)/9

print('The temperature ', temp_f, '°F = ', temp_c, '°C')


