# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    can be done using recursive and itrative approach,
    iterative approach has no extra space as that in recursive
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # return root
        while(root):
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        