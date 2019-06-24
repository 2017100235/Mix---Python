# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 01:48:50 2019

@author: juan
"""
from random import randint

print('-='*20)
print('\tVAMOS JOGAR PAR OU IMPAR')
print('-='*20)
cont = 0
while True:
    soma  = 0
    num = int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar? [P/I]: '))
    
    x = randint(0,11)
    soma  = num + x
    
    if soma % 2==0:
        print(f'Você jogou {num} e o pc {x}. total é {soma} deu PAR')
    else: 
        print(f'Você jogou {num} e o pc {x}. total é {soma} deu IMPAR')
    
    if soma%2==0 and escolha.upper() == 'P':
        print('='*40)
        print('\tVocê ganhou essa rodada !')
        cont +=1
        
    elif soma%2!=0 and escolha.upper() == 'I': 
        print('='*40)
        print('\tVocê ganhou essa rodada !')
        cont +=1 
    else: 
        print('='*40)
        print('\t\tVocê perdeu !')
        break
    
print('-='*20)  
print(f'GAME OVER! Você venceu {cont} vezes')