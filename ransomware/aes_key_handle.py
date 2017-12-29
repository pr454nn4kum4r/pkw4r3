from Crypto import Random
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode


def aes_gen_key(rsa_pubkey):
    aes_key = Random.new().read(32)
    rsapubkey = RSA.importKey(b64decode(rsa_pubkey))
    encrypt_aes = rsapubkey.encrypt(aes_key,'x')[0]
    aes_file = open("aes_key_file",'w')
    aes_file.write(b64encode(encrypt_aes))
    aes_file.close()
    return aes_key
