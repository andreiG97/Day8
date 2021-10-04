alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text_to_encode, nr_shifts):
    encoded = ''
    text_array = list(text_to_encode)
    for i in range(0, text_array.__len__()):
        if text_array[i] in alphabet:
            current_index = alphabet.index(text_array[i])
            if current_index + nr_shifts < alphabet.__len__():
                text_array[i] = alphabet[current_index + nr_shifts]
            else:
                shifter = current_index + nr_shifts - alphabet.__len__()
                text_array[i] = alphabet[shifter % 26]
        else:
            pass
    encoded = "".join(text_array)
    return encoded


def decrypt(text_to_decode, nr_unshifts):
    decoded = ''
    text_array = list(text_to_decode)
    for i in range(0, text_array.__len__()):
        current_index = alphabet.index(text_array[i])
        text_array[i] = alphabet[current_index - nr_unshifts]

    decoded = "".join(text_array)
    return decoded


def main(direct):

    if direct == 'encrypt':
        return encrypt(text, shift)
    return decrypt(text, shift)


should_run = True
while should_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(main(direction))
    run = input('Yes or no')

    if run.lower() == 'yes':
        should_run = True
    else:
        should_run = False



