from functools import reduce

def productExceptSelf(nums):
    '''
    lst = []
    idx = 0
    while idx < len(nums) :
        lst_product = 1
        for i in range(len(nums)):
            if i != idx:
                lst_product *= nums[i]
        lst.append(lst_product)
        idx += 1
    return lst
    '''
    prod = reduce(lambda a, b: a * (b if b else 1), nums, 1)
    zero_count = nums.count(0)
    if zero_count > 1:
        return [0]*len(nums)
    for i, c in enumerate(nums):  # i = index, c =nums[i]
        if zero_count:  # list全是0除非c所在的位置是0，进入else
            nums[i] = 0 if c else prod  #if c is not 0, add 0 in list, else (c is 0), add prod to the list
        else:
            nums[i] = prod // c
    return nums



def main():
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums1))
    print(productExceptSelf(nums2))

main()