"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    '''
    dfs solution with queue works for both perfect binary tree and non perfect
    without queue is for perfect binary tree
    commented code is without queue
    '''
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        # level = root
        # while(level.left!=None):
        #     curr = level
        #     while curr!=None:
        #         curr.left.next = curr.right
        #         if curr.next !=None:
        #             curr.right.next = curr.next.left
        #         curr = curr.next
        #     level = level.left
        # return root
        
        queue = collections.deque()
        queue.append(root)
        
        while(len(queue)!=0):
            size = len(queue)
            prev = queue.popleft()
            if prev.left != None:
                queue.append(prev.left)
                queue.append(prev.right)
            for i in range(1,size):
                curr = queue.popleft()
                if curr.left!= None:
                    queue.append(curr.left)
                    queue.append(curr.right)
                prev.next = curr
                prev = curr
        return root