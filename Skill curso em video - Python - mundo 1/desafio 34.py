# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:48:34 2019

@author: juan
"""

salario = float(input('Qual o seu salario: '))
if salario>1250.00:
    print('Seu salario teve um reajuste de 10% passando a valer R${:.2f}'.format(salario*1.10))
else:
    print('Seu salario teve um reajuste de 15% passando a valer R${:.2f}'.format(salario*1.15))