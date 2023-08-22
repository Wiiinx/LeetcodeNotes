# dp
def uniquePaths(m, n):
    row = [1] * n
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1): #reverse order
            newRow[j] = newRow[j + 1] + row[j] # compute the new row
        row = newRow #update the new row

    return row[0]

    # Time: O(n * m)
    # Memory: O(n)




def main():
    print(uniquePaths(3, 7))
    print(uniquePaths(3, 2))

main()