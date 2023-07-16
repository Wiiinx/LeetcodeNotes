
class MinStack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin == None or val < curMin:
            curMin = val
        self.data.append((val, curMin)) # min永远被push在最上面


    def pop(self):
        """
        :rtype: None
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][1]  # return 刚刚push的东西



def main():

    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())  # return -3
    print(minStack.pop())
    print(minStack.top())  # return 0
    print(minStack.getMin())   # return -2





main()