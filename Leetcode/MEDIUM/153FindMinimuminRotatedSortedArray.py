# constrains:  O(log n) time.

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:  # list in order
            left += 1  # 往右边找
        else:
            right = mid  # 往左边找

    return nums[left]



def main():
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))
main()