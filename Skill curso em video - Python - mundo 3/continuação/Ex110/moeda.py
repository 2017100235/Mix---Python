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

def resumo(valor=0,aum=0,redux=0):
    print('=' * 30)
    print("       RESUMO DO VALOR     ")
    print('=' * 30)

    print(f'Preço analisado:{moeda(valor):>14}')
    print(f'Dobro do preço:{dobro(valor,True):>15}')
    print(f'Dobro do preço:{dobro(valor,True):>15}')
    print(f'Metade do preço:{metade(valor,True):>13}')
    print(f'{aum}% de aumento:{aumento(valor,aum,True):>15}')
    print(f'{redux}% de redução:{reduzir(valor,redux,True):>15}')

    print('=' * 30)