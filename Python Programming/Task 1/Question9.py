#Custom encryption-decryption system

def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isupper():
            encrypted += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted
message = input("Enter your message: ")
key = int(input("Enter encryption key (number): "))

encrypted_msg = encrypt(message, key)
print("Encrypted:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, key)
print("Decrypted:", decrypted_msg)

