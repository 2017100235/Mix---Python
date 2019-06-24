# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:23:18 2019

@author: juan
"""

maior = menor = float(input('seu peso: '))
p_maior = p_menor = 1

for i in range(2,6):
    x = float(input('seu peso: '))
    if x >= maior:
        maior = x
        p_maior = i
    if x <= menor:
        menor = x
        p_menor = i

print('''A pessoa mais pesada é {}º,{:.2f}kg
A pessoa mais leve é {}º,{:.2f}kg'''.format(p_maior,maior,p_menor,menor))
        