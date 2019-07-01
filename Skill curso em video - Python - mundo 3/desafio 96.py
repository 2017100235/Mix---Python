# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:18:58 2019

@author: juan
"""

def area(l,c):
    print(f'A area de um terreno {l:.1f}x{c:.1f} e de {l*c:.1f}m²')
    
x = float(input('LARGURA (M): '))
y = float(input('COMPRIMENTO (C): '))
area(x,y)