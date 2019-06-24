# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:12:21 2019

@author: juan
"""
#fatorial usando o for
num = int(input('Digite um numero : '))
x = num
fat = 1

for i in range(num,0,-1):
    fat *= i 

print('o fatorial de {} é {}'.format(x,fat))

"""
# fatorial usando o while
num = int(input('Digite um numero : '))
x=num
fat = 1
while num !=1:
    fat *=num
    num-=1
    
print('o fatorial de {} é {}'.format(x,fat))
"""

