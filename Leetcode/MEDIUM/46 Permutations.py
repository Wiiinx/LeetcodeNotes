def permute1(nums):
    def helper(start, end):
        if start == end:

            #print(nums[:])
            res.append(nums[:])

        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            helper(start+1, end)
            nums[start], nums[i] = nums[i], nums[start]
    res = []
    helper(0, len(nums))
    return res





def permute(nums):
    path = []
    res = []

    def dfs(nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    dfs(nums, path, res)
    return res



def main():
    print(permute([1, 2, 3]))
    #print(permute([0, 1]))
    #print(permute([1]))

main()