# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:01:36 2020

@author: Rodrigo Bernardo Medeiros

"""

'''
Create a circle class that will take the value of a radius and return the area 
of the circle
'''



class circle(object):
    
    def __init__(self,radius):
        
        
        self.radius = radius
        self.area = 0.0
    
    def calc_area(self):
        import math
        
        self.area = math.pi*self.radius**2
        return self.area
    
my_circle = circle(2)

print(my_circle.calc_area())
print(my_circle.area)

