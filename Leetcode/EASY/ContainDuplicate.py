def containsDuplicate(nums):
    lst = []
    for i in nums:
        if i in lst:
            return True
        lst.append(i)
    return False



def main():
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums1))
    print(containsDuplicate(nums2))
    print(containsDuplicate(nums3))

main()