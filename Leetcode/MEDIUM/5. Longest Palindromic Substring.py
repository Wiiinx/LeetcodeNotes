def longestPalindrome(s):
    ss = list(s)
    res = []
    ans = []
    archive = []
    def isPalindrome(lst):
        str1 = ''.join(lst)
        i, j = 0, len(str1) - 1
        flag = True
        while i <= j:
            if str1[i] != str1[j]:
                flag = False
                return None
            i += 1
            j -= 1
        if flag == True:
            return str1
    i = 0
    while i < len(ss):
        count = i + 1
        res.append(ss[i])
        if ss[i] in res:
            res = ss[i: count + 1]
            if res not in archive:
                new_res = isPalindrome(res)
                ans.append(new_res)
                i = 0
                res = []
            else:
                i += 1
                continue
        i += 1

    cur_max = ['', 0]
    for j in ans:
        if len(j) > cur_max[1]:
            cur_max[0] = j
            cur_max[1] = len(j)
    return cur_max[0]



def main():
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("sbdfhehhee"))  #ehhe
    #print(longestPalindrome("iswewe"))  #wew or eew
    print(longestPalindrome("eweisewerhdeedh")) #hdeedh

main()