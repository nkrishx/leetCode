# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    inorder traversal with condition check for bast and then swap
    '''
    def __init__(self):
        self.first = None
        self.last = None
        self.prev = None
        self.flag = False
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self.inorder(root)
        temp=self.last.val
        self.last.val = self.first.val
        self.first.val = temp
        
    def inorder(self,root):
        #base
        if root is None:
            return
        #logiv
        self.inorder(root.left)
        if self.prev != None and self.prev.val >=root.val:
            if self.flag==False:
                self.last=root
                self.first=self.prev
                self.flag= True
            else:
                self.last = root
                
        self.prev=root
        self.inorder(root.right)
    
        