import art


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def produto(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


operacoes = {
    "+": soma,
    "-": subtracao,
    "*": produto,
    "/": divisao
}


def calcualdora():
    print(art.logo)

    num1 = float(input("Qual o promeiro numero?: "))
    for sinal in operacoes:
        print(sinal)
    continua = True

    while continua:
        sinal_operacao = input("Informe o sinal da operacao: ")
        num2 = float(input("Qual o segundo numero?: "))
        calcula = operacoes[sinal_operacao]
        resultado = calcula(num1, num2)
        print(f"{num1} {sinal_operacao} {num2} = {resultado}")

        if input(f"Voce quer continuar calculando com o resultado ({resultado})? \n"
                 f"Digite 'S' para continuar ou 'N' para iniciar um novo calculo: ") == 'S':
            num1 = resultado
        else:
            continua = False
            calcualdora()


calcualdora()
