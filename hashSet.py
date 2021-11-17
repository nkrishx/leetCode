class MyHashSet(object):

    def __init__(self):
        self.bucket = 1000
        self.bucketItem = 1001
        self.storage = [False]*1000
    
    def bucketHash(self,key):
        return key%self.bucket
    
    def bucketItemHash(self,key):
        return key/self.bucketItem

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        x = self.bucketHash(key)
        y = self.bucketItemHash(key)
        if(self.storage[x]== False):
            self.storage[x]=[False]*1000
        self.storage[x][y] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        x = self.bucketHash(key)
        y = self.bucketItemHash(key)
        if(self.storage[x]== False):
            return
        self.storage[x][y]=False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        x = self.bucketHash(key)
        y = self.bucketItemHash(key)
        if(self.storage[x] == False):
            return False
        return self.storage[x][y]

    
    


# Your MyHashSet object will be instantiated and called as such:
#obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)