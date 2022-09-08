from art import logo, vs
from game_data import data
import random

pontuacao = 0


def sorteia():
    """Sorteia os perfis que vao ser comparados no jogo"""
    sorteio = {"1": None, "2": None}
    while sorteio["1"] == sorteio["2"]:
        sorteio = {
            "1": data[random.randint(0, len(data) - 1)],
            "2": data[random.randint(0, len(data) - 1)],
        }
        print(sorteio["1"])
        print(sorteio["2"])
    return sorteio


def compara(perfil_a, perfil_b, resposta):
    """Compara os perfis sorteados entre si e com a resposta do usuario e retorna se o usuario acertou ou nao"""
    global pontuacao
    if perfil_a["follower_count"] > perfil_b["follower_count"]:
        mais_seguidores = "A"
    else:
        mais_seguidores = "B"

    if resposta == mais_seguidores:
        pontuacao += 1
        return True
    else:
        return False


def jogar(sorteio):
    """Funcao principal do jogo, recebe os perfis sorteados"""
    print(f"Comparar A: {sorteio['1']['name']}, um(a) {sorteio['1']['description']}. ")
    print(vs)
    print(f"Contra B: {sorteio['2']['name']}, um(a) {sorteio['2']['description']}.\n ")

    resposta_valida = False
    while not resposta_valida:
        resposta = input("Quem tem mais seguidores? Digite \"A\" ou \"B\"").upper()
        if resposta != "A" and resposta != "B":
            print("RESPOSTA INVALIDA")
        else:
            resposta_valida = True

        acertou = compara(sorteio['1'], sorteio['2'], resposta)
        if acertou:
            print(f"\n\n\nVoce acertou! Sua pontuacao atual é {pontuacao}")
            jogar(sorteia())
        else:
            print(f"\n\n\nDesculpe, voce errou! Sua pontucao final foi {pontuacao}")


print(logo)
jogar(sorteia())
