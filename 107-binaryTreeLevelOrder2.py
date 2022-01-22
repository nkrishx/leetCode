# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        queue.append(root)
        result = []
        
        if root is None:
            return []
        
        result.append([root.val])
        
        while(len(queue)!=0):
            size = len(queue)
            nodes = []
            for i in range(0,size):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                    nodes.append(curr.left.val)
                if curr.right is not None:
                    queue.append(curr.right)
                    nodes.append(curr.right.val)
            if len(nodes) != 0:
                result.insert(0,nodes)
            
        return result