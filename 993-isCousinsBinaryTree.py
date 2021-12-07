# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.x_parent = None
        self.y_parent = None
        self.x_height = 0
        self.y_height = 0
        
    def dfs(self,root,level,parent,x,y):
            if root is None:
                return
            
            if root.val == x:
                self.x_parent = parent
                self.x_height = level
            
            if root.val == y:
                self.y_parent = parent
                self.y_height = level
                
            self.dfs(root.left,level+1,root,x,y)
            self.dfs(root.right,level+1,root,x,y)
    
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        '''
        dfs recursive solution
        '''
        self.dfs(root, 0, None, x, y)
        
        if self.x_parent != self.y_parent and self.x_height == self.y_height:
            return True
        else:
            return False
        
    
        
        