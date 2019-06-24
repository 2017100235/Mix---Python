# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:26:00 2019

@author: juan
"""

termo = int(input('Termo: '))
razao = int(input('Razão: '))
cont = 1
pa = termo+razao
print(termo,end=' -> ')
while cont < 10:
    print(pa, end=' -> ')
    pa+=razao
    cont+=1
print('FIM')