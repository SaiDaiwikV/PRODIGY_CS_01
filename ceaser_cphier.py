def encrypt_text(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char == " ":
            ciphertext += " "
        elif char.isupper():
            ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
    return ciphertext

plaintext = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))
print("---------------------------------------------")
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(shift))
print("Cipher Text is : " + encrypt_text(plaintext, shift))
