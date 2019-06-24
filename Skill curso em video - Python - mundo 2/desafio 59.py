# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:35:07 2019

@author: juan
"""
def exibir():
    print('''Escolha o que fazer: 
    [1] - somar
    [2] - Multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - sair do programa
     - ''')
    num = int(input())
    return num
    
x = int(input('1º valor: '))
y = int(input('2º valor: '))
resp = exibir()

while resp != 5:
    
    if resp == 1:
        print('A soma é ',x+y)
        
    elif resp == 2:
        print('A multiplicação é ', x*y)
        
    elif resp == 3: 
        if x>y: 
            print('O maior é o valor em X')
        elif x<y: 
            print('O maior é o valor em Y')
        else:
            print('Os valores são iguais')
            
    elif resp == 4:
        x = int(input('1º valor: '))
        y = int(input('2º valor: '))

    elif resp == 5: 
        print('finalizando o programa ! ')
        
    else: 
        print('valor invalido')
        
    resp = exibir()
        
        
        
        
        
        
        
        
        