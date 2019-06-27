# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:23:26 2019

@author: juan
"""
lista = []

while True: 
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        resp = str(input('''Valor adicionado com sucesso...
Quer continuar? [S/N]: ''')).strip().lower()
        if resp == 'n':
            break
    else:
        resp = str(input('''Valor Duplicado, não vou adicionar...
Quer continuar? [S/N]: ''')).strip().lower()
        if resp == 'n':
            break

print('-='*20)
print(f'Você digitou os valores {sorted(lista)}')



