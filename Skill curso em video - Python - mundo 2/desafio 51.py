# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:43:22 2019

@author: juan
"""

termo = int(input('Primeiro termo: '))
razao=  int(input('Razão:' ))
n = termo + razao
print(termo)
for i in range (1,10):
    print(n)
    n+= razao