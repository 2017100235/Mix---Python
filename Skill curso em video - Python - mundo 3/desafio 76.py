# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:49:57 2019

@author: juan
"""


carrinho = ('Lápis',1.75,'Borracha',2.00,
           'Caderno',15.90,'Estojo',25.00,
           'Transferidor',4.20,'Compasso',9.99,
           'Mochila',120.32,'Canetas',22.30,
           'livros',34.90)
print('-'*34)
print('\tLISTAGEM DE PREÇO')
print('-'*34)
comp = len(carrinho)

for i in range(0,comp-1,2):
    print(f'{carrinho[i]:.<22} R${carrinho[i+1]:>7.2f}')

print('-'*34)

