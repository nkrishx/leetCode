"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    '''
    bfs solution
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        hashMap={}
        queue=collections.deque()
        copyNode=Node(node.val)
        queue.append(node)
        hashMap[node]=copyNode
        
        while(len(queue)!=0):
            curr=queue.popleft()
            #get each of the neighbours of the current
            for each in curr.neighbors:
                if each not in hashMap:
                    neighbourCopy=Node(each.val)
                    hashMap[each]=neighbourCopy
                    queue.append(each)
                hashMap[curr].neighbors.append(hashMap[each])
        
        return hashMap[node]
        
        