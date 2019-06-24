# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 02:15:16 2019

@author: juan
"""
from random import choice


a = True
while (a):
    resp = input('''Escolha: 
         - Pedra
         - Papel
         - Tesoura 
         : ''')
    
    comp = ['pedra','papel','tesoura']
    resultado = choice(comp)
    print('sua escolha = {}, pc = {}'. format(resp,resultado))
    
    if resp == resultado: 
        print('Empate !')
        
    elif resp.lower() == 'papel': 
        if (resultado == 'pedra'):
            print('Você ganhou ! ')
        else: 
            print('Você perdeu pro pc!!!')
    
    elif (resp.lower()=='pedra'):
        if (resultado == 'tesoura'):
            print('Você ganhou ! ')
        else:
            print('Você perdeu pro pc!!!')
    
    elif (resp.lower() == 'tesoura'): 
        if(resultado == 'papel'):
            print('Você ganhou ! ')
        else:
            print('Você perdeu pro pc!!!')
    else:
        print('digitou errado')
    
    continuar = int(input(''' Quer continuar: 
        [1] - sim
        [2] - não
        : '''))
        
    if continuar == 2:
        a = False

input('Digite algo para finalizar !... ')