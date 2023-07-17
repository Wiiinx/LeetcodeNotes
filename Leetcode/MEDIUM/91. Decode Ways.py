def numDecodings_m(s):
    # Memoization
    dp = {len(s): 1}  # if empty string, return 1
    # pattern dp[i] = dp[i+1] + dp[i+2], 往后取一位 or 取两位有多少种solution，反过来取
    def dfs(i):  # position in s
        if i in dp:  # already benn cached, or i is the last position in string
            return dp[i]
        if s[0] == '0':
            return 0

        res = dfs(i + 1)
        if i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
            res += dfs(i + 2)
        dp[i] = res
        return res
    return dfs(0)


def numDecodings(s):
    # Dynamic Programming
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
        print(i, dp)
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            dp[i] += dp[i + 2]

    return dp[0]


def main():
    print(numDecodings("12"))
    print(numDecodings("226"))
    print(numDecodings("06"))

main()