# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:19:21 2019

@author: juan
"""

ano = int(input('Digite seu ano de nascimento:'))
idade = 2019 - ano
if idade<18:
    print('Ainda não e hora de se alistar, falta {} anos ainda !'.format(18-idade))
elif idade>18:
    print('''Ja passou da hora de se alistar se você ainda não fez isso,
ja sepassaram {} anos, caso contrario ignore !'''.format(idade-18))
else: 
    print('Esse ano voê tem que se alistar !')