# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# ********************************************************
import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}

def encrypt(message, password):
    encrypted_message = ''
    for index, ch in enumerate(message):
        encrypted_ch = alphabet[(ordinal_value[ch] + ordinal_value [password[index % len(password)]]) % len(alphabet)]
        encrypted_message += encrypted_ch
    return encrypted_message

def decrypt(message, password):
    decrypted_message = ''
    for index, ch in enumerate(message):
        decrypted_ch = alphabet[(ordinal_value[ch] - ordinal_value[password[index % len(password)]]) % len(alphabet)]
        decrypted_message += decrypted_ch
    return decrypted_message
