# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:39:20 2019

@author: juan
"""
#Escrever criando um arquivo 
p = open("tests.txt","a")
p.write('''
        Eu amo o python
        Meu python minha vida''')

p.close()