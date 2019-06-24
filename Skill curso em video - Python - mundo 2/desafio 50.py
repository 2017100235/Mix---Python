# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:12:45 2019

@author: juan
"""
soma = 0
for i in range(0,7):
    n= int(input('digite um numero: '))
    if n%2 == 0:
        soma +=n
print('A soma dos numeros pares e', soma)