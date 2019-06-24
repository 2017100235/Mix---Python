# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:28:11 2019

@author: juan
"""

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
media = (n1+n2)/2
if (media<5.0):
    print('aluno reprovado')
elif (media>=7.0):
    print('aluno aprovado')
else: 
    print('aluno esta de recuperação')