def isPalindrome1(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]

# a = '1234'
# a[::-1]   starts from the end towards the first taking each element
# '4321'

def isPalindrome2(x):
    if x < 0:
        return False
    inputNum = x
    newNum = 0
    while x > 0:
        newNum = newNum * 10 + x % 10
        x = x//10
    return newNum == inputNum


def main():
    x1 = 121
    x2 = -121
    print(isPalindrome1(x2))
    print(isPalindrome1(x1))
    print(isPalindrome2(x2))
    print(isPalindrome2(x1))
#47, 58
main()