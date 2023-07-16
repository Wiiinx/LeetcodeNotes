
def decryption_text(d_key):
    key = list(d_key)
    de_text = input("\nPlease type the text here:\n")
    output_text = []
    for i in de_text:
        if i.upper() in key:
            output_text.append(chr(key.index(i.upper()) + 65))
        else:
            output_text.append(i)
    print("\nDecrypting............\n")
    print("This is your Decrypted text:")
    print(''.join(output_text))
    return

def main():
    d_key = input("Type_key: ")
    decryption_text(d_key)

main()
