# 37 positions, index from 0 to 36
import sys

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

isKey = False
isMsg = False


def opt_menu():
    print("\n"
          "0.- Exit program \n"
          "1.- Generate encoding key \n"
          "2.- Insert message \n"
          "3.- Encode message \n"
          "4.- Decode message \n")


def verify_opt(num):
    if num not in [0, 1, 2, 3, 4]:
        return False
    return True


def select_option():
    opt = int(input("Choose an option: "))
    while not verify_opt(opt):
        opt = int(input("Choose an option: "))
    return opt


def exit_program():
    print("Exiting program...")
    sys.exit(0)


def verify_key(num):
    if num.isdigit():
        num = int(num)
        if 5 <= num <= 20:
            return True
    return False


def enc_key():
    array = []
    for i in range(3):
        num = input(f"Write a number for the key({i + 1}): ")
        while not verify_key(num):
            num = input(f"Write a number for the key({i + 1}): ")
        array.append(int(num))
    return array


def generate_alpha(key_num):
    new_alpha = []
    for i in range(key_num, len(alpha) + key_num):
        if i < len(alpha):
            new_alpha.append(alpha[i])
        else:
            index = i % len(alpha)
            new_alpha.append(alpha[index])
    return new_alpha


def verify_msg(string):
    for i in range(len(string)):
        if string[i] not in alpha:
            return False
    return True


def insert_msg():
    msg = input("Insert a message to cipher it: ")
    while not verify_msg(msg):
        msg = input("Insert a message to cipher it: ")
    return msg


def can_encode():
    if isKey and isMsg:
        return True
    return False


def encode_msg(msg, alpha1, alpha2, alpha3):
    encoded_msg = ''
    for i in range(len(msg)):
        alpha_num = i % 3
        index = alpha.index(msg[i])
        if alpha_num == 0:
            encoded_msg += alpha1[index]
        elif alpha_num == 1:
            encoded_msg += alpha2[index]
        else:
            encoded_msg += alpha3[index]
    return encoded_msg


def decode(msg, alpha1, alpha2, alpha3):
    decoded_msg = ''
    for i in range(len(msg)):
        alpha_num = i % 3

        if alpha_num == 0:
            index = alpha1.index(msg[i])
            decoded_msg += alpha[index]
        elif alpha_num == 1:
            index = alpha2.index(msg[i])
            decoded_msg += alpha[index]
        else:
            index = alpha3.index(msg[i])
            decoded_msg += alpha[index]
    return decoded_msg


if __name__ == "__main__":
    key = None
    alpha1 = None
    alpha2 = None
    alpha3 = None
    msg = None
    isKey = False
    isMsg = False
    encoded = False
    while True:
        opt_menu()
        option = select_option()
        if option == 0:
            exit_program()
        if option == 1:
            key = enc_key()
            print(f"The chosen key is {key}")
            alpha1 = generate_alpha(key[0])
            alpha2 = generate_alpha(key[1])
            alpha3 = generate_alpha(key[2])
            print(alpha1)
            print(alpha2)
            print(alpha3)
            isKey = True
        if option == 2:
            msg = insert_msg()
            print(f"Message to cipher: {msg}")
            isMsg = True
        if option == 3:
            if not can_encode():
                print("ERROR! Insert key or message.")
            print(f"The encoded message is: {encode_msg(msg, alpha1, alpha2, alpha3)}")
            encoded = True
        if option == 4:
            if not isKey:
                print("ERROR! Insert key or message.")
            encodedMessage = input(f"Insert message to decode: ")
            decodedMessage = decode(encodedMessage, alpha1, alpha2, alpha3)
            print(decodedMessage)
