
class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.n = len(self.stack)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

    def main(self):
        input = ["MyQueue", "push", "push", "peek", "pop", "empty"]

        myQueue = MyQueue()
        myQueue.push(1)
        myQueue.push(2)
        print(myQueue.peek())
        print(myQueue.pop())
        print(myQueue.empty())
    main(self)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
