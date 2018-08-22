import parser
import os
from cryptography.fernet import Fernet



key = Fernet.generate_key()
 
f = Fernet(key)
with open("key.txt", "a") as myFile:
    myFile.write(str(f))
    myFile.close()

