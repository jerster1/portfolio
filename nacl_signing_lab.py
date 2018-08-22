from nacl.encoding import Base64Encoder
from nacl import signing

signingKey = signing.SigningKey.generate()
verifyKey = signingKey.verify_key.encode(encoder=Base64Encoder)

signiture = signingKey.sign(b'This is a signed message.', encoder=Base64Encoder)

print("Your signed message: {}".format(signiture))
print("Verification key: {}".format(verifyKey))

verifier = signing.VerifyKey(verifyKey, encoder=Base64Encoder)

try:
    verifier.verify(b'This  is a signed message,' , signedMessage, encoder=Base64Encoder):
    print("Message verrified.")
except:
    print("nope")