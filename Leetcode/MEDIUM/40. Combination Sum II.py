def combinationSum2(C, target):
    res = []
    C.sort()
    def backtrack(idx, C, target, path, res):
        if target == 0:
            res.append(list(path))
            return

        for i in range(idx, len(C)):
            if i > idx and C[i] == C[i-1]:  #跳过重复的path
                continue
            if C[i] > target:
                break
            else:
                path.append(C[i])
                backtrack(i+1, C, target - C[i], path, res)
                path.pop()

    backtrack(0, C, target, [], res)
    return res

def main():
    print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combinationSum2([2, 5, 2, 1, 2], 5))

main()