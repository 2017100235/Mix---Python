# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:34:18 2019

@author: juan
"""

#Precisa do arquivo Media para funcionar
import Media


print('Notas Unicarioca\n')
av1 = (float(input('AV1: ')))
av2 = (float(input('AV2: ')))
media  = (av1+av2)/2

if (media >= 7): 
    print('''\nVocê já esta aprovado, deseja fazer av3:
    - Sim
    - Não''')
    resp = input()
    if (resp.lower() == 'sim'):
        av3 = (float(input('AV3: ')))
        Media.media_final(av1,av2,av3)
    else: 
        print('Parabens você passou ! sua media é ', media)
else: 
    print('Voce necessita fazer AV3')
    av3 = (float(input('AV3: ')))
    Media.media_final(av1,av2,av3)   

input('Digite algo para finalizar ! ...')