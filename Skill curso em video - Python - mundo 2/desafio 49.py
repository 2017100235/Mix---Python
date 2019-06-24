# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:08:29 2019

@author: juan
"""

n = int(input('Digite um numero: '))
print('Tabuada do ',n)
for i in range(1,11):
    print('{} x {} = {}'.format(n,i,n*i))