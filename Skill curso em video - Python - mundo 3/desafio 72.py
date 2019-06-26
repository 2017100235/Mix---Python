# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:39:36 2019

@author: juan
"""

x= ('zero','um','dois','três','quatro','cinco',
    'seis','sete','oito','nove','dez','onze',
    'doze','treze','quatorze','quinze','desesseis',
    'dezessete','dezoito','dezenove','vinte')

while True: 
    num = int(input("Digite um numero entre 0 e 20: "))
    if num >=0 and num<=20:
        break
    
print(f'você digitou o numero {x[num]}')    