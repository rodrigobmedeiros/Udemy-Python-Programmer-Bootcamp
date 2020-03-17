# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:41:58 2020

@author: Rodrigo Bernardo Medeiros
"""

class Cards(object):
    
    def __init__(self,value, suit):
        
        self.value = value
        self.suit = suit
        
    def display_card(self):
        
        print(f'{self.value} of {self.suit}')
        
    def get_value(self):
        
        return self.value
    
    def get_suit(self):
        
        return self.suit
    
    def __str__(self):
        
        my_card = str(self.value) + ' of ' + str(self.suit)
        return my_card
        

