def videoStitching(clips, time):
    end, end2, res = -1, 0, 0
    for i, j in sorted(clips):
        if end2 >= time or i > end2:
            break
        elif end < i <= end2:
            res, end = res + 1, end2
        end2 = max(end2, j)
    return res if end2 >= time else -1




def main():
    clips1 = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    time1 = 10

    clips2 = [[0, 1], [1, 2]]
    time2 = 5
    clips3 = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
             [4, 5], [5, 7], [6, 9]]
    time3 = 9
    print(videoStitching(clips1, time1))
    print(videoStitching(clips2, time2))
    print(videoStitching(clips3, time3))

main()