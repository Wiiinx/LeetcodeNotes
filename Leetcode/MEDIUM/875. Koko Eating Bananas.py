import math
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r  # initial is the max in pile
    def eatingHours(mid, piles):
        count = 0
        for i in piles:
            count += math.ceil(i/mid)
        return count

    while l <= r:
        k = (l+r) // 2
        cur_h = eatingHours(k, piles)
        if cur_h <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res




def main():
    print(minEatingSpeed([3, 6, 7, 11], 8))
    print(minEatingSpeed([30,11,23,4,20], 5))
    print(minEatingSpeed([30,11,23,4,20], 6))
main()