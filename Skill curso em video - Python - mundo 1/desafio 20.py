# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 04:02:19 2019

@author: juan
"""

from random import shuffle
nome_1 = input('nome 1: ')
nome_2 = input('nome 2: ')
nome_3 = input('nome 3: ')
nome_4 = input('nome 4: ')
lista = [nome_1,nome_2,nome_3,nome_4]
resp = shuffle(lista)
print('\nO(a) escolhido foi ', lista)