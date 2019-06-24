# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:47:16 2019

@author: juan
"""

ano = int(input('Digite o ano: '))
if ano%4==0:
    if ano%100==0:
        if ano%400==0: 
            print ('Esse ano é Bissexto !')
        else:
            print ('Esse ano não e Bissexto !')
            
    else: 
        print ('Esse ano é Bissexto !')
    
else:
    print ('Esse ano não e Bissexto !')
