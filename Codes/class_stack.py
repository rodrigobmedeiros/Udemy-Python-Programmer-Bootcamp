# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:21:09 2020

@author: Rodrigo Bernardo Medeiros
"""

class Stack(object):
    
    def __init__(self):
        
        self.list_stack = []
        
    def isempty(self):
        
        if not self.list_stack:
            
            return True
        
        else:
            
            return False
        
    def push(self,item):
        
        self.list_stack.append(item)
        
    def pop(self):
        
        self.list_stack.pop()
        
    def peek(self):
        
        if self.list_stack ==[]:
            
            return None
        
        else:
            
            return self.list_stack[-1]
        
    def __repr__(self):
        
        return repr(self.list_stack)
    

