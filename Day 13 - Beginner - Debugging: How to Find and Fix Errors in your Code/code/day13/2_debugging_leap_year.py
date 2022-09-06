# year = input("Which year do you want to check?")  # Errado
year = int(input("Which year do you want to check?"))  # Corrigido

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Problema - no input da variavel year deve ser feito um cast para string para que as comparacoes sejam possiveis.
