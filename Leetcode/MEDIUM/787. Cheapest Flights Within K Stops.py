import collections
import heapq


# Bellman-Ford
def findCheapestPrice(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1): # k + 1 layers
        tmpPrices = prices.copy()

        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p  # updating the min cost
            prices = tmpPrices # update temp
    return -1 if prices[dst] == float("inf") else prices[dst]


def main():
    print(findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))

main()