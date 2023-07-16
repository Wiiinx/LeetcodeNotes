def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set()  # cannot revisit the same position

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c<0 or r>=rows
                or c >=cols or
                word[i] != board[r][c] or (r, c) in path): # all the invalid condition
            return False
        path.add((r, c))

        # found the character and look for next step
        # look for all other 4 possible position
        res = (dfs(r+1, c, i+1)) or \
              (dfs(r-1, c, i+1)) or \
              (dfs(r, c+1, i+1)) or \
              (dfs(r, c-1, i+1))
        path.remove((r, c))  #already found the position
        return res

    # start traversing from all the position
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True

    return False
    # O(n * m * 4^n)
    # dfs = 4^len(word)


def main():
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],["A", "D", "E", " E"]], "ABCCED"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))


main()