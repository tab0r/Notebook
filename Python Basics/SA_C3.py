def cipher(text, cipher_alphabet, option='encipher'):
    #assumes cipher alphabet dictionary is plaintext:values
    oldText = list(text)
    newText = ''

    if option != 'encipher': #make it a tiny bit faster
        decipher_alphabet = dict(zip(cipher_alphabet.values(), cipher_alphabet.keys()))

    print option

    for letter in oldText:
        if letter == ' ':
            newLetter = letter
        else:
            if option == 'decipher':
                newLetter = decipher_alphabet.get(letter)
            else:
                newLetter = cipher_alphabet.get(letter)
        newText += str(newLetter)

    return newText

d = dict(zip('abcdefghijklmnopqrstuvwxyz','phqgiumeaylnofdxjkrcvstzwb'))
ciphertext = cipher('defend the east wall of the castle', d)

print ciphertext
print "Deciphering...\n"

#d2 = dict(zip('phqgiumeaylnofdxjkrcvstzwb','abcdefghijklmnopqrstuvwxyz'))

print cipher(ciphertext, d, option='decipher')
