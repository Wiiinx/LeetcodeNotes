def combinationSum(C, target):
    res = []
    ans = []
    def backtracking(lst, target, ans, res):
        print(lst, target, ans)
        if target < 0:
            return
        if target == 0:
            res.append(ans)
            return
        for i in range(len(lst)):
            backtracking(lst[i:], target - lst[i], ans+[lst[i]], res)
    backtracking(C, target, ans, res)

    return res

def combinationSum1(C, target):
    res = []
    def dfs(nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[i:], target - nums[i], path+[nums[i]], res)

    dfs(C, target, [], res)
    return res




def main():
    print(combinationSum([2, 3, 6, 7], 7))
    #print(combinationSum1([2, 3, 5], 8))
    #print(combinationSum([2], 1))

main()