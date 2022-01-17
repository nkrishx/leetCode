class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for each in range(0,n+1)] for val in range(0,k+1)]
        
        for each in range(1,n+1):
            dp[1][each] = each
        
        for i in range(2,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = sys.maxsize
                for f in range(1, j+1):
                    dp[i][j] = min(dp[i][j],1+max(dp[i-1][f-1], dp[i][j-f]))
                    
        return dp[k][n]