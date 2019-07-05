# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:58:56 2019

@author: juan
"""

def metade(num):
    return f'R$ {num/2:.2f}'.replace('.',',')

def dobro(num):
    return f'R$ {num*2:.2f}'.replace('.',',')

def aumento(num):
    return f'R$ {num*1.10:.2f}'.replace('.',',')

def reduzir(num):
    return f'R$ {num*0.87:.2f}'.replace('.',',')

def moeda(num):
    return f'R$ {num:.2f}'.replace('.',',')