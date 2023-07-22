def canPartition(nums):
    if sum(nums) % 2: return False  # sum不能被平分为2

    dp = set()
    dp.add(0)
    target = sum(nums) // 2
    if target < 0: return False
    if target == 0: return True

    for i in range(len(nums) - 1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    return True if target in dp else False

def main():
    print(canPartition([1, 5, 11, 5]))
    print(canPartition([1, 2, 3, 5]))

main()