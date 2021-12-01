# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    brute force method with inOrder traversal (left,right,root) is below
    The same logic is replaced with the isValidBST fun here
    under the hood the same mechanism happens
    '''
    def isValidBST(self, root):
        self.prev = None
        
        return self.inorder(root)
    
    def inorder(self, root):
        # base case where we have traversed the entire height 
        # of the tree
        if root == None: return True

        # logic
        #splitting here for inorder traversal (left)
        if self.inorder(root.left) == False:
            return False
        
        if self.prev is not None and self.prev.val >= root.val:
            return False
        self.prev = root
        
        if self.inorder(root.right) == False:
            return False
        
        return True
        
        
        
        
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
        
#         prev = TreeNode(None)
        
#         stack = []
        
#         while root or len(stack) > 0:
#             while root:
#                 stack.append(root)
#                 root = root.left
            
#             root = stack.pop()
#             if prev.val is not None and prev.val >= root.val:
#                 return False
#             prev = root
#             root = root.right
            
#         return True
        