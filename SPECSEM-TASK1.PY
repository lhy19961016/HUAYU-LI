def encryption(plaintext, key: int):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i].islower():
            if 96 < int(ord(plaintext[i])) < 123:
                cipher_char = chr(ord(plaintext[i]) + int(key))
                ciphertext.append(cipher_char)
        elif plaintext[i].isupper():
            if 64 < int(ord(plaintext[i])) < 91:
                cipher_char = chr(ord(plaintext[i]) + int(key))
                ciphertext.append(cipher_char)
        elif 0 <= int(ord(plaintext[i])) <= 9:
            cipher_char = chr(ord(plaintext[i]) + int(key))
            ciphertext.append(cipher_char)
        else:
            cipher_char = plaintext[i]
            ciphertext.append(cipher_char)

    return ''.join(ciphertext)


if __name__ == '__main__':
    plaintext = input('Input plaintext:')
    key = input('Input key for encryption:')
    ciphertext = encryption(plaintext, key)
    print(ciphertext)
