# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        '''
        can be done using both DFS and BFS
        we use an extra size(level) variable to know the current level of the tree
        '''
        if root is None:
            return
        self.dfs(root,0) #start at level 0
        return self.result
        
    def dfs(self, root, level):
        #base
        if root is None:
            return
        
        #logic
        if level == len(self.result):
            self.result.append([]) #if first time we encounter an element on a level 
                              #set an empty list to append into
        
        self.result[level].append(root.val)
        
        self.dfs(root.left, level+1)
        
        self.dfs(root.right, level+1)