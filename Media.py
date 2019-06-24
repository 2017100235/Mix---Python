# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 01:08:06 2019

@author: juan
"""
def media_final(n1,n2,n3):
    
    if n1>n2:
        if n1>n3:
            if n2>n3:
                nova_media_1 = (n1+n2)/2
                print('Sua media final é {}'.format(nova_media_1))
            else:
                nova_media_1 = (n1+n3)/2
                print('Sua media final é {}'.format(nova_media_1))    
            if (nova_media_1>=7):
                print('Parabens você passou !')
            else: 
                print('Infelizmente você não passou!')
          
    if n2>n1:
         if n2>n3:
            if n1>n3:
                nova_media_2 = (n2+n1)/2
                print('Sua media final é {}'.format(nova_media_2))
            else: 
                nova_media_2 = (n2+n3)/2
                print('Sua media final é {}'.format(nova_media_2)) 
            if (nova_media_2>=7):
                print('Parabens você passou !')
            else: 
                print('Infelizmente você não passou!')
            
    if n3>n1:
        if n3>n2:
            if n1>n2:
                nova_media_3 = (n3+n1)/2
                print('Sua media final é {}'.format(nova_media_3))
            else: 
                nova_media_3 = (n3+n2)/2
                print('Sua media final é {}'.format(nova_media_3))
            if (nova_media_3>=7):
                print('Parabens você passou !')
            else: 
                print('Infelizmente você não passou!')
             
    return 0