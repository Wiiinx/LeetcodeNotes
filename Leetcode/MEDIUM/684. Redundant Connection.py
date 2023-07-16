def findRedundantConnection(edges):
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = par[n]

        while p != par[p]:  # try to find root parents
            par[p] = par[par[p]]  # shorten the length, setting parent to grandparent
            p = par[p]
        # return the root parent
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:  #same parent, means already connected, redundant
            return False

        if rank[p1] > rank[p2]:
            par[p2] = p1  # updating parents
            rank[p1] += 1
        else:
            par[p1] = p2
            rank[p2] += 1
        return True

    for n1, n2 in edges:
        if not union(n1, n2):  # not able to union together, already connected
            return [n1, n2]



def main():
    edges1 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    edges2 = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantConnection(edges1))
    print(findRedundantConnection(edges2))
main()