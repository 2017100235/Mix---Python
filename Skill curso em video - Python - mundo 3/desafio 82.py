# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:02:01 2019

@author: juan
"""
lista = []
par = []
impar = []

while True:
    
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    if resp == 'n':
        break

for i in lista:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)
        
print(f'A lista = {lista}\nPar = {par} \nImpar = {impar}')



''' #Tambem pode ser feito assim 
while True:
    
    lista.append(int(input('Digite um valor: ')))
    num = lista[len(lista)-1]
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()
    if resp == 'n':
        break
        
print(f'A lista = {lista}\nPar = {par} \nImpar = {impar}')
'''