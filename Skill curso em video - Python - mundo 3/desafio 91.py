# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:15:56 2019

@author: juan
"""

from random import randint
from time import sleep
from operator import itemgetter

lista = []
jogadores = {
'jogadores1': randint(1,6),
'jogadores2': randint(1,6),
'jogadores3': randint(1,6),
'jogadores4': randint(1,6)}

print('valores sorteados: ')
for k,v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou {v}')
    
lista = sorted(jogadores.items(), key=itemgetter(1), reverse = True)

print('\nRank dos vencedores: ')
for i,x in enumerate(lista):
    sleep(1)
    print(f'{i+1}º lugar: {x[0]} com {x[1]}')
        
        
        
        
        
        
        
        
        
        
        
