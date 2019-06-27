# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:30:44 2019

@author: juan
"""
x=[]
cont_1 = 0
cont_2 = 0
x.append(str(input('Digite a expressão: ')).strip())

for i in range(0,len(x[0])):
    if x[0][i] == '(':
        cont_1+=1
    if x[0][i] == ')':
        cont_2+=1
        
if cont_1 == cont_2:
    print('A expressão esta correta !')
else:
    print('Sua expressão esta errada !')
    
    
    
''' Pode ser feito assim, usando como string
   
x = str(input('Digite a expressão: ')).strip()
if x.count('(') == x.count(')'):
    print('A expressão esta correta !')
else:
    print('Sua expressão esta errada !')