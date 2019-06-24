# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:01:41 2019

@author: juan
"""

soma = 0
for i in range (1,501,2):
    if (i%3==0):
        soma +=i
print('A soma dos numeros impares multiplos de 3 é ',soma)