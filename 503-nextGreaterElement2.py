class Solution:
    '''
    we iterate 2*n times since we want cyclic iteration on the same list
    '''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        n=len(nums)
        result=[-1 for i in range(0,n)]
        stack=[]
        
        for i in range(0,2*n):
            while len(stack)!=0 and nums[stack[-1]]<nums[i%n]:
                index=stack.pop()
                result[index]=nums[i%n]
            
            # if i<n:
            stack.append(i%n)
            
        return result
            