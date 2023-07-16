def lengthOfLIS(nums):
    res = []
    for num in nums:
        for i, v in enumerate(res):
            if num <= v:  # 插卡
                res[i] = num  # 将比自己大的替换掉，成为新的连续数字
                # [10, 9, 2, 5, 3, 7, 101, 18]中： 3替换掉5
                break  # 当前最小，替换掉前面的，换下一个数字插卡
        else:
            res.append(num)  # 前面没找到替换的，插入后面，length + 1
    return res





def main():
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))

main()