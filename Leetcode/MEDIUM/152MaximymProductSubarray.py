# TimeLimitExceed!!!!!
def maxProduct(nums):
    cur_max = min(nums)


    def prod(lst1):
        prod = 1
        lst = []
        for i in range(len(lst1)):
            prod *= lst1[i]
            lst.append(prod)
        return max(lst)

    for i in range(len(nums) - 1):
        cur_prod = prod(nums[i:])
        cur_max = max(cur_prod, cur_max)


    return max(cur_max, max(nums))




def maxProduct1(nums):
    cur_max = min(nums)

    def product_helper(nums):
        lst = []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            lst.append(prod)
        return max(lst)


    for i in range(len(nums)):
        cur_prod = product_helper(nums[i:])
        cur_max = max(cur_max, cur_prod)
    return cur_max


def main():
    nums1 = [2, 3, -2, 4]
    nums2 = [-2, 0, -1]
    nums3 = [2, -3, 4, -8, 0]

    print(maxProduct1(nums1))  #6
    print(maxProduct1(nums2))  #0
    print(maxProduct1([0, 2]))  #2
    print(maxProduct1([0, 2, 2]))  #4
    print(maxProduct1([-4, -3]))  #12
    print(maxProduct1([3, -1, 4]))  #4
    print(maxProduct1([-2])) #-2


main()
