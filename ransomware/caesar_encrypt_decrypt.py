def caesar_shift(plain, shift_num):
    cipher = ""
    for c in plain:
        if c.isalpha():
            if c.islower():
                temp_shift = ord(c) + shift_num
                if temp_shift > ord('z'):
                    temp_shift -= 26
                if temp_shift < ord('a'):
                    temp_shift += 26
                final_c = chr(temp_shift)
                cipher += final_c
            elif c.isupper():
                temp_shift = ord(c) + shift_num
                if temp_shift > ord('Z'):
                    temp_shift -= 26
                if temp_shift < ord('A'):
                    temp_shift += 26
                final_c = chr(temp_shift)
                cipher += final_c
        else:
            cipher += c

    return cipher

#print caesar_shift(caesar_shift("New Text Document.txt",len("New Text Document.txt")%26),(len("New Text Document.txt")%26)*-1);
