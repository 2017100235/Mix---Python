# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 02:35:04 2019

@author: juan
"""
soma  = 0
cont = 0

barato = nome = str(input('nome do produto: ')).strip()
valor_barato = valor = float(input('valor: '))

while True: 
    
    soma+=valor
    if valor > 1000:
        cont += 1
    resp = str(input('Quer continuat [S/N]: ')).strip().lower()
    while resp not in 'sn':
         resp = str(input('Quer continuat [S/N]: ')).strip().lower()
    if resp == 'n':
        break

    nome = str(input('nome do produto: ')).strip()
    valor = float(input('valor: '))
    
    if valor < valor_barato: 
        barato = nome

print(f'''
Total gasto {soma:.2f},
{cont} custa mais de R$1000,00
{barato} é o produto mais barato
      ''')
    
    
    
    
    
    