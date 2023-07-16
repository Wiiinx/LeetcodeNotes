def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        #  check if it's the start of a sequence
        if (n-1) not in numSet:  # start of a sequence
            length = 0
            while(n + length) in numSet:  # check the consecutive part
                length += 1
            longest = max(length, longest)
    return longest


def main():
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))

main()