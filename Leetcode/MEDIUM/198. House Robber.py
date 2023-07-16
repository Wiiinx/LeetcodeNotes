def rob(nums):
    dp = [0] * len(nums)

    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums[0], nums[1])

    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = dp[i - 2] + nums[i]

    return dp
def main():
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))

main()