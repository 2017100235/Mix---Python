# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:24:29 2019

@author: juan
"""

from random import randint

x = randint(0,10)
num = int(input('Escolha um numero inteiro entre 0 - 10: '))
cont = 0
print('vc = {}, pc = {}'.format(num,x))
while num != x :
    x = randint(0,10)
    num = int(input('Escolha um numero inteiro entre 0 - 10: '))
    cont+=1
    print('vc = {}, pc = {}'.format(num,x))
    
print('parabens vc acertou o numero, e precisou de',cont,'tentativas')