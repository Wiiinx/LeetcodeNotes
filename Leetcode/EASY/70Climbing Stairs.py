def climbStairs(n):
    # edge cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [1, 2]
    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])


    return dp[n - 1]

def main():
    print(climbStairs(3))
    print(climbStairs(4))

    print(climbStairs(99))

main()