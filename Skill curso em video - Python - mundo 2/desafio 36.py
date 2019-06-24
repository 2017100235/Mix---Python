# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:31:11 2019

@author: juan
"""

casa = float(input('valor da casa: '))
salario = float(input('valor do salario: '))
anos = int(input('quantos anos vc vai pagar: '))
parcela = (casa/(anos*12))

print('valor das parcelas é R$ {:.2f}'.format(parcela))
if parcela > salario*0.3: 
    print('lamentamos mas não será possivel parcerlar')
else: 
    print('Ok, acordo fechado ')