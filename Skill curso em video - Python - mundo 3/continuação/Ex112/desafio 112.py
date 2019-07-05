"""
Created on Thu Jul  4 16:58:51 2019

@author: juan
"""
from utilidadescev.moeda import resumo
from utilidadescev.dados import leiadinheiro

p = leiadinheiro('Digite o preço: R$ ')
resumo(p,80,35)