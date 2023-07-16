import collections
def lastStoneWeight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first: #opposite way
            heapq.heapush(stones, second - first) # adding the difference

    stones.append(0)
    return abs(stones[0])


def main():
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))

main()