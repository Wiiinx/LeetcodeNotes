def isHappy(n):
    visit = set()

    while n not in visit:
        visit.add(n)
        lst = [int(x) ** 2 for x in str(n)]
        print(lst)
        n = sum([int(x) ** 2 for x in str(n)])


    return n == 1

def main():
    print(isHappy(199))

main()