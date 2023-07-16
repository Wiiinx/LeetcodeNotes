def minCostClimbingStairs(cost):
    if not cost:
        return 0
    dp = [0] * len(cost)
    dp[0] = cost[0]

    if len(cost) >= 2:
        dp[1] = cost[1]

    # dp[2] = cost[2] + min(dp[0], dp[1])
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-2], dp[i-1])

    return min(dp[-1], dp[-2])

def main():
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


main()