class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        '''
        doubly linked list for o(1) operations
        we use a dummy head and tail for easy operations
        '''
        self.size = capacity
        self.hashMap = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addToList(self,node):
        '''
        when we need to add a node to list,
        node ref passed
       '''
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    def removeFromList(self,node):
        '''
        remove node
        '''
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        '''
        get in o(1)
        '''
        #check in hashMap if existing if not return -1
        if key not in self.hashMap:
            return -1
        
        #we need to get the value and also add it to the top of the list
        #add to list
        node = self.hashMap[key] #get node
        self.removeFromList(node) #rewmove from current position 
        self.addToList(node) #add to start of list
        
        return node.val    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value 
            self.removeFromList(node)
            self.addToList(node)   
        else:
            if len(self.hashMap) == self.size:
                last_node = self.tail.prev
                del self.hashMap[last_node.key]
                self.removeFromList(last_node)

            node = Node(key,value)   
            self.addToList(node)
            self.hashMap[key] = node
            
        return 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)