def search(nums, target):
    L, H = 0, len(nums)
    while L < H:
        M = (L + H) // 2
        if target < nums[0] < nums[M]:  # -inf
            L = M + 1
        elif target >= nums[0] > nums[M]:  # +inf
            H = M
        elif nums[M] < target:
            L = M + 1
        elif nums[M] > target:
            H = M
        else:
            return M
    return -1


def main():
    print(search([4, 5, 6, 7, 0, 1, 2], 0)) #4
    print(search([4, 5, 6, 7, 0, 1, 2], 3)) #-1
    print(search([1], 0)) #-1
    print(search([1], 1))   #0
    print(search([1, 3], 1)) #0
    print(search([1, 3], 3)) #1
    print(search([1, 3, 5], 1)) #1
    print(search([4, 5, 6, 7, 0, 1, 2], 1)) #5


main()