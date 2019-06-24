# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:08:47 2019

@author: juan
"""
x=''.join(str(input('digite algo: ')).split())
resp = True
fim = (len(x) +1)//2

for i in range(0,fim):
    if x[i] != x[len(x) - 1 - i]: 
        resp  = False
        print('Essa frase não é palindrômo')
        break
    
if resp == True: 
    print('Essa frase é palindrômo')

