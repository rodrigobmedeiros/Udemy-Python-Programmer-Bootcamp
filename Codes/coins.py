# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:53:19 2020

@author: Rodrigo Bernardo Medeiros
@function: coins

"""

def coins(n_coins):
    
    # I need to analyze heads and tails, because its a 0-1 outcoming, I will
    # use a boolean to represent this event.
    
    isheads = True
    coins_list = []
    # n is the step number for each iterarion
    n_init = 1
    n_step = 2
    # Create a list with all coins in heads position
    
    for i_coins in range(n_coins):
        
        coins_list.append(isheads)
        
    print(coins_list)
    
    while n_init < n_coins:
        
        for i in range(n_init,n_coins,n_step):
            
            coins_list[i] = not coins_list[i]
        
        n_init += 1
        n_step += 1
        print(coins_list)
        
    total_heads = coins_list.count(True)
    return total_heads
    
    
    
            