# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:06:00 2019

@author: juan
"""

cad = dict()
gols = list()

total = 0
cad['Nome'] = str(input('Nome: ')).strip().title()
cont = int(input(f'Quantas partidas {cad["Nome"]} jogou: '))
for i in range(0,cont):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
    total += gols[i]
    
cad['Gols'] = gols
cad['Total'] = total
print('-='*20)
print(f'O jogador {cad["Nome"]} jogou {cont} partidas')
for i in range(0,cont):
    print(f'  => Na partida {i+1}, fez {cad["Gols"][i]} gols.')

print(f'Foi um total de {cad["Total"]} Gols')    
