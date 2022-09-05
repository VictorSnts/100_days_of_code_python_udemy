# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def count_occurrence(nome1, nome2, teste):
    nome = (nome1 + nome2).upper()
    teste = teste.upper()
    counter = 0

    for i in range(len(nome)):
        if nome[i] in teste:
            counter += 1

    return counter


count_true = count_occurrence(name1, name2, "True")
count_love = count_occurrence(name1, name2, "Love")
score = int(str(count_true) + str(count_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
