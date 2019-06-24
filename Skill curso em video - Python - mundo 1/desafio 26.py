# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:25:17 2019

@author: juan
"""

frase = input('Digite: ')
print('Sua frase tem {}, letas "a"'.format(frase.count('a')))
print('Na sua frase a letra "a" aparece na primeira vez na posição',
      frase.find('a'))
print('Na sua frase a letra "a" aparece na ultima vez na posição',
      frase.split().pop().find('a'))