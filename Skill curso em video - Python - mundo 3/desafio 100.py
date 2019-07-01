# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:32:24 2019

@author: juan
"""

from random import randint
from time import sleep

def somapar(par):
    s = 0
    for i in par:
        if i%2 == 0 :
            s+=i
    print(f'Somando os valores pares de {par} temos {s}')

def sorteio():
    lista = []
    print('Sorteando 5 valores da lista: ',end="")
    for i in range(5):
        sleep (0.3)
        lista.append(randint(0,10))
        print(lista[i], end=" ")
    print('PRONTO !')
    somapar(lista)

# inicio do programa
sorteio()