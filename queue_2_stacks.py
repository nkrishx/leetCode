class MyQueue(object):

    def __init__(self):
        self.inStack =[]
        self.outStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.outStack.pop()
            

    def peek(self):
        """
        :rtype: int
        """
        if(len(self.outStack)==0):
            while(len(self.inStack)!=0):
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if(len(self.inStack)==0 and len(self.outStack)==0):
            return True
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()