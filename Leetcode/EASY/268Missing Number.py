def missingNumber(nums):
    res = 0
    for i in range(len(nums)):
        res += (i - nums[i])
    return res





def main():
    print(missingNumber([3, 0, 1]))
    print()
    print(missingNumber([0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([1]))

main()