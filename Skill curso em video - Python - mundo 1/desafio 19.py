# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 03:51:04 2019

@author: juan
"""

from random import choice
nome_1 = input('nome 1: ')
nome_2 = input('nome 2: ')
nome_3 = input('nome 3: ')
nome_4 = input('nome 4: ')
lista = [nome_1,nome_2,nome_3,nome_4]
resp = choice(lista)
print('\nO(a) escolhido foi ',resp)