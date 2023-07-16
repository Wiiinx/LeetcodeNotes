def maxProfit(prices):
    cur_max, left, right = 0, 0, 1

    max_lst = []
    index_lst = []



    while right < len(prices):

        if prices[left] < prices[right]:
            "找到max之后存一下"
            if prices[right] - prices[left] > cur_max:
                max_lst.append(prices[right] - prices[left])
                index_lst.append(left)
                print("Max", max_lst, "Idx", index_lst)

           # prices = prices[right + 1:]
            cur_max = 0

        else:
            left = right
        right += 1
    return sum(max_lst)





def main():
    #print(maxProfit([7, 1, 5, 3, 6, 4]))
    #print(maxProfit([1, 2, 3, 4, 5]))
    print(maxProfit([1, 2, 3, 4, 5]))
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))


main()