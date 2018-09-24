# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:00:50 2018

Código criado para gerar tabelas de campeonatos

@author: Douglas Barbino
"""

import json
import math
import numpy as np
import pandas as pd
import sys

#Importa o dado do arquivo, sendo necessario avisar que o tipo eh str
dataTeams = pd.read_csv("times.txt", delimiter='*', index_col=False, dtype=str, na_values=' ', keep_default_na=False, comment='#')
#data = pd.read_csv(sys.argv[1], delimiter='*', index_col=False, dtype=str, na_values=' ', keep_default_na=False, comment='#')
#Converte os dados para um vetor numpy de tipo string
dataTeams = (dataTeams.values).astype(str)
#Como o np.split retorna uma matriz [N, 1], usa-se a funcao np.flatten para transformar em um vetor
dataTeams = dataTeams.flatten()

#Leitura do arquivo JSON
with open('chaveamento_jogos.json') as data_file:
    dataLeague = json.load(data_file)
    
#Contador de rodadas
numberMatchday = 0

#Leitura das rodadas do torneio com aquele numero de clubes
for rodadas in dataLeague[str(dataTeams.size)]:
    #Incrementa o contador de rodadas
    numberMatchday += 1
    #Imprime qual rodada eh para facilitar a visualizacao
    print("\nRodada " + str(numberMatchday))
    #Percorre o numero de partidas que ocorrerao, sendo o maior inteiro menor que (numeroClubes / 2)
    for i in range(0, math.floor(dataTeams.size/2)):
        #Imprime a partida conforme o que foi lido na rodada
        print(dataTeams[rodadas[2*i]] + " x " + dataTeams[rodadas[2*i+1]])