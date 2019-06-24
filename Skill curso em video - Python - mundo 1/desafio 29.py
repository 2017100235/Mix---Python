# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:44:08 2019

@author: juan
"""

vel = float(input('Qual sua velocidade: '))
if vel > 80: 
    print ('Você ultrapassou',vel - 80,'km/h da  velocidade permitida')
    print('O valor à pagar será de R${:.2f}'.format((vel-80)*7))
else: 
    print('Ok velocidade permitida !')
