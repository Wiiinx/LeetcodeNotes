from operator import itemgetter

def read_text():
    dict = {}
    f = open('CipherText.txt', 'r')
    while 1:
        char = f.read(1)
        if char.isalpha():
            if char.upper() not in dict:
                dict[char.upper()] = 0
            else:
                dict[char.upper()] += 1
        elif not char:
            break

    f.close()
    return sorted(dict.items(), key=itemgetter(1))


def generate_key(dict):
    lst = []
    for i in dict:
        lst.append(i[0])
    lst.reverse()
    return ''.join(lst)


def decryption_file(key, letter_freq):
    print(letter_freq)
    d_file = open('CipherText.txt', 'r')
    d_out = open('DecipherText.txt', 'w')
    while 1:
        char = d_file.read(1)
        if not char:
            break
        if char.isalpha():
            if char.upper() in letter_freq:
                d_out.write(letter_freq[key.index(char.upper())])  # decrypting
            else:
                d_out.write(char)
        else:
            d_out.write(char)
    d_out.close()
    d_file.close()
    return



def sort_key(key, letter_freq):
    dict = {}
    for i in range(len(key)):
        dict[key[i]] = letter_freq[i]
    print(sorted(dict.items(), key=itemgetter(1)))

def main():
    count = read_text()
    key = generate_key(count)
    letter_freq = 'ETAOIHNSRDLUWGCYMFPBKVXQJZ'
    print(key)
    decryption_file(key, letter_freq)
    sort_key(key, letter_freq)


main()