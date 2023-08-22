def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        # if new end < start of cur
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            print('res:', res ,'+ intervals[i:', intervals[i:])
            return res + intervals[i:]
        # start is greater the end of interval
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            # overlapping -> update/merge
            print('merge',newInterval)
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            print('after merge', newInterval)
    res.append(newInterval)
    print(res)
    return res

def main():
    print(insert([[1,3],[6,9]], [2,5]))

main()