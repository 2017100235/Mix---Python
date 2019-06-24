# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:33:41 2019

@author: juan
"""

termo = int(input('Termo: '))
razao = int(input('Razão: '))
cont = 1
pa = termo+razao
print(termo)

while cont < 10:
    print(pa)
    pa+=razao
    cont+=1

resp = int(input('Quer exibir mais quantos valores: '))

while resp !=0:
    cont = 1    
    while cont < resp + 1:
        print(pa)
        pa+=razao
        cont+=1
    resp = int(input('Quer exibir mais quantos valores: '))
    






