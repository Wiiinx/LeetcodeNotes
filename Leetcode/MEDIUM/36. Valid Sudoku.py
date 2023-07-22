import collections
def isValidSudoku(board):
    cols = collections.defaultdict(set)  #Hashset
    rows = collections.defaultdict(set)
    square = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r]) or \
                    (board[r][c] in cols[c]) or \
                    board[r][c] in square[(r//3, c//3)]:
                return False

            # 在当前index下的set里面添加数字
            rows[r].add(board[r][c])  #  {0: {'6', '5'}, 1: {'3'}, 4: {'9', '7'}, 3: {'1'}, 5: {'5'}})
            cols[c].add(board[r][c])  # {0: {'5', '3', '7'}, 1: {'6', '9', '1', '5'}})
            square[(r//3, c//3)].add(board[r][c]) # {(0, 0): {'5', '6', '9', '3', '8'}, (0, 1): {'7', '5', '9', '1'}}
    return True






def main():
    board1 =[["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(isValidSudoku(board1))
main()