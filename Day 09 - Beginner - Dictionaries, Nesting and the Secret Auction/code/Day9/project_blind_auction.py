import os
import art

print(art.logo)
print(art.bem_vindo)

lances = []
other_bid = True
while other_bid:
    nome = input("Qual o seu nome? ")
    lance = float(input("Qual será o valor de sua licitação? R$"))
    registro = {
        "nome": nome,
        "lance": lance
    }
    lances.append(registro)

    opcao = input("Tem mais algum interessado? Sim ou Nao: ").lower()
    while opcao != "sim" and opcao != "nao":
        print("Opcao invalida. Por favor digite Sim ou Nao.")
        opcao = input("Tem mais algum interessado? Sim ou Nao: ").lower()
    if opcao == "nao":
        other_bid = False
    os.system("clear")

maior_lance = 0
ganhador = {}
for lance in lances:
    if lance["lance"] > maior_lance:
        maior_lance = lance["lance"]
        ganhador = {
            "nome": lance["nome"],
            "lance": lance["lance"]
        }

print(f"O vencedor é {ganhador['nome']} com um lance de R${ganhador['lance']}.")
