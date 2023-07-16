def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    l, r = 0, rows * cols - 1

    while l <= r:
        mid = (l+r) // 2
        nums = matrix[mid//cols][mid % cols]
        if nums == target:
            return True
        elif nums < target:
            l = mid+1
        else:
            r = mid-1

    return False


def other(matrix, target):
    l, r = 0, len(matrix) * len(matrix[0])-1
    while l <= r:
        mid = (l + r) // 2
        if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
            return True
        if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
            l = mid + 1
        else:
            r = mid

    return False


def main():
    #print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    #print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34))
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 35))
    print(searchMatrix([[1,3]], 3))
    print(other([[1,3]], 3))
    #print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 5))

main()