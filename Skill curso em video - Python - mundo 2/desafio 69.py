# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 02:16:41 2019

@author: juan
"""
cont_18 = 0
cont_h = 0
cont_m = 0
while True :
    nome = str(input('nome: ')).strip()
    idade= int(input('idade: '))
    sexo = str(input('sexo [M/F]')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]')).strip().upper()
        
    if idade > 18:
        cont_18 += 1
    
    if sexo == 'M':
        cont_h += 1
        
    if sexo == 'F' and idade < 20:
        cont_m += 1
    
    resp = str(input('Quer continuar: [S/N]')).strip().upper()
    
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()
        
    if resp == 'N': 
        break
print(f'''
Exite {cont_18} maior  de 18 anos
Tem {cont_h} homens cadastrados
Tem {cont_m} mulher menor de 20 anos
''')