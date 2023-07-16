
def sortColors(nums):
    i = 1
    while i < len(nums):
        if nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i = 1
        else:
            i += 1


def main():
    nums1 = [2, 0, 2, 1, 1, 0]
    nums2 = [2, 0, 1]
    sortColors(nums1)
    sortColors(nums2)
    print(nums1)
    print(nums2)

main()