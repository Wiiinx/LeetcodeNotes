import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 创建树
def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root


def rightSideView(root):
    q = collections.deque()
    if root:
        q.append(root)
    res = []
    while q:
        size, val = len(q), 0

        for i in range(size):
            removeNode = q.popleft()
            val = removeNode.val  # val会变成最后一个popleft的，也就是最右边的值
            if removeNode.left:
                q.appendleft(removeNode.left)
            if removeNode.right:
                q.append(removeNode.right)
        res.append(val)

    return res


def main():
    data = [1, 2, 3, None, 5, None, 4]
    data2 = [1, 2, 3, 4]
    pNode = build(data)
    pNode2 = build(data2)
    res = rightSideView(pNode)

    print(res)
    print(rightSideView(pNode2))


main()