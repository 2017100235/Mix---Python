# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 00:46:02 2019

@author: juan
"""
n = int(input('Digite um valor: '))
print ('\tTabuada do ', n)
for i in range(1,11):
    print ('\t{} x {:2} = {}'.format(n,i,n*i))