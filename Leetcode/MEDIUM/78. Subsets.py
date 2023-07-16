# Recursion
def recur(nums, res):
    if len(nums) == 0:
        return res

    if nums in res:
        res.remove(nums)
    res.append(nums)
    return recur(nums[1:], res) and recur(nums[:-1], res)


def subset2(nums):
    def permutation(start, end, nums):
        if start == end:
            res.append(nums[:])

        for i in range(start, end):
            #nums[start], nums[i] = nums[i], nums[start]
            permutation(start + 1, end, nums)
            #nums[start], nums[i] = nums[i], nums[start]

    res = [[]]
    for i in range(len(nums)):
        permutation(0, len(nums[i:]), nums[i:])
    return res

def subsets2(nums):
    def dfs(nums, idx, path, res):
        print("idx:", idx, "path:", path)
        res.append(list(path))   # has to be list() method
        for i in range(idx, len(nums)):
            path.append(nums[i])
            dfs(nums, i+1, path, res)  # Recursion here
            path.pop()

    res, path = [], []
    dfs(nums, 0, path, res)  # star recursion
    return res


def subset(nums):
    res = []
    def backtrack(idx, nums, path, res):
        res.append(list(path))

        for i in range(idx, len(nums)):
            path.append(nums[i])
            backtrack(i+1, nums, path, res)
            path.pop()

    backtrack(0, nums, [], res)
    return res

def main():
    print(subset([1, 2, 3]))
    print(subset([0]))
main()