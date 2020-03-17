# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:56:19 2020

@author: Rodrigo Bernardo Medeiros
"""

def sierpinski_triangle(n_iter):
    
    from random import choice
    import matplotlib.pyplot as plt
    
    
    list_to_choose = [1,2,3]
    Po = [0,0]
    
    x_list = []
    y_list = []
    
    x_list.append(Po[0])
    y_list.append(Po[1])
    
    x_new = Po[0]
    y_new = Po[1]
    
    for i_num in range(0,n_iter):
        
        x_new,y_new = calc_next_point(choice(list_to_choose), x_new,y_new)
        x_list.append(x_new)
        y_list.append(y_new)
        
    plt.plot(x_list,y_list,'o')
    plt.savefig('teste.png', format='png')
    
    

        
def calc_next_point(transf, xo,yo):
    
    if transf == 1:
        
        x1 = 0.5*xo
        y1 = 0.5*yo
        
    elif transf == 2:
        
        x1 = 0.5*xo + 0.5
        y1 = 0.5*yo + 0.5
        
    else:
        
        x1 = 0.5*xo + 1
        y1 = 0.5*yo
        
    return x1,y1
    
    
    

