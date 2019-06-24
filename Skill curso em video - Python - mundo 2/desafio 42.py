# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:41:47 2019

@author: juan
"""

a = int(input('digite 1º lado do triangulo: '))
b = int(input('digite 2º lado do triangulo: '))
c = int(input('digite 3º lado do triangulo: '))

if ((abs(b-c)<a<(b+c)) and (abs(a-c)<b<(a+c)) and (abs(a-b)<c<(a+b))):
    print('Esses valores formam um triangulo !')
    
    if (a==b==c): 
        print('Um triangulo esquilatero')
    elif(a==b or b==c or a==c):
        print('Um triangulo isorceles')
    else: 
        print('Um trinagulo escaleno')
    
else: 
    print('Esses valores não formam um triangulo !')
