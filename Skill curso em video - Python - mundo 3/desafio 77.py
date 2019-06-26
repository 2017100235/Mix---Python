# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:58:46 2019

@author: juan
"""

palavra = ('aprender','programar','linguagem','python',
           'curso','gratis','estudar','praticar',
           'trabalhar','mercado','programador','futuro')

for i in palavra: 
    print(f'\nNa palavra {i.upper()} temos',end=' ') 
    for x in range(0,len(i)):
        if i[x] in 'aeiou':
            print(i[x],end=' ')
