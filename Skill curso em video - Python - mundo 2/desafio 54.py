# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:07:36 2019

@author: juan
"""
cont = 0
for i in range(0,7):
    ano = int(input('ano de nascimento: '))
    idade = 2019 - ano
    if idade >= 18:
        cont+=1
print('Tem {} adultos e {} menor de idade'.format(cont,7-cont))