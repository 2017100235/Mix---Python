# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 01:36:05 2019

@author: juan
"""

num = int(input('Digite um numero: '))
cont = soma = 0

while True:  
    if num == 999:
        break
    cont+=1
    soma+=num
    num = int(input('Digite um numero: '))

print(f'A soma é {soma}, foram {cont} iteraçoes')