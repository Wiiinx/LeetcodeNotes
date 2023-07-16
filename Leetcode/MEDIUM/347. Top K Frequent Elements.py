def topKFrequent(nums, k):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    res = sorted(dict.values())[-k:]
    ans = []

    for i in dict.items():
        if i[1] in res:
            ans.append(i[0])
    ans.reverse()


    return ans


def main():
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4], 3))
    print(topKFrequent([1], 1))

main()