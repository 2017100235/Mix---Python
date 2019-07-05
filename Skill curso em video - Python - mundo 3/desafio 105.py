# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:48:16 2019

@author: juan
"""
def notas(*n, sit=False):
    """-> função para analisar notas e situação de varios alunos
    n = notas de todos os alunos
    sit = e a situação da turma , ela e opcional
    return =  retorna o dicionario com todas as informações da turma 
    """
    turma = {}
    
    turma['tamanho'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = 0
    
    for i in n:
        turma['media'] += i   
    turma['media'] = turma['media']/turma['tamanho']
    
    if sit == False:
        return(turma)
    else: 
        if turma['media'] >= 7:
            turma['situação'] = 'BOA'
        elif 6 <= turma['media'] < 7:
            turma['situação'] = 'Regular'
        else: 
            turma['situação'] = 'Ruim'
        return(turma)
   



resp = notas(5,4,8,7,6,6,6,sit=True)
print(resp)
#help(notas)