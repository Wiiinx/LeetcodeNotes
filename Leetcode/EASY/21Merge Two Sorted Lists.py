class Node:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, val=None):
        self.head = None
        self.next = None
        if val is not None:
            self.add_multiple_nodes(val)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def val(self):
        return [node.val for node in self]

    def add_node(self, val):
        if self.head is None:
            self.next = self.head = Node(val)
        else:
            self.next.next = Node(val)
            self.next = self.next.next
        return self.next

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.next = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    while list2 is not None:
        nodeA, nodeB = list1, list2
        list2 = list2.next
        if nodeA.val < nodeB.val:
            nodeA.next = nodeB
            list1 = nodeB.next
        else:
            prev = None
            while nodeA is not None and nodeB.val > nodeA.val:   # lists are sorted
                prev = nodeA
                nodeA = nodeA.next  # traverse

            temp = prev.next  # A > B
            prev.next = nodeB
            nodeB.next = temp
    return list1


def mergeTwoLists2(list1, list2):
    nodeA, nodeB = list1, list2

    while nodeA:
        if nodeA.val < nodeB.val:
            nodeA.next = nodeB
            list1 = nodeB.next
            print(nodeA)
        else:

            nodeA = list1.next
            list1 = list1.next
            nodeB = list2.next





def main():
    lst1 = LinkedList()
    lst1.add_multiple_nodes([1, 2, 4])
    lst2 = LinkedList()
    lst2.add_multiple_nodes([1, 3, 4])
    #print(lst1)
    #print(lst2)
    print(mergeTwoLists2(lst1, lst2))






main()


