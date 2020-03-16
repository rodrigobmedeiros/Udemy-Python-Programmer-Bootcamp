# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:16:13 2020

@author: Rodrigo Bernardo Medeiros
"""

'''
Question 01 - Create a class to represent a bank account. It will need to have
a balance, a method of withdrawn money, depositing money and displaying the ba-
lance to the screen. Create an instance of the bank account and check the me-
thods work as expected.
'''

class bankaccount():
    
    def __init__(self, balance=0.0):
        
        # The count will be initialized with balance equals to zero or if it
        # was the case, with a value.
        
        self.balance = balance
        
    def display_balance(self):
        
        print(f'Your balance is {self.balance}')
        
    def deposit_money(self):
        
        deposit = float(input('How much money do you want to deposite? :>> '))
        self.balance += deposit
        
        print(f'Your new balance is {self.balance}')
        
    def withdrawal_money(self):
        
        withdrawal = float(input('How much money do you want to withdrawn? :>> '))
        
        if withdrawal > self.balance:
            
            print(f'Your balance is insufficient, your balance is {self.balance}')
        
        else:
            
            self.balance -= withdrawal
            print(f'successful withdrawal, your balance is {self.balance}')
            
rodrigo_count = bankaccount()

rodrigo_count.display_balance()

rodrigo_count.deposit_money()

rodrigo_count.withdrawal_money()


            
        
        
        
        
        
        