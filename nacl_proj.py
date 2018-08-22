from nacl.encoding import Base64Encoder
from nacl import signing
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-g', '--generate', action='store_true', help='Generate both priv and pub key')
group.add_argument('-e', '--encrypt', metavar='PLAINTEXT', help='The plaintext to encrypt.')
group.add_argument('-d', '--decrypt', metavar='CIPHERTEXT', help='The ciphertext to decrypt.')

args = parser.parse_args()

if args.generate:
    signingKey = signingKey.Privitekey()
    print("Generated both keys: {}".format(signingKey))
else:
        pass



if args.encrypt == "":
    x = input("what would you like to encrypt?: ")
    y = signingKey.sign(x, encoder=Base64Encoder)
    print("Heres your encrypted message: {}".format(y, encoder=Base64Encoder))
if
    a = args.encrypt
    b = signingKey.sign(a, encoder=Base64Encoder)
    print("Heres your encrypted message: {}".format(b, encoder=Base64Encoder))
else:
    print("yah idk wtf happend")









# verifyKey = signingKey.verify_key.encode(encoder=Base64Encoder)

# signiture = signingKey.sign(b'This is a signed message.', encoder=Base64Encoder)

# print("Your signed message: {}".format(signiture))
# print("Verification key: {}".format(verifyKey))

# verifier = signing.VerifyKey(verifyKey, encoder=Base64Encoder)

# try:
#     verifier.verify(b'This  is a signed message,' , signedMessage, encoder=Base64Encoder):
#     print("Message verrified.")
# except:
#     print("nope")