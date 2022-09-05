alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(text_input, shift_input, direction_input):
    resultado = ""
    for pos in range(len(text_input)):
        if text_input[pos] != " ":
            index = alphabet.index(text_input[pos])
            if direction_input == "encode":
                try:
                    resultado += alphabet[index + shift_input]
                except IndexError:
                    nova_posicao = (index + shift_input) - len(alphabet)
                    resultado += alphabet[nova_posicao]
            elif direction == "decode":
                try:
                    resultado += alphabet[index - shift_input]
                except IndexError:
                    nova_posicao = (index - shift_input) + len(alphabet)
                    resultado += alphabet[nova_posicao]
            else:
                print("Invalid Option!")
                return
        else:
            resultado += " "
    print(f"The {direction_input}d text is {resultado}")
    pass

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text_input=text, shift_input=shift, direction_input=direction)


