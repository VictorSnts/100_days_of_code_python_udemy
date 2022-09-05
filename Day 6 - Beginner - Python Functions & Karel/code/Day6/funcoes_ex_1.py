"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def imprimir(n):
    retorno = ""
    for i in range(n + 1):
        for j in range(i):
            retorno += f"{i} "
        retorno += "\n"
    return retorno


numero = int(input("Informe um numero: "))
print(imprimir(numero))
