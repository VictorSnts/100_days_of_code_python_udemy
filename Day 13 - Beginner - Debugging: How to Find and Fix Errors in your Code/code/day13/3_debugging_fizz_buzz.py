for number in range(1, 101):
    # if number % 3 == 0 or number % 5 == 0:  # Errado
    if number % 3 == 0 and number % 5 == 0:  # Corrigido
        print("FizzBuzz")
    # if number % 3 == 0: # Errado
    elif number % 3 == 0: # Corrigido
        print("Fizz")
    # if number % 5 == 0: # Errado
    elif number % 5 == 0: # Corrigido
        print("Buzz")
    else:
        # print([number]) # Errado
        print(number)  # Corrigido

# Problema 1 - no bloco if deve se satisfazer as duas condicoes, entao devemos trocar or por and
# Problema 2 - na segunda e na terceira comparacao devemos usar elif
# Problema 3 = no bloco else, no comando print nao é necessario que a variavel number esteja entre []

