def missingNumber(nums):
    n = len(nums)
    nums.sort()
    i = 1
    if nums[0] != 0:
        return 0
    while i < n:
        if i < len(nums):
            if nums[i - 1] + 1 != nums[i]:
                return nums[i - 1] + 1
        i += 1
    return nums[len(nums)-1] + 1






def main():
    print(missingNumber([3, 0, 1]))
    print()
    print(missingNumber([0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([1]))

main()