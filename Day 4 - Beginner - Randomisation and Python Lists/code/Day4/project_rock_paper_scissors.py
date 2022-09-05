import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("--- Bem-vindo ao jogo \"Pedra, Papel e Tesoura\" ---")

cod_opcao_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura."))
cod_opcao_computador = random.randint(0, 2)

opcao_usuario = ""
if cod_opcao_usuario == 0:
    opcao_usuario = rock
elif cod_opcao_usuario == 1:
    opcao_usuario = paper
elif cod_opcao_usuario == 2:
    opcao_usuario = scissors
else:
    print("Opção informada é invalida")

opcao_computador = ""
if cod_opcao_computador == 0:
    opcao_computador = rock
elif cod_opcao_computador == 1:
    opcao_computador = paper
elif cod_opcao_computador == 2:
    opcao_computador = scissors

print(f"Voce jogou: \n{opcao_usuario}")
print(f"Computador jogou: \n{opcao_computador}")

if cod_opcao_computador == cod_opcao_usuario:
    print("O jogo terminou com empate.")
elif (cod_opcao_computador == 0 and cod_opcao_usuario == 2) or \
        (cod_opcao_computador == 2 and cod_opcao_usuario == 1) or \
        (cod_opcao_computador == 1 and cod_opcao_usuario == 0):
    print("O computador venceu!")
elif (cod_opcao_usuario == 0 and cod_opcao_computador == 2) or \
     (cod_opcao_usuario == 2 and cod_opcao_computador == 1) or \
     (cod_opcao_usuario == 1 and cod_opcao_computador == 0):
    print("Voce venceu!")


