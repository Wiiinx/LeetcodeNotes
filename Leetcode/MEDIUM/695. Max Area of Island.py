def maxAreaOfIsland(grid):
    def dfs(grid, r, c):
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != 1):
            return 0
        grid[r][c] = 0
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)

    if not grid:
        return 0

    max_Area = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                max_Area = max(max_Area, dfs(grid, r, c))
    return max_Area

def main():
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(maxAreaOfIsland(grid1))

main()