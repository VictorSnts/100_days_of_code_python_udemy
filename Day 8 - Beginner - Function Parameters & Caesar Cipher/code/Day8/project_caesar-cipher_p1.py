alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#   and print the encrypted text.

def encrypt(text_input, shift_input):
    resultado = ""
    for pos in range(len(text_input)):
        if text_input[pos] != " ":
            index = alphabet.index(text_input[pos])
            try:
                resultado += alphabet[index + shift_input]
            except IndexError:
                nova_posicao = (index + shift_input) - len(alphabet)
                resultado += alphabet[nova_posicao]
        else:
            resultado += " "
    print(f"The encoded text is {resultado}")


# TODO-3: Call the encrypt function and pass in the user inputs.
#   You should be able to test the code and encrypt a message.
encrypt(text, shift)
