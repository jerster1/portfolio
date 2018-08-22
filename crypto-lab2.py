import sys
import os
from cryptography.fernet import Fernet
 
# Accept input using Parser
# three functions: generate a key, encrypt, decrypt
# keygen: save to a file called my.key
# encrypter: 2 inputs -- plaintext & the key file
# decrypter: 2 inputs -- ciphertext & the key file
# handle the errors! InvalidToken && InvalidSignature
# optional: let the user specify to generate the key AND encrypt at the same time
# EXAMPLE: my-code.py --genkey --encrypt "Blah"
# EXAMPLE: my-code.py --encrypt "Blah" /path/to/my.key
 
key = Fernet.generate_key()
 
f = Fernet(key)
print("Your key: {}".format(key))
cipherText = f.encrypt(b'Hello, world!')
print("Your ciphertext: {}".format(cipherText))
 
plainText = f.decrypt(cipherText)
print("Your plaintext: {}".format(plainText))