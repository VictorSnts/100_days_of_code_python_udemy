# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


# 🚨 Don't change the code above 👆

# Write your code below this line 👇

def calcula_pedido(tamanho, pepperoni, chease):
    order = 0

    if tamanho == "S":
        order += 15
    elif tamanho == "M":
        order += 20
    elif tamanho == "L":
        order += 25
    else:
        return "Invalid Size Option"

    if pepperoni == "Y":
        if tamanho == "S":
            order += 2
        else:
            order += 3
    elif pepperoni != "N":
        return "Invalid Pepperoni Option"

    if chease == "Y":
        order += 1
    elif chease != "N":
        return "Invalid Chease Option"

    return f"Your final bill is: ${order}."


print(calcula_pedido(size, add_pepperoni, extra_cheese))
