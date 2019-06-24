# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:58:48 2019

@author: juan
"""

preco = float(input('preço: '))
print('''Qual a forma de pagamento: 
    [1] - dinheiro
    [2] - cheque
    [3] - cartão ''')
x= int(input())

if x == 1 or x== 2: 
    print('o seu produto tem 10% de desconto , ficando com o valor de R$', preco*0.9)
elif x==3: 
    print(''' o pagamento com o cartão será: 
        [4] - A vista
        [5] - Em 2x
        [6] - Em 3x ou mais''')
    resp = int(input())
    if resp == 4: 
        print('O produto tera desconto de 5%,e ficará no valor de R$', preco*0.95)
    elif resp == 5:
        print('O produto não tera desconto e ficará no valor de R$', preco)
    elif resp == 6: 
        print('O seu produto terá um juros de 20% é ficará no valor de R$', preco*1.20)
    else: 
        print('opção invalida')
else: 
    print('opção invalida')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    