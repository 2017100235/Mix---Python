# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:43:29 2019

@author: juan
"""

import random 

x = random.randint(0,5)
num = int(input('digite um numero entre 0-5 : '))
if x == num:
    print('Você acertou o numero! \n escolhido = {}, radomizado = {} '.format(num,x))
else: 
    print('Você errou o numero !\n escolhido = {}, radomizado = {}'.format(num,x))
