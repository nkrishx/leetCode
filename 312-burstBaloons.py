class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        n=len(nums)
        dp=[[0 for each in range(0,n)] for each in range(0,n)]
        
        for l in range(1,n+1):
            for i in range(0,n-l+1):
                j = i+l-1
                for k in range(i,j+1):
                    left = 1
                    right = 1
                    if i !=0:
                        left = nums[i-1]
                    if j !=n-1:
                        right = nums[j+1]
                    
                    before=0
                    after=0
                    if i!=k:
                        before = dp[i][k-1]
                    if j!=k:
                        after = dp[k+1][j]
                    
                    dp[i][j] = max(dp[i][j],(before+ (left*nums[k]*right) + after))
        
        return dp[0][n-1]
                    