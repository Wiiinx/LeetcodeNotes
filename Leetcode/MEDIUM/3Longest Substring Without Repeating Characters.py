def lengthOfLongestSubstring(s):
    charSet = set()
    l, res = 0, 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r+1 - l)
    return res




def lengthOfLongestSubstring2(s):
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:
            output = max(output, r - l + 1)
        else:
            if seen[s[r]] < l:
                output = max(output, r - l + 1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output

def main():
    print(lengthOfLongestSubstring("abcabcbb"))
    #print(lengthOfLongestSubstring("bbbbb"))
    #print(lengthOfLongestSubstring("pwwkew"))
    #print(lengthOfLongestSubstring(''))
    print(lengthOfLongestSubstring('au'))
    print(lengthOfLongestSubstring("cdd"))
main()