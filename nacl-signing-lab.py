from nacl.encoding import Base64Encoder
from nacl.signing import SigningKey, VerifyKey

signingKey = SigningKey.generate()
verifyKey = signingKey.verify_key.encode(encoder=Base64Encoder)

signature = signingKey.sign(b'This is a signed message.', encoder=Base64Encoder)

print("Your signed message: {}".format(signature))
print("Verification key: {}".format(verifyKey))

verifier = VerifyKey(verifyKey, encoder=Base64Encoder)

try:
    verifier.verify(b'This is a signed message.', signature, encoder=Base64Encoder)
    print("Message verified.")
except:
    print("Nope.")