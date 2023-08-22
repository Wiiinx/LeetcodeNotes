def merge(intervals):
    intervals.sort()


    res = [intervals[0]]
    for i in range(len(intervals)):
        ans = []


        if res[-1][1] >= intervals[i][0] and res[-1][0] <= intervals[i][1] :
            ans.append([min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])])
            res.pop()
            res.append(ans[0])

        elif res[-1][1] >= intervals[i][0] and res[-1][0] >= intervals[i][1]:
            ans.append(intervals[i])
            ans.append(res[-1])
            res.pop()
            res.append(ans[0])
            res.append(ans[1])

        else:
            res.append(intervals[i])
    return res

def main():
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[0,0]])) # [[0,0],[1,4]]
    print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
main()