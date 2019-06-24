# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:13:26 2019

@author: juan
"""

sexo = (str(input('Seu sexo: [M/F]: '))).strip().lower()
    
while sexo not in 'mf':
    sexo = (str(input('Digite novamente, Seu sexo: [M/F]: '))).strip().lower()
    print(sexo)
print('Sexo OK!')