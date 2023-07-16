def groupAnagrams1(strs):  # failed case by strs2 = ["", ""]
    dict = {}
    values = []
    res = []
    for n in strs:
        inner = {}
        for i in n:
            if i not in inner:
                inner[i] = 1
            else:
                inner[i] += 1

        dict[n] = inner



    for k, v in dict.items():
        if v not in values:
            values.append(v)
            res.append([k])
        else:
            idx = values.index(v)
            res[idx].append(k)

    return res

def groupAnagrams(strs):
    hash_table = {}
    for i in strs:
        sorted_str = ''.join(sorted(i))

        if sorted_str not in hash_table:
            hash_table[sorted_str] = []

        hash_table[sorted_str].append(i)

    return list(hash_table.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs1 = [""]
    strs2 = ["", ""]
    print(groupAnagrams1(strs))
    print(groupAnagrams1(strs1))
    print(groupAnagrams1(strs2))

    print(groupAnagrams(strs))
    print(groupAnagrams(strs1))
    print(groupAnagrams(strs2))

main()