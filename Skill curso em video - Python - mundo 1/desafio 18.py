# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 03:30:15 2019

@author: juan
"""

from math import sin,cos,tan,radians
x=int(input('angulo: '))
print('sen({}º) = {:.3f}'.format(x,sin(radians(x))))
print('cos({}º) = {:.3f}'.format(x,cos(radians(x))))
print('tan({}º) = {:.3f}'.format(x,tan(radians(x))))