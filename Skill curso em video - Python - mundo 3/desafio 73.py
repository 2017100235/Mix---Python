# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:55:30 2019

@author: juan
"""

times = ('Palmeiras','Santos','Flamengo','Internacional',	
'Atlético-MG','Goiás','Botafogo','Bahia','São Paulo','Corinthians',	
'Grêmio','Athletico-PR','Ceará','Fortaleza','Vasco','Fluminense',	
'Chapecoense','Cruzeiro','CSA','Avaí')

print(f'Os cinco 1º colocados são {times[:6]}\n')
print(f'Os quatro ultimos colocados são {times[16:]}\n')
print(f''' Todos os times do brasileirão : 
{sorted(times)}''')
print(f"\n A Chapecoence se encontra na posição {times.index('Chapecoense')+1}")