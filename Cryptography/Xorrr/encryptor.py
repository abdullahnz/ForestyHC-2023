#!/usr/bin/python3

FLAG = b"ForestyCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
KEY = b"??????????"

assert len(KEY) == 10

def encrypt(plaintext : bytes, key : bytes) -> bytes:
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append(plaintext[i] ^ key[i % len(key)])
    return bytes(ciphertext).hex()

encrypted_flag = encrypt(FLAG, KEY) 
print(encrypted_flag)