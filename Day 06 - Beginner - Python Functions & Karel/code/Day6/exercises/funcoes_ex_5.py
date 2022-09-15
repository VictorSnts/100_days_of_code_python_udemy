"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do
imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""


def soma_imposto(custo, taxa_imposto):
    imposto = custo * (taxa_imposto / 100)
    return custo + imposto


custo_produto = float(input("Informe o custo de um produto: "))
taxa = float(input("Informe a taxa de imposto: "))
print(soma_imposto(custo_produto, taxa))

