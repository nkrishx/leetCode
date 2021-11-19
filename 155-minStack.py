class MinStack(object):

    def __init__(self):
        self.mainStack = []
        self.minStack = []
        self.minStack.append(sys.maxint)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.mainStack.append(val)
        self.minStack.append(min(self.mainStack))
        

    def pop(self):
        """
        :rtype: None
        """
        self.mainStack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()