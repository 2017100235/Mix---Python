# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:47:40 2019

@author: juan
"""
soma = 0
velho = 0
cont = 0
for i in range (1,5):
    nome = input('Qual o seu nome: ')
    idade = int(input('Sua idade: '))
    sexo = input('''Seu sexo:
         - Homem
         - Mulher
         -: ''')
    soma += idade
    
    if sexo.lower() == 'homem':
        if idade > velho:
            velho = idade
            p_velho = nome
            
    if sexo.lower() == 'mulher' and idade <20:
        cont += 1

print('''A media de idade é {};
O nome do homem mais velho é {}, {} anos ;
Nesse grupo tem {} mulheres menores de 20 anos'''. format(soma/4,p_velho,velho,cont))

          
