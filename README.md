# gera-base
Projeto em Python para gerar jogadores do jogo Brasfoot, podendo ser adaptado para outros jogos do tipo manager

Bibliotecas utilizadas:
* numpy
* pandas
* random
* sys

Para executar, utilize um terminal para ir até a pasta do projeto e digite o seguinte comando: 

python gera_base.py nomeArquivo.txt numeroJogadoresGerados j/OutroCaracter

Sendo esses os parâmetros:
* nomeArquivo.txt - Arquivo onde estão os nomes que serão utilizados para coletas os nomes e sobrenomes. Ex: jap.txt
* numeroJogadoresGerados - Digite o número de jogadores que deseja gerar. Ex: 11
* name/j/OutroCaracter - Digite **name** para que sejam gerados apenas os nomes dos jogadores, **j** para que o atleta seja criado com idade de um atleta das categorias de base (entre 16 e 19 anos) ou qualquer outra letra para que ele venha com uma idade de jogador profissional (entre 19 e 33 anos)

# gera-tabelas
Projeto em Python para gerar tabelas de campeonatos, em geral no formato de todos contra todos

Bibliotecas utilizadas:
* json
* math
* numpy
* pandas
* sys

Para executar, utilize um terminal para ir até a pasta do projeto e digite o seguinte comando: 

python gera_tabelas.py nomeArquivo.txt numeroTurnos  y/a/outroValor tipoTabela

Sendo esses os parâmetros:
* nomeArquivo.txt - Arquivo onde estão os clubes do torneio cuja tabela será gerada. Ex: myleaguetg.txt
* numeroTurnos - Digite o número de turnos que o torneio terá. Ex: 2
* y/a/outroValor - Digite **y** para que a lista de clubes seja dividida do meio e cada metade tenha sua ordem embaralhada, visando facilitar quando há o interesse de que determinados clubes tenham um jogo a mais em casa no último turno do torneio, **a** para que os clubes sejam embaralhados juntos ou qualquer outra letra para que a ordem que os clubes estão no arquivo seja respeitada


Muito obrigado por observarem meu código!