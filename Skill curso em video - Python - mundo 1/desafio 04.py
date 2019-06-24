# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 00:17:17 2019

@author: juan
"""

string = input('Digite algo: ')
print('A mensagem digitada:')
print('é um numero : ',string.isnumeric())
print('é uma string: ',string.isalpha())
print('é um alfa-numerica: ',string.isalnum())
print('é digito: ',string.isdigit())
print('é decimal: ',string.isdecimal())
print('é minuscula: ',string.islower())
print('é maiuscula: ',string.isupper())
print('seu tipo primitivo é ',type(string))