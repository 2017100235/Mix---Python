# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:52:58 2019

@author: juan
"""

aluno = {}
lista = []

while True:
    
    aluno['nome'] = str(input('nome: ')).strip().title()
    aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'
    
    lista.append(aluno.copy())
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    if resp =='n':
        break

for i in lista:
    for x , y in i.items():
        print(f'{x:<4} {y:>7}', end=" ")
    print()
        
        