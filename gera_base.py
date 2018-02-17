# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:58:46 2018

Idade Juniores: 16-19
Idade Profissionais: 19-33

CUIDADO COM CARACTERES ESPECIAIS...

COMPILAR: python gera_base.py nomeArquivo.txt numeroJogadoresGerados j/OutroCaracter

@author: Douglas Barbino
"""

import numpy as np
import random
import sys

#Eh melhor deixar os vetores de nomes e sobrenomes de maneira global do que passa-los como parametro toda vez

#Importa o dado do arquivo, sendo necessario avisar que o tipo eh str
#data = np.genfromtxt("jap.txt", dtype=str, comments='#', delimiter=' ', usecols=(0,1))
data = np.genfromtxt(sys.argv[1], dtype=str, comments='#', delimiter=' ', usecols=(0,1))
#Extrai os nomes e sobrenomes
name, surname = data[:,[0]], data[:,[1]]
#Remove os repetidos
name = np.unique(name)
surname = np.unique(surname)

#Função onde os jogadores são gerados
def createPlayers(playerPosition, ageRange, randomSide):
    #Lista das posicoes
    positions = {0: "gk", 1: "la", 2: "za", 3: "vo", 4: "ma", 5: "at"}
    #Lista das combinacoes de habilidades que cada posicao pode ter
    characteristics = {0: np.array(["Col/DPe", "Col/SGo", "DPe/Ref", "Ref/SGo", "SGo/DPe"]),
                       1: np.array(["Cru/Mar", "Cru/Vel", "Fin/Pas", "Fin/Vel", "Mar/Fin", "Mar/Pas", "Mar/Vel"]),
                       2: np.array(["Cab/Res", "Des/Cab", "Des/Mar", "Des/Res", "Mar/Vel"]),
                       3: np.array(["Des/Cab", "Des/Fin", "Des/Mar", "Des/Pas", "Des/Vel", "Mar/Fin", "Mar/Pas", "Mar/Vel"]),
                       4: np.array(["Arm/Dri", "Arm/Fin", "Arm/Pas", "Arm/Vel", "Fin/Pas", "Pas/Fin"]),
                       5: np.array(["Cab/Vel", "Dri/Fin", "Fin/Cab", "Fin/Dri", "Fin/Vel", "Vel/Fin"])}
    #Cria o nome do jogador (\t = tab)
    result = name[random.randint(0, name.size-1)] + " " + surname[random.randint(0, surname.size-1)] + "\t"
    #Insere a posicao do jogador com base no que foi sorteado
    result += positions[playerPosition] + "\t\t"
    #Adiciona a idade baseado no tipo de jogador desejado
    if (ageRange == 'j'):
        result += str(random.randint(16, 19))
    else:
        result += str(random.randint(19, 33))
    #Adiciona a habilidade sorteada, com o numero de possibilidades baseadas na posicao dele
    result += "\t" + characteristics[playerPosition][random.randint(0, characteristics[playerPosition].size-1)] + "\t"
    #Verifica se eh necessario sortear um lado
    if ((randomSide == 'd') or (randomSide == 'e')):
        #Nao eh necessario, adiciona o lado passado como parametro
        result += randomSide
    else:
        #Eh necessario sortear um lado
        result += random.choice(['d', 'e'])
    return (result)

#Funcao onde sao criados 11 jogadores de uma vez, como se fosse um time
def createFormation():
    #Variavel para armazenar os jogadores criados dentro da funcao
    playerCreated = ""
    #Vetor com possiveis formacoes
    formations = {0 : [[1, 0, 3, 2, 2, 3], "3-4-3"],
                  1 : [[1, 0, 3, 2, 3, 2], "3-5-2"],
                  2 : [[1, 0, 3, 2, 4, 1], "3-6-1"],
                  3 : [[1, 2, 2, 2, 2, 2], "4-4-2 classic"],
                  4 : [[1, 2, 2, 1, 3, 2], "4-4-2 offensive"],
                  5 : [[1, 2, 2, 3, 1, 2], "4-4-2 defensive"],
                  6 : [[1, 2, 2, 2, 1, 3], "4-3-3 defensive"],
                  7 : [[1, 2, 2, 1, 2, 3], "4-3-3 offensive"],
                  8 : [[1, 2, 2, 2, 3, 1], "4-5-1"],
                  9 : [[1, 2, 3, 1, 2, 2], "5-3-2"],
                  10: [[1, 2, 3, 2, 2, 1], "5-4-1"]}
    #Posicao do jogador nao eh sorteada, eh gerado com base no que a formacao decidir
    drawFormation = random.randint(0, 10)
    #Print da posicao para conferir depois
    print(formations[drawFormation][1])
    for drawPosition in range(0, 6):
        #Caso naquela posicao tenha no minimo 2 jogadores, eh necessario eles estarem na direita e esquerda
        if (formations[drawFormation][0][drawPosition] > 1):
            #Limpa variavel auxiliar
            aux = 1
            #Se forem 4 naquela posicao, esse codigo executa duas vezes
            while (aux < formations[drawFormation][0][drawPosition]):
                #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
                playerCreated += createPlayers(drawPosition, sys.argv[3], 'd') + "\n"
                #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
                playerCreated += createPlayers(drawPosition, sys.argv[3], 'e') + "\n"
                #Incrementa a variavel
                aux += 2
        #Caso o numero de jogadores seja impar, alguem tera que ficar em uma posicao randomica
        if ((formations[drawFormation][0][drawPosition] % 2) == 1):
            #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
            playerCreated += createPlayers(drawPosition, sys.argv[3], 'f') + "\n"
    return playerCreated

#Funcao onde sao criados dois jogadores em uma mesma posicao, um de cada lado
def createDoublePlayersPosition(repetition):
    #Variavel para armazenar os jogadores criados dentro da funcao
    playerCreated = ""
    #Vetor que sera utilizado para sortear quais positions ganharao mais jogadores
    arrayPositions = np.arange(0, 6)
    #Enquanto nao sortearem o numero pedido jogadores, nao sai do loop, ja que a cada jogador eh removida a posicao sorteada
    while (arrayPositions.size > (6 - repetition)):
        #Seleciona aleatoriamente uma posicao ainda disponivel
        drawPosition = random.choice(arrayPositions)
        #A remove do array para que nao seja escolhida novamente, sendo necessario procurar sua localizacao ali
        arrayPositions = np.delete(arrayPositions, np.where(arrayPositions == drawPosition))
        #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
        playerCreated += createPlayers(drawPosition, sys.argv[3], 'd') + "\n"
        #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
        playerCreated += createPlayers(drawPosition, sys.argv[3], 'e') + "\n"
    return playerCreated, arrayPositions

#Funcao onde eh criado um jogador em uma posicao
def createSinglePlayerPosition(repetition, arrayPositions):
    #Variavel para armazenar os jogadores criados dentro da funcao
    playerCreated = ""
    #Variavel para controlar o tamanho original do vetor de posicoes, ja que nao necessariamente o loop terminara quando o vetor estiver vazio
    originalSize = arrayPositions.size
    #Enquanto nao sortearem o numero pedido jogadores, nao sai do loop, ja que a cada jogador eh removida a posicao sorteada
    while (arrayPositions.size > (originalSize - repetition)):
        #Seleciona aleatoriamente uma posicao ainda disponivel
        drawPosition = random.choice(arrayPositions)
        #A remove do array para que nao seja escolhida novamente, sendo necessario procurar sua localizacao ali
        arrayPositions = np.delete(arrayPositions, np.where(arrayPositions == drawPosition))
        #Chama a funcao para gerar os atletas, passando como parametros a posicao dele e a faixa de idade
        playerCreated += createPlayers(drawPosition, sys.argv[3], 'f') + "\n"
    return playerCreated

#Existem tres funcoes para montar os jogadores:
# - Para montar um time com 11 jogadores
# - Para entre 7 e 10 jogadores soltos, pois algumas posicoes ficarao com dois atletas, um de cada lado
# - De 6 para baixo
#A prioridade eh montar times, montando apos isso os jogadores que ficam na mesma posicao e, por ultimo, o que sobrar

#Variavel onde sera colocado os jogadores criados
filePlayers = ""
#Armazena o numero de jogadores desejados conforme parametro passado pelo usuario
numberPlayers = int(sys.argv[2])
#Executa a funcao de criar times quantas vezes for possivel por meio da divisao inteira
for numberTeams in range (0, (numberPlayers // 11)):
    filePlayers += createFormation()
#Com todos os times possiveis ja feitos, numberPlayers fica com o resto do valor original dividido por 11, representando quantos jogadores ainda precisam ser criados
numberPlayers = numberPlayers % 11
#Caso numberPlayers seja maior que 6, eh necessario aplicar o processo de criar mais de um jogador em uma posicao
if (numberPlayers > 6):
    #Variavel auxiliar para receber os jogadores
    newPlayers = ""
    #Executa essa funcao numberPlayers-6 vezes
    newPlayers, arrayPositions = createDoublePlayersPosition(numberPlayers-6)
    #Insere os jogadores criados na lista
    filePlayers += newPlayers
    #Cria os jogadores que ainda estao faltando
    filePlayers += createSinglePlayerPosition(arrayPositions.size, arrayPositions)
#Como na alcancava 6 jogadores, cria o numero que existe mesmo
else:
    #Vetor que sera utilizado para sortear quais positions ganharao mais jogadores
    arrayPositions = np.arange(0, 6)
    #Cria os jogadores que ainda estao faltando
    filePlayers += createSinglePlayerPosition(numberPlayers, arrayPositions)
        
#Escreve os jogadores criados em um arquivo txt, ja em um formato pronto para exportar ao Excel
with open('jogadores.txt', 'w') as f:
	f.write(filePlayers)