# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:54:29 2018

@author: Usuário
"""
filePlayers = ""

for i in range(0, 2161):
    filePlayers += "aaa" + str(i) + "\n"
        
#Escreve os jogadores criados em um arquivo txt, ja em um formato pronto para exportar ao Excel
with open('teste_base.txt', 'w') as f:
	f.write(filePlayers)