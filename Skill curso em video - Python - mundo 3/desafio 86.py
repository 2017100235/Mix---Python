# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:19:41 2019

@author: juan
"""

matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor para[{i},{j}]: ')))

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^4} ]', end="")
    print()
