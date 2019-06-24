# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:46:09 2019

@author: juan
"""

distancia = float(input('Qual a distância percorrida em km: '))
if distancia>200:
    print('O valor da passagem é R${:.2f}'.format(distancia*0.45))
else: 
    print('O valor da passagem é R${:.2f}'.format(distancia*0.5))
