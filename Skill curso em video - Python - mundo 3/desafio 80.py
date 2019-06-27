# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:24:40 2019

@author: juan

     
"""

lista = []

num = int(input('Digite um numero: '))
lista.append(num)
print('Adicionado ao final da lista...')  
 
for i in range(1,5):
    num = int(input('Digite um numero: '))
    
    if num >= max(lista): 
        lista.append(num)
        print('Adicionado ao final da lista...')  
        
    elif num <= min(lista):
        compri = len(lista)
        lista.append(lista[compri-1])
        for x in range(compri,0,-1):
            lista[x] = lista[x-1]
            
        lista[0] = num
        print('Adicionado na posição 0 da lista...') 
        
    else:
        for j in range(1,len(lista)):
            if num <= lista[j]:
                compri = len(lista) - 1
                lista.append(lista[compri])
                for x in range(compri,0,-1):
                    lista[x] = lista[x-1]
                  
                lista[j] = num
                print(f'Adicionado na posição {j} da lista... ')
       
            if num > lista[j]:
                compri = len(lista)-1
                lista.append(lista[compri])
            
                for x in range(0,compri):
                    if num < lista[x] :
                        lista[x + 1] = lista[x]
                lista[j + 1] = num
                print(f'Adicionado na posição {j+1} da lista... ')
            break

print('-='*20)
print(lista)