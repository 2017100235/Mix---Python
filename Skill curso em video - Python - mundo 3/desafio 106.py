# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:19:26 2019

@author: juan
"""

def exibir():
    print('~'*25)
    print('SISTEMA DE AJUDA PyHELP')
    print('~'*25)
    
def manual(string):
    print('~'*(35 + len(string)))
    print(f" acessando o manual do comando '{string}'")
    print('~'*(35 + len(string)))
    help(string)

while True:
    exibir()
    resp = str(input('Função ou Biblioteca (fim para encerrar): ')).strip().lower()
    if resp == 'fim':
        break
    else:
        manual(resp)


        
