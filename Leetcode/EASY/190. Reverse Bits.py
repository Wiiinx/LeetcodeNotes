import math
def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n>>i) & 1

        res = res | bit << (31 - i)
    return res



def main():
    print(reverseBits(1000001111010011100))


main()
