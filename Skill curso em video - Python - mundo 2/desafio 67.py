# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 01:39:53 2019

@author: juan
"""

while True: 
    num = int(input('Quer ver qual tabuada: '))
    if num < 0 :
        break
    for i in range (1,11):
        print(f'{num} x {i} = {num*i}')
        