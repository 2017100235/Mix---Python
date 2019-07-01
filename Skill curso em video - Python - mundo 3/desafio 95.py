# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 01:38:31 2019

@author: juan

"""
lista = list()
gols = list()
cad = dict()

while True: 
    total = 0
    cad['Nome'] = str(input('Nome: ')).strip().title()
    cont = int(input(f'Quantas partidas {cad["Nome"]} jogou: '))
    
    for i in range(0,cont):
        gols.append(int(input(f'Quantos gols na partida {i+1}: ')))    
        total += gols[i]
    cad['Gols'] = gols[:]
    cad['Total'] = total
    lista.append(cad.copy())
    cad.clear()
    gols.clear()
    
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    while True: 
        if resp in 'sn': 
            break
        else: 
            print('Erro !',end=" ")
            resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    if resp == 'n':
        break
        
    print('-'*20)
    

print('-='*18)
print('{:<4}{:>7}{:>7}{:>7}'.format('cod','nome','gols','total'))

while True:
    
    print('-'*36)
    for y, x in enumerate(lista):
        print(f'{y:<4} {x["Nome"]:<7} {x["Gols"]}{x["Total"]:>7}',end="")
        print()
            
    print('-'*36)

    
    while True: 
        dados = int(input('Mostra dados de qual jogador: '))
        if dados > len(lista)-1:
            print('Erro !')
            while True: 
                dados = int(input('Mostra dados de qual jogador: '))
                if dados > len(lista)-1:
                     print('Erro !')
                else:
                    break
    
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[dados]["Nome"]}')
        
        a = lista[dados]
        for j,i in enumerate(a['Gols']):
            print(f'No jogo {j} fez {i} Gols')
            
        print()
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()
        while True: 
            if resp in 'sn': 
                break
            else: 
                print('Erro !',end=" ")
                resp = str(input('Quer continuar [S/N]: ')).strip().lower()
        if resp == 'n':
            break
        
    if resp == 'n':
            break