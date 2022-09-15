import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']


def input_validate(char):
    if char in numbers or char in symbols:
        return False
    elif char == " ":
        return False
    else:
        return True


def caesar(text_input, shift_input, direction_input):
    resultado = ""
    for pos in range(len(text_input)):
        if input_validate(text_input[pos]):
            index = alphabet.index(text_input[pos])
            if shift_input > len(alphabet):
                shift_input = shift_input % len(alphabet)
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
            resultado += text_input[pos]
    print(f"The {direction_input}d text is {resultado}")
    pass


execute = True
while execute:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text_input=text, shift_input=shift, direction_input=direction)

    rerun = input("\n\nYou want to restart the cipher program? Yes or No? ").lower()
    if rerun == "no":
        execute = False

