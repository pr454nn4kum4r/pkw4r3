import random
import string

#Function to create auth_code:
def create_authcode():
    #creating a random string
    auth_string = list(''.join(random.choice(string.letters+string.digits) for x in range(random.randint(25,55))))

    #calculating positions where characters are changed as per authentication algorithm
    auth_string_length = len(auth_string)
    auth_change_pos_1 = auth_string_length/2
    auth_change_pos_2 = auth_string_length/4

    #substituting the character
    rand_int_pos1 = random.randint(2, 19)*5
    rand_int_pos2 = random.randint(4, 25)*3

    auth_string[auth_change_pos_1] = str(rand_int_pos1)[0]
    auth_string[auth_change_pos_1+1] = str(rand_int_pos1)[1]

    auth_string[auth_change_pos_2] = str(rand_int_pos2)[0]
    auth_string[auth_change_pos_2+1] = str(rand_int_pos2)[1]

    auth_code = "".join(auth_string)

    return auth_code
