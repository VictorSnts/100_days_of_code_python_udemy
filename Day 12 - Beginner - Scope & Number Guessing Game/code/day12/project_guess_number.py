import random
import art


def define_nro_secreto():
    print("Estou pensanso em um numero entre 1 e 100.")
    return random.randint(1, 100)


def define_nro_tentativas():
    dificuldade = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil: '").lower()
    if dificuldade == "facil":
        return 10
    elif dificuldade == "dificil":
        return 5
    else:
        print("Opcao invalida.")
        define_nro_tentativas()


def jogar(nro_secreto, tentativas):
    while tentativas > 0:
        print(f"Voce tem {tentativas} chances restantes para adivinhar o numero secreto.")
        chute = int(input("Faca um tentativa: "))
        if chute > nro_secreto:
            tentativas -= 1
            if tentativas > 0:
                print("Muito alto. Tente chutar um numero mais baixo.")
            else:
                print("VOCE NAO TEM MAIS TENTATIVAS!!")
        elif chute < nro_secreto:
            tentativas -= 1
            if tentativas > 0:
                print("Muito baixo. Tente chutar um numero mais alto.")
            else:
                print("VOCE NAO TEM MAIS TENTATIVAS!!")
        else:
            print("VOCE ACERTOU!!")
            break


def iniciar():
    nro_secreto = define_nro_secreto()
    tentativas = define_nro_tentativas()
    jogar(nro_secreto, tentativas)


print(art.logo)
iniciar()

