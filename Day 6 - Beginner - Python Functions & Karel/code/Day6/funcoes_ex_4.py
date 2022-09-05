"""
Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for negativo e NEUTRO
se for zero/.
"""


def verifica_numero(n):
    if n == 0:
        return "NEUTRO"
    elif n > 0:
        return "P"
    else:
        return "N"


numero = int(input("Informe um numero: "))
print(f"{verifica_numero(numero)}")
