import random


def generate_key():
    letter = []
    for i in range(65, 91):
        letter.append(chr(i))
    random.shuffle(letter)
    key = ''.join(letter)
    return key


def get_key(key_lst):
    print("--------SELECT KEYS--------")
    key_option = int(input("1: retrieve my key\n2: type by my own\nEnter your choice: "))
    if key_option == 1:
        if len(key_lst) == 0:
            return 0
        print("\nSelect your keys: ")
        for i, m in enumerate(key_lst):
            print('{0}: {1}'.format(i, m))
        key_idx = int(input("Enter your choice: "))
        return key_lst[key_idx]
    elif key_option == 2:
        key = input("Type here:")
        return key


def encryption_text(new_key):
    key = list(new_key)
    en_text = input("\nPlease type the text here:\n")
    output_text = []
    for i in en_text:
        if i.upper() in key:
            output_text.append(key[ord(i.upper()) - 65])
        else:
            output_text.append(i)
    print("\nEncrypting............\n")
    print("This is your Encrypted text:")
    print(''.join(output_text))
    print("\nThis is your key: ", new_key)
    return


def encryption_file(new_key):
    key = list(new_key)
    file_name = input("\nEnter the file name: ")
    f = open(file_name, "r")
    new_file = input("Enter the output file name: ")
    output = open(new_file, 'x')
    while 1:
        char = f.read(1)
        if not char:
            break
        if char.upper() in key:
            output.write(key[ord(char.upper()) - 65])  # encrypting
        else:
            output.write(char)
    output.close()
    f.close()
    print("\nEncrypting............DONE!")
    print("This is your key: ", new_key)
    return


def decryption_file(d_key):
    key = list(d_key)
    file_name = input("\nEnter the file name:")
    d_file = open(file_name, "r")
    new_file = input("Enter the output file name: ")
    d_out = open(new_file, 'x')
    while 1:
        char = d_file.read(1)
        if not char:
            break
        if char.upper() in key:
            d_out.write(chr(key.index(char.upper()) + 65))   # decrypting
        else:
            d_out.write(char)
    d_out.close()
    d_file.close()
    print("\nDecrypting............DONE!")
    return


def decryption_text(d_key):
    key = list(d_key)
    de_text = input("\nPlease type the text here:\n")
    output_text = []
    for i in de_text:
        if i.upper() in key:
            output_text.append(chr(key.index(i.upper()) + 65)) # decrypting
        else:
            output_text.append(i)
    print("\nDecrypting............DONE!\n")
    print("This is your Decrypted text:")
    print(''.join(output_text))
    return


def main_window(key_lst):
    print("\n--------Main Window--------")
    choice = int(input("1: Encryption\n2: Decryption \n3: Exit\nEnter your choice: "))

    # Encryption
    if choice == 1:
        print("\n--------Encryption--------")
        en_choice = int(input("1: Encrypt from a txt. file\n2: Type below\n3: Back to main window\nEnter your choice: "))
        if en_choice == 1:  # encrypt from a txt file
            new_key = generate_key()
            key_lst.append(new_key)
            encryption_file(new_key)

        elif en_choice == 2:
            new_key = generate_key()
            key_lst.append(new_key)
            encryption_text(new_key)
        elif en_choice == 3:
            print()
            main_window(key_lst)
        else:
            print()
            main_window(key_lst)

    # Decryption
    elif choice == 2:
        print("\n--------Decryption--------")
        de_choice = int(input("1: Decrypt from a txt. file\n2: Type below\n3: Back to main window\nEnter your choice: "))
        if de_choice == 1:  # decrypt from a txt file
            d_key = get_key(key_lst)  # get keys
            if d_key == 0:
                print("\nThere's no key in the list...")
            else:
                decryption_file(d_key)
        elif de_choice == 2:
            d_key = get_key(key_lst)  # get keys
            if d_key == 0:
                print("\nThere's no key in the list...")
            else:
                decryption_text(d_key)
        elif de_choice == 3:
            print()
            main_window(key_lst)
        else:
            print()
            main_window(key_lst)
    elif choice == 3:
        return
    main_window(key_lst)


def main():
    key_lst = []
    main_window(key_lst)


main()
