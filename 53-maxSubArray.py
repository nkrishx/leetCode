class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        curr=nums[0]
        maxVal=nums[0]
        
        for i in range(1,len(nums)):
            curr=max(curr+nums[i],nums[i])
            maxVal =max(maxVal,curr)
            
        return maxVal