from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from modules.constants import *
import base64

def ValidCredentials(currentPubKey, signature):
    signature = base64.b64decode(signature);
    # print (currentPubKey)
    # print(signature)

    rsaKey = RSA.importKey(currentPubKey)
    h = SHA.new()
    h.update(KEY.encode("utf-8"))
    verifier = PKCS1_PSS.new(rsaKey)

    return verifier.verify(h, signature)
