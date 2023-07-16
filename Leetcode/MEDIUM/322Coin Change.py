def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])
                '''
                                coin = 4, 
                                a = 7
                                dp[7] = 1 + dp[3]  # 7 - 4 = 3
                                '''
    return dp[amount] if dp[amount] != amount + 1 else -1
    #O(n)



def main():
    print(coinChange([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange([1], 0))

main()