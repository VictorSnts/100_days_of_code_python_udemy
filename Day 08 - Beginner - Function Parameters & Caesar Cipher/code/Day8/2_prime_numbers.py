# Write your code below this line ๐
def prime_checker(number):
    divisores = 0
    for num in range(1, number + 1):
        if number % num == 0:
            divisores += 1
    if divisores == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
