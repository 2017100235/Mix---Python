# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 00:34:42 2019

@author: juan
"""

soma = maior = menor = num = int(input('Numero: '))
cont = 1
resp = str(input('Quer continuar [S/N]: '))
while (resp.lower()=='s'):
    num = int(input('Numero: '))
    if num > maior:
        maior = num
    if num < menor: 
        menor = num
    soma +=num
    cont+=1
    resp = str(input('Quer continuar [S/N]: '))

print(''' 
Media = {}
Maior = {}
Menor = {}      
'''. format(soma/cont,maior,menor))  
