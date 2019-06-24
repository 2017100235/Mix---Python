# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:23:48 2019

@author: juan
"""
num = int(input('digite o numero: '))

milhar = num//1000
num = (num - milhar*1000)
print ('milhar:  ',milhar)

centena = (num//100)
num = (num - centena*100)
print ('centena: ',centena)

dezena = (num//10)
num = (num - dezena*10)
print('dezena:  ',dezena)

unidade = num
print('unidade: ',unidade) 



""" O mesmo codigo, mas usando recurso de string para responder
num = input('digite o numero: ')
print('milhar:  ',num[0:1])
print('centena: ',num[1:2])
print('dezena:  ',num[2:3])
print('unidade: ',num[3:])

"""















