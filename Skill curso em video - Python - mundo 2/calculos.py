# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:28:55 2019

@author: juan
"""

# funções para os calculos de converção
def base_2(divisor):
    resp = []
    while(divisor != 0):
        resp.append(divisor%2)
        divisor = (divisor//2)
    
    return resp

def base_8(divisor):
    resp = []
    while(divisor != 0):
        resp.append(divisor%8)
        divisor = (divisor//8)
    
    return resp

def base_16(divisor):
    resp = []
    while(divisor != 0):
        z = divisor%16
        if (z>=10):  
            a = 65
            for i in range (10,16):
                if (z == i):
                    resp.append(chr(a))
                    divisor = (divisor//16)
                else:
                    a+=1
        else:
            resp.append(divisor%16)
            divisor = (divisor//16)
           
    return resp

def exibir(valor):
    a = True
    while(a):
        if(len(valor)==0):
            a = False
        else: 
            print(valor.pop(),end='')
    return 0
