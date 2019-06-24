# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 00:05:16 2019

@author: juan
"""

x = 0
y = 1
num = int(input('Qual o numero de interações: '))
print(x, end=' -> ')
print(y, end=' -> ')
while num != 2: 
    fib = x+y
    print(fib, end=' -> ')
    x = y
    y = fib
    num-=1
print('FIM')