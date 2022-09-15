import math
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("--- Bem-Vindo a Calculadora de Gojetas! ---")

valor_conta = float(input("Qual o total da nossa conta? R$"))
percent_gorjeta = int(input("Quanto vamos dar de gorjeta? 10, 12, ou 15? "))
pessoas = int(input("Em quantas pessoas vamos dividir? "))

percent_gorjeta = percent_gorjeta / 100
gorjeta = valor_conta * percent_gorjeta
total = valor_conta + gorjeta

total_por_pessoa = (total / pessoas)
print(f"Cada um deve pagar R${round(total_por_pessoa, 2)}")

