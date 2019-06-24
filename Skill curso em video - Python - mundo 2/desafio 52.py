# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:56:37 2019

@author: juan
"""

num = int(input('Digite um numero: '))
tot = 0
x=[]

for i in range (1,num+1):
    if num%i == 0: 
        tot +=1
        x.append(i)
if tot == 2:
    print('Esse numero é primo pois ele e divisiveis por',x)
else: 
    print('Esse numero não é primo pois ele e divisiveis por',x)
        