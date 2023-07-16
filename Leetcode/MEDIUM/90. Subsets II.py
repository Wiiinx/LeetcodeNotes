def subsetsWithDup(nums):
    res = []
    nums.sort()
    def backtrack(nums, path, res):
        if path not in res:
            res.append(list(path))

        for i in range(len(nums)):
            path.append(nums[i])
            backtrack(nums[i+1:], path, res)
            path.pop()

    backtrack(nums, [], res)
    return res
def main():
    print(subsetsWithDup([1, 2, 2]))
    print(subsetsWithDup([4,4,4,1,4]))

main()