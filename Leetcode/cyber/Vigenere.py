from operator import itemgetter
import math

def count_total():
    count = 1
    f = open('example.txt', 'r')
    while (1):
        char = f.read(1)
        if not char:
            break
        else:
            count += 1
    return count



def most_frequent():
    dict = {}
    with open('example.txt', 'r') as file:
        for line in file:
            for word in line.split():
                if ',' in word:
                    word = word[:-1]
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1

    print(sorted(dict.items(), key=itemgetter(1)))

def find_space(target):
    count = 0
    with open('example.txt', 'r') as file:
        for line in file:
            for word in line.split():
                if ',' in word:
                    word = word[:-1]
                if word == target:
                    count += len(word)
                    print(target, count)
                    count = 0
                else:
                    count += len(word)


def main():
    total_size = count_total()
    print(total_size)


    most_frequent()
    find_space('ias')




main()