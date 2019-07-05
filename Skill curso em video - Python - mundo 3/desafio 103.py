# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:06:54 2019

@author: juan
"""

def ficha(n, g):
    '''-> Ficha ira exibir a descrição(Nome e Gols) de um jogador
     n = Nome do jogador informado 
     g = Gols do jogador que foi informado
    ''' 
    if n == '':
        n = '<Desconhecido>'
    print(f'O jogador {n} fez {g} Gol(s) no campeonato')
    


# progrma principal
nome=str(input('Nome do jogador: '))
gols=str(input('Gols do jogador: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(n=nome, g=gols)