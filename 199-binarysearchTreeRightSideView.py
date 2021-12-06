# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result =[]
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        using dfs level order traversal logic
        we dont, need to add elements in a level and just the right most one
        '''
        if root is None:
            return self.result
        
        self.dfs(root,0)
        
        return self.result
        
    def dfs(self,root,level):
        #base
        if root is None:
            return 
        
        if len(self.result) == level:
            self.result.append(root.val)
            
        self.dfs(root.right, level+1)
        
        self.dfs(root.left, level+1)
        