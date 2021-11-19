import random
import json
import time

pontos = 0
qtdePerguntas = 10
gabaritoRodada = []
perguntas = json.load(open('./perguntas.json'))

def apresentacao(): #Introdução
    print("Bem vindo ao Quiz do Grupo Cassino do Gabigol!")
    jogador = input("Por favor, insira seu nome: ").title()
    print('Caso deseje ler o tutorial, digite "Tutorial". Para seguir para o quiz, digite qualquer outra coisa.')
    
    if input().title() == "Tutorial":
        tutorial()
        
    modo = int(input("Insira 1 para jogar no modo clássico ou 2 para jogar no modo cassino: "))
    return jogador, modo

def tutorial(): #Mostra o tutorial
    print(f'\nO modo classico e o modo cassino sao muito similares, o jogador ganha pontos por acertar as questoes respondidas, porem, no modo cassino, as questoes que o \njogador errou tiram seus pontos. Se um jogador acertar uma questao de 8 pontos e errar uma de 6 pontos, por exemplo, ele ficara com 2 pontos.\n')
    time.sleep(6)

def recebeResposta(): #Recebe a resposta para cada pergunta do jogador
    resposta = input()
    return resposta

def checaCheat(jogador, resposta): #Verifica se o cheat está ativo
    if jogador == "Fabiana":
        print(f'Resposta Correta: {resposta}')

def loopPergunta(qtde: int, nome: str, modo: str): #qtde = Quantidade de questões
    perguntasDadas = [0, 0, 0] #Contador de questões fáceis, médias e difíceis
    maxPerguntas = [3, 5, 2] #Máximo de perguntas de cada dificuldade
    count = 1

    while True:

        index_pergunta = random.choice(list(perguntas.keys()))
        pergunta = perguntas[index_pergunta]

        if (pergunta["dificuldade"] == "F" and perguntasDadas[0] < maxPerguntas[0] #Verifica se já chegou no limite de questões da dificuldade especificada
        or pergunta["dificuldade"] == "M" and perguntasDadas[1] < maxPerguntas[1]
        or pergunta["dificuldade"] == "D" and perguntasDadas[2] < maxPerguntas[2]):
            gabaritoRodada.append(pergunta["gabarito"])
            print(f'{count}) {pergunta["titulo"]}') #Mostra o enunciado da pergunta
            print(pergunta["alternativas"]) #Mostra as alternativas possíveis
            checaCheat(nome, pergunta["gabarito"]) #Verifica se o cheat code está ativo
            somaPontos(modo, pergunta["gabarito"], pergunta["pesoNormal"], pergunta["pesoCassino"])
            time.sleep(1.5)

            if pergunta["dificuldade"] == "F": #Acrescenta como pergunta dada de acordo com a dificuldade
                perguntasDadas[0] += 1

            elif pergunta["dificuldade"] == "M":
                perguntasDadas[1] += 1

            elif pergunta["dificuldade"] == "D":
                perguntasDadas[2] += 1

            if(len(list(perguntas.keys())) >= 1):
                del perguntas[index_pergunta] #Remove o item do dicionário para não ter perguntas repetidas no quiz

            count += 1

        if perguntasDadas == maxPerguntas:
            break

def somaPontos(gamemode, resposta, pesoNormal, pesoCassino):
    global pontos
    if gamemode == 1: #If para definir como ocorrerá a pontuação
        if recebeResposta().upper() == resposta: #If para adicionar pontos à pontuação do jogador caso acertar a resposta (modo clássico)                                   
            pontos += pesoNormal

    elif gamemode == 2:
        if recebeResposta().upper() == resposta: #If para adicionar pontos à pontuação do jogador caso acertar a resposta ou remover pontos caso ele errar (modo cassino)
            pontos += pesoCassino

        else:
            pontos -= pesoCassino

def mediaClassico(): #Calcula a média de acordo com o modo clássico
    global pontos
    resultado = pontos / 5.8
    return resultado

def mediaCassino(): #Calcula a média de acordo com o modo cassino
    global pontos
    resultado = pontos / 7.8
    return resultado

def mostraResultado(gamemode): #Mostra o resultado final para o jogador de acordo com o modo de jogo
    if gamemode == 1:
        resp = mediaClassico()

    elif gamemode == 2: 
        resp = mediaCassino()

    if resp < 7:
        print(f"Podia ser melhor :/, voce tirou {resp:.2f} e aqui esta sua recompensa: \nhttps://www.youtube.com/watch?v=0-sQrPu26zc")
        
    else:
        print(f"Parabens, voce tirou {resp:.2f} (: e aqui esta sua recompensa: \nhttps://www.youtube.com/watch?v=aYRBR_NxyJs")
        
    print("Aguarde 5 segundos para ver o gabarito...")

def gabarito(respostasRodada): #Mostra o gabarito para o jogador de acordo com as respostas obtidas até o momento
    time.sleep(5) #Tempo de espera para que o jogador possa ler sua nota
    print("Gabarito:")
    nQuestao = 1
    
    for resposta in respostasRodada:
        print(f'{nQuestao}: {resposta}')
        nQuestao += 1

def main():
    nome_jogador, modo_jogo = apresentacao()
    
    loopPergunta(qtdePerguntas, nome_jogador, modo_jogo)

    mostraResultado(modo_jogo)
    
    gabarito(gabaritoRodada)

if __name__ == '__main__':
    main()