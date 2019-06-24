# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 03:15:50 2019

@author: juan
"""

from math import hypot 
co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
print('hipotenusa {:.2f}'.format(hypot(co,ca)))