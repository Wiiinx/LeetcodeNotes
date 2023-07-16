def longestCommonSubsequence(text1, text2):
    lst = ['']
    text1 = '' + text1
    text2 = '' + text2
    flag_lst = []



    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                if j >= text2.index(lst[-1]) and j not in flag_lst:
                    # print(i, text2.index(lst[-1]), lst[-1])
                    lst.append(text1[i])
                    flag_lst.append(j)

                else:

                    lst.remove(lst[-1])
                    lst.append(text1[i])


    return ''.join(lst[1:])


def main():
    print(longestCommonSubsequence('abcde', 'ace'))
    print(longestCommonSubsequence('ezupkr', 'ubmrapg'))
    print(longestCommonSubsequence('bsbininm', 'jmjkbkjkv'))

main()

#bsbininm
#jmjkbkjkv