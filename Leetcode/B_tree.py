class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 创建一二叉树
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode


# Leetcode235
def lowestCommonAncestor(root, p, q):
    def dfs(target, root, stack):
        if root:
            if target == root.val:
                stack.append(root.val)
                return stack
            if target < root.val:
                stack.append(root.val)
                dfs(target, root.left, stack)
            else:
                stack.append(root.val)
                dfs(target, root.right, stack)
        return stack

    p_stack = dfs(p, root, [])
    q_stack = dfs(q, root, [])
    ptr = 0
    res = 0

    while ptr < min(len(p_stack), len(q_stack)):
        if p_stack[ptr] == q_stack[ptr]:
            res = p_stack[ptr]
            ptr += 1
        else:
            return res
    return res

if __name__ == "__main__":
    root1 = creatBTree([6,2,8,0,4,7,9,None,None,3,5], 0)
    print(lowestCommonAncestor(root1, 2, 4))