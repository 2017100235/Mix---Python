# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:33:08 2019

@author: juan
"""
from random import choices
x = tuple(choices(range(0,10),k=5))
print(f'{x} \n Maior = {max(x)} \n Menor = {min(x)}')