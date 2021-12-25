class Solution:
    '''
    dfs or bfs wont work since we cannot distinctly tell if we are making a square 
    shape or not, hence we move diagonal downwards at each cell and keep dropping if we keep
    finding 1's (time limit exceeded)(commented)
    DP solution since repeated sub problems
    we create a dp array of same size as that of the input plus 1 extra row and colums of 
    zeros at the beginning to avoid exdge case code for first row and column elements
    '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        if m==0 or n==0:
            return 0
        
        maxvalue = 0
        dp=[[0 for i in range(0,n+1)] for j in range(0,m+1)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxvalue = max(maxvalue,dp[i][j])
                    
        return maxvalue*maxvalue
        
#         flag = False
#         for i in range(0,m):
#             for j in range(0,n):
#                 if matrix[i][j] == '1':
#                     flag = True
#                     current = 1
#                     while i+current <m and j+current<n and flag!=False:
#                         #at i+current and j+current index
#                         #check in same column if we have 0
#                         for k in range(i+current,i-1,-1):
#                             if matrix[k][j+current] =='0':
#                                 flag = False
#                                 break 
#                         #check in same row for 0
#                         for k in range(j+current, j-1,-1):
#                             if matrix[i+current][k] == '0':
#                                 flag = False
#                                 break
#                         if flag == True:
#                             current+=1
                
#                     maxvalue=max(maxvalue,current)
#         return maxvalue*maxvalue