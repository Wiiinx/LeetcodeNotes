def setZeroes(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/rows need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                # set the first col to zero
                # indicating this row should be 0
                matrix[0][c] = 0

                # marking the first row to zero
                # indicating which col should be 0
                # the [0][0] position should be rowZero( overlapping session)
                if r > 0:
                    matrix[r][0] = 0
                else:
                    # change the overlapping session to True
                    rowZero = True
    for r in range(1, ROWS):
        for c in range(1, COLS):
            # if the first col/row is 0, setting entire
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # zero out 1st col
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
    # zero out 1st row
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
    return matrix



def main():
    #print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

main()