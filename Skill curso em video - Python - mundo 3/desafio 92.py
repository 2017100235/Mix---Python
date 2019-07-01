# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:32:53 2019

@author: juan
"""
from datetime import datetime

cadastro = dict()

cadastro['Nome'] = str(input('nome: ')).strip().title()
born = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - born
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem):'))

f cadastro['CTPS'] == 0:
    for k,v in cadastro.items():
        print(f'{k} tem valor {v}')
else: 
    cadastro['Ano'] = int(input('Ano da contratação: '))
    cadastro['Aalario'] = float(input('Salario: '))
    cadastro['Aposentadoria'] = (cadastro['ano'] + 35) - born
    for k,v in cadastro.items():
        print(f'{k} tem valor {v}')
