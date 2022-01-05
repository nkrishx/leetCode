class Solution:
    '''
    traverse from behind
    '''
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        destination=n-1
        
        if len(nums)<2:
            return True
        
        for i in range(n-2,-1,-1):
            if nums[i]+i >= destination:
                destination=i
        
        if destination==0:
            return True
        