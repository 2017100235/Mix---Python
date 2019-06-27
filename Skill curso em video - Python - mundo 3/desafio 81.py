# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:44:38 2019

@author: juan
"""
num = []
cont = 0
while True:
    num.append(int(input('digite um valor: ')))
    cont +=1
    resp = str(input('Quer continuar ? [S/N]: ')).strip().lower() 
    if resp == 'n':
        break
num.sort(reverse=True)
print(f'''voce digitou {cont} elementos
A lista decrescente = {num}''')
if 5 in num:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')