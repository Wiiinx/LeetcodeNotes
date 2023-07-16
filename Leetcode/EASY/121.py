def maxProfit(prices):
    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right  # 更新最低买入价格，直接从这个价格后面找
        right += 1
    return max_profit

def main():
    lst1 = [7,1,5,3,6,4]
    lst2 = [7,6,4,3,1]
    print(maxProfit(lst1))
    print(maxProfit(lst2))

main()