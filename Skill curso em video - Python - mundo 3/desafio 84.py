# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:26:58 2019

@author: juan
"""
lista = []
cadastro = []
num = []
while True: 
    cadastro.append(str(input('nome: ')).strip())
    cadastro.append(float(input('peso: ')))
    num.append(cadastro[1])
    lista.append(cadastro[:])
    cadastro.clear() 
    
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    if resp == 'n':
        break 
    
print('-='*20)

print(f'Ao todo foram cadastrado {len(lista)} pessoas')

print(f'O maior peso foi de {max(num):.1f}Kg. Peso de ',end='')
for i in range(0,len(lista)):
    if lista[i][1] == max(num):
        print(lista[i][0],end=" ")
        
print(f'\nO menor peso foi de {min(num):.1f}Kg. Peso de ',end='')
for i in range(0,len(lista)):
    if lista[i][1] == min(num):
        print(lista[i][0],end=" ")


    
    
    
    
    
    
    
    
    
    
    