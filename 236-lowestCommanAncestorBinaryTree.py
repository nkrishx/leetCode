# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    since its not a BST, we cannout use the bst properties,
    hence we create a path to the element of intrest.
    We also add the elememnt if found twice, this is to avoid finisding out
    which is the shorter path array and then itreate over it.
    Now we can just return the i-1 element when there is no match since till i-1 we 
    have seen a match
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1=[]
        path2=[]
        self.backTrack(root,p,path1)
        self.backTrack(root,q,path2)
        for i in range(0,len(path1)): #can be either path1 or 2
            if path1[i] != path2[i]:
                return path1[i-1]
        return None
    
    def backTrack(self, root,p,path):
        #base
        if root == None:
            return
        if root == p:
            path.append(p)
            path.append(p)
            return
        
        #logic
        #action
        path.append(root)
        #recurse
        self.backTrack(root.left,p,path)
        self.backTrack(root.right,p,path)
        if path[len(path)-1] == p:
            return
        #backtrack
        path.pop()