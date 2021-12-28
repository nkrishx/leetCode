class Solution:
    '''
    dp solution
    bottom up approach,
    we know the last row,col has only 1 choice
    and we build bottom up from there using the logic
    dp[i][j] = dp of down + dp of right
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(0,n+1)] for j in range(0,m+1)]
        dp[m-1][n-1]=1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]