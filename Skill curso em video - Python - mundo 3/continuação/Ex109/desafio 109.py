"""
Created on Thu Jul  4 16:58:51 2019

@author: juan
"""
import moeda
p = float(input('Digite o preço: R$ '))
print(f'''
A metade de {moeda.moeda(p)} vale {moeda.metade(p,True)}
O dobro de {moeda.moeda(p)} vale {moeda.dobro(p,True)}
Aumentando 15%, temos {moeda.aumento(p,15,True)}
Reduzido 13%, teremos {moeda.reduzir(p,13,True)}''')