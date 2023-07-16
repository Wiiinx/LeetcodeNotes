def twoSum(nums, target):
    dic = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in dic:
            return [dic[m], i]
        else:
            dic[n] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target)
    print(twoSum(nums, target))


main()