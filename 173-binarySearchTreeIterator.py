# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
the idea is that we need to control the recurssion occuring,
while in validating a BST we did a inorder traversal on the left of each and also on the right
but here we will not do the right, we will give out the top of the stack as the next element when called. And to check if hasNext we check if stack is empty or not.
We use a physical stack here. 
Iterators basic idea is that it only needs to know about the next element, hence we control the right side.
'''
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.dfs(root)

    def next(self):
        """
        :rtype: int
        """
        returnVal = self.stack.pop()
        self.dfs(returnVal.right)
        return returnVal.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if(len(self.stack) != 0):
            return True
        else:
            return False
            
    def dfs(self,root):
        while(root != None): #loop for putting all left elements into stack
            self.stack.append(root)
            root = root.left
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()