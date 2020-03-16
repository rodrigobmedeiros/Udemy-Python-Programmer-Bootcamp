# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:56:03 2020

@author: Rodrigo Bernardo Medeiros
"""

class people():
    
    specie = 'Human'
    
    def __init__(self,name, age,city):
        
        
        
        self.name = name
        self.age = age
        self.city = city
        
    def get_details(self):
        
        print(f'Infomration: Name: {self.name}, Age: {self.age} and City: {self.city}')
        

rodrigo = people('Rodrigo Bernardo Medeiros', 33, 'Rio de Janeiro')

rodrigo.get_details()


