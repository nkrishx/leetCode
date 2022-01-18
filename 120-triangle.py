class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        
        dp = [0 for each in range(0,len(triangle[-1]))]
        #fill in the last row values
        for i in range(0,len(dp)):
            dp[i] = triangle[-1][i]
            
        #print(dp)
            
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
                
        return dp[0]
        
#         sumValue = triangle[0][0]
        
#         for i in range(0,len(triangle)-1):
#             minValue = sys.maxsize
#             for j in range(0,len(triangle[i])):
#                 minValue = min(minValue,min(triangle[i+1][j],triangle[i+1][j+1]))
#             sumValue = sumValue+minValue
        
#         return sumValue
        
        