def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i + len(w) <= len(s)) and s[i: i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]


def main():
    print(wordBreak("leetcode", ["leet","code"]))
    print(wordBreak("applepenapple", ["apple","pen"]))
    print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    print(wordBreak("aaaaaaa", ["aaaa","aaa"]))

main()