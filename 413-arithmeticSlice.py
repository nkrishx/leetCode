class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        # for i in range(0,len(nums)-2):
        #     diff = nums[i+1] - nums[i]
        #     for j in range(i+1,len(nums)-1):
        #         if (nums[j+1] - nums[j]) == diff:
        #             count+=1
        #         else:
        #             break
        
        # dp = [0 for each in range(0,len(nums))]
        # for i in range(2,len(nums)):
        #     if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
        #         dp[i] = dp[i-1] + 1
        #         count += dp[i]
        
        previous = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                previous = previous + 1
                count += previous
            else:
                previous = 0
        
        return count