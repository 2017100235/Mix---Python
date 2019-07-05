# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:34:20 2019

@author: juan
"""

def leiaint(num):
    while True: 
        if num.isnumeric():
            return int(num)
            break
        else: 
            print('ERRO!, Digite um numero inteiro valido')
            num = str(input('Digite um numero: ')) 



n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n}')