# pkw4r3
This is an attempt to create a POC of Crypto Ransomware. Please use this for only educational purposes only.

Testing POC:

Requirements:
1) Apache+PHP Stack for C&C Server
I have developed everything on Kali Machine as attacker machine. I didnt test this on Windows Machine.

2) Windows Machine to act as Victim Machine
Please avoid legacy machines that are below Windows XP. I am using WMI wrappers which might not work in those machines

3)Python, Microsoft C++ 9.0, Pycrypto installed on Windows Machine
I understand that malware should not be dependent with third party requirements other than built-in features of the victim.
Considering, this is just a POC not a malware and for easy readability, I have used Python and above packages.


Installation:
*Copy "C&C" folder in Apache Web Server.
*Copy "Ransomware" folder to Windows Machine

Execution:
*First run generate_dga.py and choose on of the domains and add it to Windows /etc/hosts linking to your attacking machine
*Start Apache Web Server
*Execute ransomware.py
*Your files in Desktop with given extensions are encrypted 

Decryption:
* Browse summary.txt in victim_manager in Apache Web Server to see the folder related to the victim
* Copy the .pem suffixed file to Victim Windows Machine
* Run decrypt.py with .pem file as argument
* Encrypted files are decrypted





