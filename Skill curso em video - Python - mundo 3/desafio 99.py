# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:04:21 2019

@author: juan
"""
from time import sleep
def maior(*num):
   print('-='*22)
   print('Analisando valores passados ...')
   for j,i in enumerate(num):
       sleep(0.5)
       print(i,end=" ")
   print(f'Foram informados {len(num)} valores ao todo')
   if len(num) > 0:
       print(f'O maior valor informado foi {max(num)}')
   else:
       print(f'O maior valor informado foi 0')
   print()



maior(2,9,4,5,7,1)

maior(4,7,0)

maior(1,2)

maior(6)

maior()
