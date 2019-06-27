# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:00:44 2019

@author: juan
"""

x = []
posi_max = []
posi_min = []

for posi,i in enumerate(range(5)):
    x.append(int(input(f'digite o {posi+1}º valor: ')))

print('-='*20) 
for i,j in enumerate(x): 
    if j == max(x):
        posi_max.append(i)
    if j == min(x):
        posi_min.append(i)

print(f'''
A lista = {x}
Maximo = {max(x)}, posição = {posi_max}
Minimo = {min(x)}, posição = {posi_min}''')