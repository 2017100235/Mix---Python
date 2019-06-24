# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 02:53:57 2019

@author: juan
"""
print('-='*16)
print('\t Banco Inter')
print('-='*16)
num = int(input('Qual o valor para sacar: '))

nota_50 = num // 50
num  = num - nota_50 * 50

nota_20 = num // 20
num = num - nota_20 * 20

nota_10 = num // 10
num = num - nota_10 * 10
 
print(f'''
Total de {nota_50} de cedulas de R$ 50,00
Total de {nota_20} de cedulas de R$ 20,00
Total de {nota_10} de cedulas de R$ 10,00
Total de {num} de cedulas de R$ 1,00       
''')
