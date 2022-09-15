# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
maximo = 90

anos = maximo - int(age)
meses = 12 * anos
semanas = 52 * anos
dias = 365 * anos

print(f"You have {dias} days, {semanas} weeks, and {meses} months left.")

