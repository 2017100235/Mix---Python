# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:18:01 2019

@author: juan
"""

def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade >= 65 or 16<=idade>18:
        print(f'com {idade} anos: Voto opcional !')
    elif idade >= 18:
        print(f'com {idade} anos: Voto obrigatorio !')
    else:
        print(f'com {idade} anos: Voto não obrigatorio !')


print ('='*20)
num = int(input('Em que ano você nasceu: '))
voto(num)