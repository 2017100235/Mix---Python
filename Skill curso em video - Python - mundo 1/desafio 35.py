# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:49:25 2019

@author: juan
"""

a = int(input('digite 1º lado do triangulo: '))
b = int(input('digite 2º lado do triangulo: '))
c = int(input('digite 3º lado do triangulo: '))

if ((abs(b-c)<a<(b+c)) and (abs(a-c)<b<(a+c)) and (abs(a-b)<c<(a+b))):
    print('Esses valores formam um triangulo !')
else: 
    print('Esses valores não formam um triangulo !')
