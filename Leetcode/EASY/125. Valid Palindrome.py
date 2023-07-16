
def isPalindrome(s):
    t = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            t += i.lower()
    l, h = 0, len(t)-1

    while l < h:
        if t[l] != t[h]:
            return False
        else:
            l += 1
            h -= 1
    return True


def main():
    #print(isPalindrome("A man, a plan, a canal: Panama"))
    #print(isPalindrome("race a car"))
    #print(isPalindrome(" "))
    print(isPalindrome("0P"))
    print(isPalindrome("3P"))

main()