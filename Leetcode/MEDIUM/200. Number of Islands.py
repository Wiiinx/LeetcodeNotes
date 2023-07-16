def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(grid, r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1'):
            return
        grid[r][c] = '0'  #把走过的路都替换成water，四周都是water就无路可走了 然后到 外面的loop count+1，重新寻找岛屿
        dfs(grid, r+1, c)
        dfs(grid, r-1, c)
        dfs(grid, r, c+1)
        dfs(grid, r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                count += 1
    return count

def main():
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]

    grid2 = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    print(numIslands(grid))
    print(numIslands(grid2))

main()