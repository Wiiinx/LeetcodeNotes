def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # top row: left -> right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # right col: top -> down
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # bottom row: right -> left
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        # left col: bottom -> up
        for i in range(bottom-1, top-1,-1):
            res.append(matrix[i][left])
        left += 1
    return res


def main():
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
main()