# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("--- Bem-Vindo ao Gerador de Senhas! ---!")
nr_letters = int(input("Quantas letras voce gotaria que sua senha tivesse?\n"))
nr_symbols = int(input(f"Quantos simbolos?\n"))
nr_numbers = int(input(f"E quantos numeros??\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# senha = ""
# for i in range(nr_letters):
#     senha = senha + letters[random.randint(0, len(letters) - 1)]
#
# for j in range(nr_symbols):
#     senha = senha + symbols[random.randint(0, len(symbols) - 1)]
#
# for k in range(nr_numbers):
#     senha = senha + numbers[random.randint(0, len(numbers) - 1)]
#
# print(f"Nossa sugestão de senha é {senha}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
senha = ""
tot_caracteres = nr_numbers + nr_letters + nr_symbols

for i in range(tot_caracteres):
    sorteio = random.randint(0, 2)
    if sorteio == 0 and nr_numbers > 0:
        senha = senha + random.choice(numbers)
        nr_numbers -= 1
    elif sorteio == 1 and nr_symbols > 0:
        senha = senha + random.choice(symbols)
        nr_symbols -= 1
    elif sorteio == 2 and nr_letters > 0:
        senha = senha + random.choice(letters)
        nr_letters -= 1

print(f"Nossa sugestão de senha é {senha}")
