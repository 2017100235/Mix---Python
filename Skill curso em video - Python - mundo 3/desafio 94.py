# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:28:00 2019

@author: juan
"""
lista = []
pessoa = {}

media = 0

while True: 
   
    pessoa['Nome']= str(input('Nome: ')).strip().title()
    while True: 
        pessoa['Sexo']= str(input('Sexo [M/F]: ')).strip().lower()
        if pessoa['Sexo'] in 'mf':
            break
        else:
            print('Erro !')
        
    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']
    
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()
        if resp in 'sn':
            break
        else:
            print('Erro !')
    
    if resp == 'n':
        break
    
media = (media/(len(lista)))

print(f''' Foram cadastradas {len(lista)} pessoas 
A media de idade foi {media:.1f} anos
As mulheres do cadastro são ''',end="")

for i in lista: 
    if i['Sexo'] == 'f':
        print(f'{i["Nome"]}', end=" ")

print(f'\nAs pessoas com idade acima da media é ')
print()
for i in lista:
    if i['Idade'] > media:
        print(f'{i["Nome"]} sexo:{i["Sexo"]} {i["Idade"]} anos')
       
        

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    