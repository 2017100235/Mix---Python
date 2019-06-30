# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:04:22 2019

@author: juan
"""

matriz = [[],[],[]]
cont = soma = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor para[{i},{j}]: ')))
        if matriz[i][j] %2 == 0:
            cont+= matriz[i][j]
        if j == 2:
            soma += matriz[i][j]
print()        
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^4} ]', end="")
    print()
maior = max(matriz[1])
print(f'''
Soma de valores pares = {cont}
Soma dos valores da 3ª coluna= {soma}
Maior valor da 2ª linha = {maior}''')