# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:38:05 2019

@author: juan
"""
from time import sleep

def contador(ini,fim,passo):
    print('-='*16)
    print(f'Contagem de {ini} ate {fim} de {passo} em {passo}')
    if ini <= fim: 
        for i in range(ini,fim + 1,passo):
            sleep(0.5)
            print(i,end=" ")    
    else:
        if passo < 0:
            for i in range(ini,fim - 1,passo):
                sleep(0.5)
                print(i,end=" ")
        elif passo == 0: 
            for i in range(ini,fim - 1,-1):
                sleep(0.5)
                print(i,end=" ")
        else:
            for i in range(ini,fim-passo,-passo):
                sleep(0.5)
                print(i,end=" ")
    print('FIM!')

# contagem de 1 a 10 passo1    
contador(1,10,1)

# contagem de 10 a 0 passo-2
contador(10,0,2)

# contagem personalizada
print('Agora e sua vez de personalizar a contagem!')
x = int(input('Inicio: '))
y = int(input('Fim: '))
z = int(input('Passo: '))

contador(x,y,z)




