class HashBucket:
    
    def __init__(self):
        self.hashBucket = []
    
    def get(self,key):
        for bucketKey in self.hashBucket: 
            if bucketKey[0] == key:
                return bucketKey[1]
        return -1
    
    def put(self,key,value):
        for index,keyVal in enumerate(self.hashBucket):
            if(keyVal[0] == key):
                self.hashBucket[index] = (key,value)
                return
        self.hashBucket.append((key,value))
        
    def remove(self,key):
        for index,keyVal in enumerate(self.hashBucket):
            if(keyVal[0] == key):
                del self.hashBucket[index]
    
    
class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.hash_map = [HashBucket() for i in range(self.size)]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key%self.size
        self.hash_map[hash_key].put(key, value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_key = key % self.size
        return self.hash_map[hash_key].get(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key % self.size
        self.hash_map[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)