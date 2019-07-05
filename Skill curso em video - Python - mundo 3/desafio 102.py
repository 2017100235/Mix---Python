# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 23:04:49 2019

@author: juan
"""

def fatorial(n,show=False):
    '''->Calcula o fatorial de um numero.
    para n: O numero a ser calculado
    para show: (opcional) mostra ou não a conta
    return: O valor do fatorial de um numero n.
    ''' 
    resp = 1
    print('='*27)
    if show == False: 
        for i in range(n,0,-1):
            resp *= i
        return resp
    
    else: 
        for i in range(n,0,-1):
            resp *= i
            
            if i > 1:
                print (f'{i} x ',end="")
            else:
                print(f'{i} = ',end="")
        return resp
    
#help(fatorial)   
print(fatorial(6,True))
    
