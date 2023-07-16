def isAnagram(s, t):
    dic = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    for j, p in dic.items():
        if j not in t:
            return False
        elif p != t.count(j):
            return False
    return True

def main():
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
    print(isAnagram("a", "ab"))
    print(isAnagram("aacc", "ccac"))


main()