# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:30:26 2019

@author: juan

"""

num = tuple(int(input(f'{i+1}º numero: ')) for i in range(4))

print(f'''
voce digitou os valores {num}      
Nº 9 apareceu = {num.count(9)} vezes ''')

if 3 not in num:
    print('O valor 3 não foi encontrado em nenhuma posição')
else:
    print(f'O valor 3 foi encontrado na {num.index(3)+1}º posição')

print('Os valores pares foram ',end=' ')
for i in num:
    if i%2==0:
        print(i,end=' ')

    

