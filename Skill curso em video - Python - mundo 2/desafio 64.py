# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 00:26:13 2019

@author: juan
"""

num = int(input('Digite um numero: '))
cont = soma = 0
while num != 999:
    cont+=1
    soma+=num
    num = int(input('Digite um numero: '))

print('A soma e {}, foram {} iteraçoes'.format(soma,cont))