# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:42:38 2019

@author: juan
"""

# Salve todas as musicas na mesma pasta que esse algoritmo
# Depois, é so coloca-lo pra funcionar :)
import emoji
from pygame import mixer
from glob import glob

lista = []
for i in glob('*.mp3*'):
    lista.append(i)
while True: 
    for i in range(0, len(lista)-1):
        mixer.init()
        mixer.music.load(lista[i])
        mixer.music.load(lista[i])
        mixer.music.play()
    
        input('Tecle algo para passar de musica ... ')
        
    print(emoji.emojize('Sua play list terminou :disappointed:',use_aliases=True))
    resp = str(input(emoji.emojize('Quer escutar novamente [S/N] :smiley:: ',use_aliases=True))).strip().lower()
    while True:
        if resp  not in 'sn':
            resp = str(input('Digite novamente: ')).strip().lower()
        else: 
            break
    if resp == 'n':
        input('Tecle "Enter" para sair ...')
        break
    else:
        print(emoji.emojize('\n:wink:', use_aliases=True))