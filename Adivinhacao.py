import random

def jogar():
    apresentacao()
    nivel = dificuldade()
    chances = tentativas(nivel)

    pontos = 100

    numero_aleatorio = numeroAleatorio()

    acertou = False
    for rodada in range(1,chances+1):
        print(f"Tentativa {rodada} de {chances}")
        chute = int(input("DIGITE UM NUMERO: "))
        if (chute < 1) or (chute >100):
            print("DIGITE UM NUMERO ENTRE 1 E 100!")
        elif chute < numero_aleatorio:
            print("O numero secreto é MAIOR!")
            pontos = pontos - abs(numero_aleatorio - chute)
        elif chute > numero_aleatorio:
            print("O numero secreto é MENOR!")
            pontos = pontos - abs(numero_aleatorio - chute)
        else:
            acertou = True
            break

    if (acertou): print(f"WINNER!! \n Score: {pontos}/100")
    else: print(f"YOU LOSE!\n Numero Secreto: {numero_aleatorio}")



#################FUNÇÔES############################

def numeroAleatorio():
    return random.randrange(1,101)  #gera um numero aleatório de 1 até 100.

def apresentacao():
    print("############################################")
    print("#############JOGO DE ADIVINHAÇÃO############")
    print("############################################")
    print("#DESCULBRA O NUMERO ESCONDIDO ENTRE 1 E 100#")
    print("############################################")

def dificuldade():
    verificador = True
    while(verificador):
        print("--------------------------------------------")
        print("(1) - FÁCIL")
        print("(2) - MÉDIO")
        print("(3) - DIFÍCIL")
        nivel = int(input("SELECIONE A DIFICULDADE: "))
        verificador = True if ((nivel < 1) or (nivel > 3)) else False
    return nivel

def tentativas(nivel):
    if nivel == 1:  #Fácil
        chances = 10
    elif nivel == 2: #Médio
        chances = 5
    elif nivel == 3: #Dificil
        chances = 3
    return chances


if __name__ == '__main__':
    jogar()
