import Forca
import Adivinhacao

def escolher_jogo():

    verificador = True
    while (verificador):

        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca \n(2) Adivinhação")
        jogo = int(input("Qual jogo? "))

        if(jogo == 1):
            print("Jogando forca")
            Forca.jogar()
        elif(jogo == 2):
            print("Jogando adivinhação")
            Adivinhacao.jogar()

        verificador = True if ((jogo < 1) or (jogo > 3)) else False

if(__name__ == "__main__"):
    escolher_jogo()
