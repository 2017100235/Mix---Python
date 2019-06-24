# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:48:00 2019

@author: juan
"""

num_1 = int(input('1º numero: '))
num_2 = int(input('2º numero: '))
num_3 = int(input('3º numero: '))

if (num_1>num_2):
    if(num_1>num_3):
        if(num_2>num_3):
            print('o maior é {} é o menor {}'.format(num_1,num_3))
        else: 
            print('o maior é {} é o menor {}'.format(num_1,num_2))

if (num_2>num_1):
    if(num_2>num_3):
        if(num_1>num_3):
            print('o maior é {} é o menor {}'.format(num_2,num_3))
        else: 
            print('o maior é {} é o menor {}'.format(num_2,num_1))
            
if (num_3>num_1):
    if(num_3>num_2):
        if(num_1>num_2):
            print('o maior é {} é o menor {}'.format(num_3,num_2))
        else: 
            print('o maior é {} é o menor {}'.format(num_3,num_1))
