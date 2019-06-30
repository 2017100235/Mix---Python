# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:34:15 2019

@author: juan
"""
from random import sample
from time import sleep

num = []

print('='*33)
print('\tJogo da mega sena')
print('='*33)

x = int(input('Quantos jogos você quer sortear: '))
print(f'-=-=-= Sorteando {x} jogos -=-=-=') 

for i in range(x):
    sleep(1)
    num.append(sample(range(1,61),k=6))
    num[i].sort()
    print(f'jogo {i+1}: {num[i]}')
    
print(f'-=-=-=-=-= Boa sorte -=-=-=-=-=')




