"""
Created on Thu Jul  4 16:58:51 2019

@author: juan
"""
import moeda
p = float(input('Digite o preço: R$ '))
print(f'''
A metade de {p} vale {moeda.metade(p):.2f}
O dobro de {p} vale {moeda.dobro(p):.2f}
Aumentando 10%, temos {moeda.aumento(p):.2f}
Reduzido 13%, teremos {moeda.reduzir(p):.2f}''')