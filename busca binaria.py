# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:18:25 2019

@author: juan
"""
#Busca binaria com 10 valores 
lista = []
print('-='*16)
print('\tCadastro da lista')
print('-='*16)
for i in range(10):
    lista.append(int(input('Digite um numero: ')))
  
lista.sort()
print('-='*16)
print(f'Sua lista ordenada \n{lista}')

num = int(input('Qual valor quer buscar na lista: '))

ini = 0
fim = len(lista) - 1
meio = (ini + fim)//2

while True: 
        if num == lista[meio]:
            print(f'O nº {num} esta na lista')
            break
        
        if num > lista[meio]:
            ini = meio + 1
            meio = (ini + fim)//2
                
        if num < lista[meio]:
            fim = meio - 1
            meio = (ini + fim)//2 
            
        if ini == fim: 
            if num != lista[meio]:
                print('Valor não encontrado !')
                break
            else: 
                print(f'O nº {num} esta na listaaaa')
                break
    

        
        
        
        
        
        
        