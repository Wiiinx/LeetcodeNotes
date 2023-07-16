def generateParenthesis(n):
    res = []
    ans = []
    def bfs(openN, closeN):
        if openN == closeN == n:
            res.append(''.join(ans))
            return
        if openN < n:
            ans.append('(')
            bfs(openN+1, closeN)
            ans.pop()
        if closeN < openN:
            ans.append(')')
            bfs(openN, closeN+1)
            ans.pop()
    bfs(0, 0)
    return res


def generateParenthesis1(n):  # 不使用pop()， passing ans带入每次call
    res = []
    ans = []
    def backtrack(openN, closeN, ans):
        if len(ans) == 2 * n:
            res.append(''.join(ans))
            return
        if openN < n:
            ans.append('(')
            backtrack(openN+1, closeN, ans)
        if closeN < openN:
            ans.append(')')
            backtrack(openN, closeN+1, ans)
    backtrack(0, 0, ans)
    return res


def main():
    print(generateParenthesis(3))


main()