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

#Embaralha os times caso desejado, permitindo que se divida no meio para que os times da metade
#superior da lista continuem tendo um jogo a mais em casa em campeonatos com numero de times par
#if (sys.argv[2] = 'y'):
#Realiza a divisao, com shuffleTeams sendo apenas uma copia do vetor, entao as mudancas aqui afetam o vetor dataTeams
breakTeams = np.array_split(dataTeams, 2)
#Embaralha cada metade
for teams in breakTeams:
    np.random.shuffle(teams)
#Embaralha o vetor como um todo
#elif (sys.argv[2] = 'a'):
#    np.random.shuffle(dataTeams)

#Contador de rodadas
numberMatchday = 0
#Numero de turnos
numberTurns = 4
#Repete a geracao de rodadas conforme o numero de turnos
for turn in range(0, numberTurns):
    #Leitura das rodadas do torneio com aquele numero de clubes
    for rodadas in dataLeague[str(dataTeams.size)]:
        #Incrementa o contador de rodadas
        numberMatchday += 1
        #Imprime qual rodada eh para facilitar a visualizacao
        print("\nRodada " + str(numberMatchday))
        #Percorre o numero de partidas que ocorrerao, sendo o maior inteiro menor que (numeroClubes / 2)
        for i in range(0, math.floor(dataTeams.size/2)):
            #Inverte a ordem dos times caso o numero de turnos restantes seja par, 
            #permitindo que no ultimo turno os clubes da metade superior tenham um jogo a mais em casa 
            if (((numberTurns - turn) % 2) == 0):
                #Imprime a partida conforme o que foi lido na rodada
                print(dataTeams[rodadas[2*i+1]] + "\tx\t" + dataTeams[rodadas[2*i]])
            else:
                #Imprime a partida conforme o que foi lido na rodada
                print(dataTeams[rodadas[2*i]] + "\tx\t" + dataTeams[rodadas[2*i+1]])