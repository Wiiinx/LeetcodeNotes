def generate(numRows):
    def helper(numRows, res):
        if numRows < 1:
            return []
        elif numRows < 2:
            return [[1]]
        elif numRows < 3:
            return [[1], [1, 1]]

        res = helper(numRows - 1, res)
        lst = [1]
        #print(numRows, res[numRows-2])
        for i in range(1, len(res[numRows-2])):
            #print(res[numRows-2][i-1], res[numRows-2][i])
            lst.append(res[numRows-2][i-1] + res[numRows-2][i])
        lst.append(1)
        res.append(lst)
        return res

    res = []
    res = helper(numRows, res)

    return res



def main():
    print(generate(5))
    print(generate(1))
main()