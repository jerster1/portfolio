from nacl import utils
from nacl.public import PrivateKey, Box
from nacl.encoding import Base64Encoder
 
aliceKey = PrivateKey.generate()
alicePub = aliceKey.public_key
 
bobKey = PrivateKey.generate()
bobPub = bobKey.public_key
 
# with open('pubkey.txt', mode='w') as f:
#      f.write(bytes.decode(pubKey) + '\n')
 
aliceBox = Box(aliceKey, bobPub)
bobBox = Box(bobKey, alicePub)
 
message = b'This is a secret message!'
 
encryptedMessage = aliceBox.encrypt(message, encoder=Base64Encoder)
 
print("Plaintext: {}".format(message))
print("Encrypted: {}".format(encryptedMessage))
 
print("Bob decrypted it: {}".format(bobBox.decrypt(encryptedMessage, encoder=Base64Encoder)))