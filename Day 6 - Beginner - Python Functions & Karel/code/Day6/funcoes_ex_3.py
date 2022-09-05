"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def soma(a, b, c):
    return a + b + c


n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

print(f"A soma é {soma(n1, n2, n3)}")
