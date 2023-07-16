class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
            # initializing node

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None
            # 删除这个node本身

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        # initializing list by creating node

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        prev_node = node
        next_node = node.next
        new_node = DoublyLinkedList.Node(val, next_node, prev_node)
        # creating node, store val
        prev_node.next = new_node
        next_node.prev = new_node
        # adjusting pre node and next node
        self.size += 1
        return new_node

    def add_first(self, val):
        # let head be the prev, then this val is the first
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    # 想加在哪里，就在add after的参数里写前一个val，第一个就写header，最后一个写trailer

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    # let data.prev and data.next 互相指，这样可以空过中间的node
    # 再用disconnect去删除这个node

    def delete_first(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    # 把header后面的这个删掉，就是delete first
    # 不需要互相指，直接调用，原理一样

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next
        # cursor从第一个开始，如果不是trailer，则yield
        # cursor从下一个继续开始

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"


