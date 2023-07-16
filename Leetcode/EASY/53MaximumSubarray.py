import itertools
import operator

def solution1(nums):  #dynamic programming
    max_sum = nums[0]
    current_sum = nums[0]  # current_sum < max_sum

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])  # current sum is always at least 0, otherwise start a new
        max_sum = max(max_sum, current_sum)
        # TIME O(N) SPACE O(1)
    return max_sum





def main():
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [1]
    nums3 = [5, 4, -1, 7, 8]

    print(solution1(nums1))

main()