# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:08:56 2019

@author: juan
"""
nome = input('digite o seu nome: ')

print('nome em maiusculo = ',nome.upper())
print('nome em mainusculo = ',nome.lower())
print('total de caracteres sem espaços =',len(''.join(nome.split())))
nome = nome.split()
print('total de caracteras do 1º nome =',len(nome[0]))