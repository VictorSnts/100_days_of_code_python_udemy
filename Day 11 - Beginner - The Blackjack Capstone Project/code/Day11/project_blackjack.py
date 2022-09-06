# ############## Blackjack Project #####################

# ############## Our Blackjack House Rules #####################
# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The the Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.
# ############## ##################### #####################
import random
import art

print(art.logo)
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
partidas = 0


def iniciar_partida():
    """Funcao que inicia uma nova partida"""
    global partidas
    if partidas == 0:
        opcao = input("Voce quer jogar Blackjack? Digite 'S' ou 'N' ").upper()
        print(5 * "\n")
    else:
        opcao = input("Voce quer continuar jogando Blackjack? Digite 'S' ou 'N' ").upper()
        print(5 * "\n")

    if opcao == "S":
        partidas += 1
        jogar()
    elif opcao == "N":
        print("Finalizando o jogo... Obrigado")
        return
    else:
        print("Opcao Invalida.")
        iniciar_partida()


def sortear_cartas():
    """Funcao que sorteia as cartas para os jogadores"""
    global cartas
    maos = {
        "Usuario": [random.choice(cartas), random.choice(cartas)],
        "Computador": [random.choice(cartas), random.choice(cartas)]
    }
    return maos


def outra_carta(cartas_sorteio):
    """Funcao que sorteia outra carta para o jogador"""
    nova_carta = random.choice(cartas)
    cartas_sorteio["Usuario"].append(nova_carta)
    if nova_carta == 11:
        if is_21(cartas_sorteio["Usuario"]) == ">":
            cartas_sorteio["Usuario"][-1] = 1
    return cartas_sorteio


def finaliza_partida(cartas_sorteio):
    """Funcao que finaliza a partida mostrando quem ganhou"""
    pontos_usuario = 0
    for carta in cartas_sorteio["Usuario"]:
        pontos_usuario += carta

    pontos_computador = 0
    for carta in cartas_sorteio["Computador"]:
        pontos_computador += carta

    print(f"\n\nSuas cartas: {cartas_sorteio['Usuario']} = {pontos_usuario}\n"
          f"Cartas do Computador: {cartas_sorteio['Computador']} = {pontos_computador}\n\n")

    if pontos_usuario > 21:
        return "\n\nO computador ganhou!"
    elif pontos_computador > 21:
        return "\n\nVoce ganhou!"
    elif pontos_usuario > pontos_computador:
        return "\n\nVoce ganhou!"
    elif pontos_computador > pontos_usuario:
        return "\n\nO computador ganhou!"
    else:
        return "\n\nO jogo terminou empatado!"


def is_21(cartas_usuario):
    pontos_usuario = 0
    for carta in cartas_usuario:
        pontos_usuario += carta
    if pontos_usuario == 21:
        return "="
    elif pontos_usuario > 21:
        return ">"
    else:
        return "<"


def jogar():
    """Funcao que comeca o jogo"""
    sorteio = sortear_cartas()
    jogando = True
    while jogando:
        print(f"Suas cartas: {sorteio['Usuario']}\n"
              f"Primeira carta do Computador: {sorteio['Computador'][1]}\n\n")
        if (is_21(sorteio["Usuario"]) == "=") or (is_21(sorteio["Usuario"]) == ">"):
            print(finaliza_partida(sorteio))
            break
        outra = input("Digite 'S' para pegar outra carta ou 'n' para continuar: ").upper()
        if outra == "S":
            sorteio = outra_carta(sorteio)
            if (is_21(sorteio["Usuario"]) == "=") or (is_21(sorteio["Usuario"]) == ">"):
                print(finaliza_partida(sorteio))
                break
            print(3 * "\n")
        elif outra != "N":
            print("Opcao Invalida.")
            print(3 * "\n")

        else:
            print(finaliza_partida(sorteio))
            break

    iniciar_partida()


iniciar_partida()
