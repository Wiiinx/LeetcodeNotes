

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lst = []
    i = 0
    count = 0
    while i < len(nums):
        count += nums[i]
        lst.append(count)
        i += 1

    return lst


def main():
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 1, 1, 1, 1]
    nums3 = [3, 1, 2, 10, 1]
    print(runningSum(nums1))
    print(runningSum(nums2))
    print(runningSum(nums3))



main()