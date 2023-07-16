import collections
def orangesRotting(grid):
    q = collections.deque()
    time, fresh = 0, 0

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])  # appending all the locations for rotting oranges

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # up, right, down, left

    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()  # current rotten Orange starts to rotting others
            # and remove current self
            for dr, dc in directions:  # moving...up.. down ...
                row, col = dr + r, dc + c  # current location of (up/down/left/right)
                if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                    # check if it's a valid non-rotting orange
                    continue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1


def main():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(orangesRotting(grid))


main()