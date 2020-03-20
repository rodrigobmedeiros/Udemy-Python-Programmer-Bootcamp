import numpy as np
import math

# Metodo que retorna o menor numero inteiro maior do que o número passado para a função
import sys

lista = [1,2,3,1,4,5,6,1,7,8,9,1]



print(lista)

count = 0

while 1 in lista:

    lista.remove(1)
    count += 1

print(lista)
print(count)


lista = []
print(not lista)

isempty = not lista

print(isempty)