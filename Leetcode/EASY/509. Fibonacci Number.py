def fib1(n):

    # using DFS
    if n < 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    indeg = [2] * (n + 1)
    indeg[0] = 0
    indeg[1] = 0

    def dfs(x):
        if x == n:
            return
        next = [2] if x == 0 else [x + 1, x + 2]
        for y in next:
            if y > n:
                continue
            dp[y] += dp[x]
            indeg[y] -= 1
            if indeg[y] == 0:
                dfs(y)

    for i in range(2):
        dfs(i)

    return dp[n]


def fib2(n):
    # using stack
    if n < 2:
        return n
    stack = [0, 1]
    dp = [0] * (n + 1)
    dp[1] = 1
    indeg = [0] * (n + 1)
    indeg[1] = 1




def main():
    print(fib1(8))

main()