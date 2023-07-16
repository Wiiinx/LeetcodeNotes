def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    cur_sum = numbers[l] + numbers[r]
    while cur_sum != target:
        cur_sum = numbers[l] + numbers[r]
        #print(cur_sum, numbers[l], numbers[r])
        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return [l + 1, r + 1]




def main():
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([2, 3, 4], 6))
    print(twoSum([-1, 0], -1))
    print(twoSum([0, 0, 3, 4], 0))  # [1, 2]
    print(twoSum([0, 3, 3, 4], 6))


main()