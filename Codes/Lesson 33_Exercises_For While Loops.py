# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:46:31 2020

@author: Rodrigo Bernardo Medeiros
"""

#Lesson 33 - Exercises - For While Loops

# Question 1
print('Question 1')
'''
Ask the user for two numbers between 1 and 100. Then, count from the lower to 
the higher number. Print the results.
'''


num_1 = int(input('Please enter a integer between 1 to 100 :>> '))
num_2 = int(input('Please enter a integer between 1 to 100 :>> '))

num_list = []

num_list.append(num_1)
num_list.append(num_2)

num_list = sorted(num_list)

for num in range(num_list[0],num_list[1]+1):
    print(num,end = ' ')

print()
print()

# Question 2
print('Question 2')

'''
Ask the user to input a string and then print it out to the screen in reverse
order (use a for loop)
'''

string_user = input('Please enter a string :>> ')
reverse_string = ''

for i in range(len(string_user)-1,-1,-1):
    
    print(string_user[i], end = '')

print()
print()

# Question 3
print('Question 3')

'''
Ask the user for a number between 1 and 12 the display a times table for that
number
'''

user_input = input('Please enter a integer between 1 and 12:>> ')

while not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 12:
    print('Please enter a valid number')
    user_input = input('Please enter a integer between 1 and 12:>> ')
    
user_input = int(user_input)

print()
print('=== Times Table ===')

for i in range(1,13):
    
    print(f' {user_input} * {i} = {user_input*i}')

    
print()
print()

# Question 4
print('Question 4')

'''
Can you amend the solution to question 3 so that it just prints out a times table
between1 and 12? (no need to ask user for input)
'''

for i in range(1,13):
    
    print(f'=== Times Table for {i} ===')
    print()
    
    for j in range(1,13):
        print(f' {i} * {j} = {i*j}')
        
    print('===========================')
    print()
    
print()
print()

# Question 5
print('Question 5')

'''
Ask the user to input a sequence of numbers. Then calculate the mean and print
the result.
'''

user_input = input('Please enter sequence of integers, write exit to stop :>> ')
sum_of_user_input = 0
numbers = []

while user_input.lower() != 'exit':
    
    while not user_input.isdigit():
        print('Please enter a valid number or exit to finish')
        user_input = input('Please enter sequence of integers, write exit to stop :>> ')
    
    numbers.append(int(user_input))
    user_input = input('Please enter sequence of integers, write exit to stop :>> ')
    

sum_of_user_input = sum(numbers)
mean_of_user_input = sum_of_user_input/len(numbers)

print(f'The mean of all user inputs is {mean_of_user_input}')
        
    
print()
print()

# Question 6
print('Question 6')

'''Write a code that will calculate 15 factorial. (factorial is product of positive)
ints up to a given number. e.g 5 factorial is 5x4x3x2x1
'''

n = 15
product = 1

for i in range(1,15+1):    
    
    product = i*product
    
print(f'The factorial of 15 is {product}')
    
print()
print()

# Question 7
print('Question 7')

'''
Write a code to calculate Fibonacci numbers. Create a list containing first 20 
fibonacci numbers, (Fib numbers made by sum of preceeding two.)
'''

n = 20
# Pode ser um input depois

n_1 = 0
n_2 = 1

Fib_list = []
Fib_list.append(n_1)
Fib_list.append(n_2)

for i in range(2,n):
    Fib_list.append(Fib_list[i-1]+Fib_list[i-2])
    
for num in Fib_list:
    print(num,end = ' ')
    
    
print()
print()

# Question 10
print('Question 10')

'''
Write some code tha will determine all odd and even numbers between 1 and 100.
Put the odds in a list named odd and the evens in a list named even.
'''
odds = []
evens = []

for i in range(1,101):
    div = i%2
    
    if div ==0:
        evens.append(i)
        
    elif div ==1:
        odds.append(i)
        
print(f'The odds are {odds}')
print()

print(f'The evens are {evens}')
print()
    





















