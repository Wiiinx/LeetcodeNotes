from functools import reduce

nums = [1, 2, 3, 5]
zero_count = nums.count(0)
prod = reduce(lambda a, b: a*(b if b else 1), nums, 1)
for i, c in enumerate(nums):  # i = index, c =nums[i]
    if zero_count:
        nums[i] = 0 if c else prod   # if c is not 0, add 0 in list, else (c is 0), add prod to the list
    else:
        nums[i] = prod // c

print(nums)