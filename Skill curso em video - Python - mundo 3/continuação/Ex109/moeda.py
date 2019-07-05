# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:58:56 2019

@author: juan
"""


def metade(num=0,f=False):
    if f==True:
        return f'R$ {num/2:.2f}'.replace('.',',')
    else:
        return num/2


def dobro(num=0,f=False):
    if f==True:
        return f'R$ {num*2:.2f}'.replace('.',',')
    else:
        return num*2


def aumento(num=0,t=0,f=False):
    if f==True:
        return f'R$ {num*(1+(t/100)):.2f}'.replace('.',',')
    else:
        return num*(1+(t/100))


def reduzir(num=0,t=0,f=False):
    if f==True:
        return f'R$ {num*(1-(t/100)):.2f}'.replace('.',',')
    else:
        return num*(1-(t/100))


def moeda(num=0):
    return f'R$ {num:.2f}'.replace('.',',')