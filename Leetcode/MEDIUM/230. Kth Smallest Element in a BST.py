import B_tree

# Brute Force
def kthSmallest(root, k):
    res, stack = [], []


    def traverse(root, stack, res):
        stack.append(root)

        while stack:
            sLen = len(stack)
            for i in range(sLen):
                Node = stack.pop()
                if Node:
                    res.append(Node.val)
                    traverse(root.left, stack, res)
                    traverse(root.right, stack, res)
    traverse(root, stack, res)
    res = sorted(res)
    return res[k-1]


# Using counter

def kthSmallest1(root, k):
    def dfs(root, count):
        if not root:
            return

        count += 1
        dfs(root.left, count)
        if count == k:
            print(count, root.val)
            return root.val
        dfs(root.right, count)


    return dfs(root, 0)





def main():
    data = [3, 1, 4, None, 2]
    root1 = B_tree.creatBTree(data, 0)
    print(kthSmallest(root1, 1))

    data2 = [5, 3, 6, 2, 4, None, None, 1]
    root2 = B_tree.creatBTree(data2, 0)
    print(kthSmallest1(root2, 3))


main()