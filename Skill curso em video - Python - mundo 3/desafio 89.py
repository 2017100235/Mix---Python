# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:36:33 2019

@author: juan
"""
turma = []
nome = []
nota = []

while True: 
    nome.append(str(input('nome: ')).strip().title().split()[0])
    nota.append(float(input('nota 1: ')))
    nota.append(float(input('nota 2: ')))
    media = (nota[0] +nota[1])/2
    nome.append(nota[:])
    nome.append(media)
    turma.append(nome[:])
    nome.clear()
    nota.clear()
    
    resp = str(input('Quer continuar[S/N]: ')).strip().lower()
    while True:
        if resp not in 'sn':
            resp = str(input('Digitou errado!\nQuer continuar[S/N]: ')).strip().lower()
        else:   
                break
    if resp == 'n':
        break

print('='*22)
print('{:<4}{:<10}{:>7}'.format('Nº','Nome','Media'))
print('-'*22)

for posi,i in enumerate(turma):
    print('{:<4}{:<10}{:>7.1f}'.format(posi,i[0],i[2]))

print('-'*22)

while True:
    num = int(input('Mostra notas de qual aluno? (999 interrompe):'))
    if num == 999:
        break
    elif num <=len(turma)-1:
        print(f'Notas de {turma[num][0]} são {turma[num][1]}')
        print('-'*22)
    else: 
        print('Digitou errado tente novamente! ')

print('FINALIZANDO... \n<<<VOLTE SEMPRE>>>')    