def isValid(s):
    dict = {'(': ')', '{': '}', '[': ']'}
    str2 = []
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in dict:
            str2.append(i)
        elif not str2 or dict[str2.pop()] != i:
            return False

    return not str2


def main():
    #print(isValid("()"))
    #print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("{[]}"))
    print(isValid("(){[{()}]}()(())"))
    print(isValid("{[{((}]}"))
    print(isValid("([)]"))


main()