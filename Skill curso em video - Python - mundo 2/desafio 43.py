# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:48:11 2019

@author: juan
"""

peso = float(input('Seu peso: '))
altura = float(input('sua altura: '))
imc = peso/(altura**2)
print('Seu imc é {:.2f}'.format(imc))
if imc <18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso normal')
elif imc>=25 and imc <30: 
    print('Sobrepeso')
elif imc>=30 and imc <=40:
    print('obesidade')
else: 
    print('obesidade morbida')