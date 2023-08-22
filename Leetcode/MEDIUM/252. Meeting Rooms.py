
def canAttendMeetings(intervals):
    intervals.sort(key=lambda i: i[0])

    prevEnd = intervals[0][0]
    for start, end in intervals:
        if start < prevEnd:
            return False
        prevEnd = end
    return True

def main():
    print(canAttendMeetings([(0, 30), (5, 10), (15, 20)]))
    print(canAttendMeetings([(5,8),(9,15)]))

main()