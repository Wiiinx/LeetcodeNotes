def threeSum(nums):
    nums.sort()
    res = []
    for left in range(len(nums) - 2):
        if nums[left] > 0:  # start with positive will always > 0
            break
        if left > 0 and nums[left] == nums[left - 1]:  # duplicate with previous num
            continue
        mid = left + 1  # 中间的指针
        right = len(nums) - 1
        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum > 0:  # right往小的走
                right -= 1
            elif curr_sum < 0:   # mid往大的走
                mid += 1
            else:  # sum == 0
                res.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]:
                    mid += 1
                while right > mid and nums[right] == nums[right - 1]:
                    right -= 1
                mid += 1
                right -= 1
    return res


def threeSum2(nums):
    res = set()

    # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # 2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p)

    # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    #   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1 * num in N:
                res.add((-1 * num, 0, num))

    # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0, 0, 0))

    # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    #   exists in the positive number set
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    #   exists in the negative number set
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res


def main():
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]
    print(threeSum2(nums1))
    print(threeSum(nums2))
    print(threeSum(nums3))

main()
