from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import modules.constants

def ValidCredentials(currentPubKey, signature):
    rsaKey = RSA.importKey(currentPubKey)
    h = SHA.new()
    h.update(constants.KEY.encode("utf-8"))
    verifier = PKCS1_PSS.new(rsaKey)

    return verifier.verify(h, signature)
