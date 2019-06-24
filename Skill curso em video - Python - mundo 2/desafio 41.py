# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:34:56 2019

@author: juan
"""

ano = int(input('Ano de nascimento: '))
idade = 2019-ano

if idade<=9:
    print('categoria: Mirim')
elif (idade>9 and idade <=14): 
    print('categoria: Infantil')
elif (idade>14 and idade <=19):
    print('categoria: Junior')
elif (idade>19 and idade <=20):
    print('categoria: Senior')
else: 
    print('categoria: Master')