# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:39:47 2019

@author: juan
"""

#Para o programa funcionar é necessario o arquivo calculos
import calculos

# inicio do programa
num = int(input('digite um numero inteiro: '))
print('Escolhar uma das opções para converter: ')
print('1 - numero binario')
print('2 - numero octal')
print('3 - numero hexadecimal')

x = int(input())
print('\n')

if(x==1):
    op_1 = calculos.base_2(num)
    print(num,'seu equivalente na base 2 vale: ')
    calculos.exibir(op_1)  
    
elif(x==2):
    op_2 = calculos.base_8(num)
    print(num,'seu equivalente na base 8 vale: ')
    calculos.exibir(op_2)
    
elif(x==3): 
    op_3 = calculos.base_16(num)
    print(num,'seu equivalente na base 16 vale: ')
    calculos.exibir(op_3)
else: 
    print('opção invalida !')
 
input('\n\nTecle algo para finalizar !...')
 