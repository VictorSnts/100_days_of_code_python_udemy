"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def imprimir(n):
    retorno = ""
    for i in range(n + 1):
        for j in range(i):
            retorno += f"{j+1} "
        retorno += "\n"
    return retorno


numero = int(input("Informe um numero: "))
print(imprimir(numero))
