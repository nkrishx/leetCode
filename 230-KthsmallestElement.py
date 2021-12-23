# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    in order traversal logic 
    set return conditions based on k value
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack =[]
        stack.append(root)
        while(len(stack)!=0 or root!=None):
            while(root != None):
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if k==0:
                return root.val
            root = root.right
        return -1