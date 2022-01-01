class PhoneDirectory:
    '''
    o(1) solution for all operations
    '''
    def __init__(self, maxNumbers: int):
        self.queue = collections.deque()
        self.hashSet = []
        
        for i in range(0,maxNumbers):
            self.queue.append(i)
        
    def get(self) -> int:
        if len(self.queue)!=0:
            number = self.queue.popleft()
            self.hashSet.append(number)
            return number
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.hashSet:
            return False
        else:
            return True

    def release(self, number: int) -> None:
        if number in self.hashSet:
            self.hashSet.remove(number)
            self.queue.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)