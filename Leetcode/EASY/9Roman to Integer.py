def romanToInt(s):
    check_lst = [1, 5, 10, 50, 100, 500, 1000]
    sum_lst = []
    str = 'IVXLCDM'

    for i in range(len(s)):
        if s[i] in str:
            val = str.find(s[i])
            if i > 0 and check_lst[val] > sum_lst[i - 1]:
                diff = check_lst[val] - sum_lst[i - 1] - sum_lst[i - 1]
                sum_lst.append(diff)
            else:
                sum_lst.append(check_lst[val])
    return sum(sum_lst)


def main():
    print(romanToInt("III"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))

main()