class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        nums.sort()
        maxSum=0
        
        for i in range(0,len(nums),2):
            maxSum=maxSum+nums[i]
        
        return maxSum