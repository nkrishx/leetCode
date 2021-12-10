class Solution(object):
    
    def backTrack(self,candidate,index,path,target):
        #base
        if index >=len(candidate) or target <0:
            return
        
        if target == 0:
            #we deepcopy the path since we backtrack we pop out the added elements
            self.result.append(deepcopy(path))
            return
        
        #logic
        #dont choose case
        self.backTrack(candidate,index+1,path,target)
        
        #choose case
        #action
        path.append(candidate[index])
        #recurse
        self.backTrack(candidate,index,path,target-candidate[index])
        #backtrack pop
        path.pop()
        
        
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        can be done using recurssion, but we need to remember that
        every recursive call will need a new copy of the path chosen,
        if not then the same path container will get updated for all nodes visited.
        This can be avoided by backtracking solution, backtracking is same as recursion
        but with the extra step of removing the element we added into path before stating the 
        recursive call.
        Same idea of choose an element, dont choose an element
        backtracking solutions are of structure - action, recurse, backtrack
        '''
        
        self.result = []
        self.backTrack(candidates,0,[],target)
        return self.result