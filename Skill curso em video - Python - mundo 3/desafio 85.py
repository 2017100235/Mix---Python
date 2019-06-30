# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:56:04 2019

@author: juan
"""
lista =[[], []]

for i in range(7):
    num = int(input(f'{i+1}º Numero: '))
    if num%2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
        
lista[0].sort()
lista[1].sort()
print(f'Valores pares = {lista[0]} \nValores impares = {lista[1]}')