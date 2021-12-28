class Solution:
    '''
    dp solution, in the dp array we construct we 
    append the max sum possible at that particular index and use this value for
    all elements further in the array
    '''
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if len(arr)==0:
            return 0
        
        n=len(arr)
        dp=[0]*n
        
        for i in range(0,n):
            maxvalue = arr[i]
            for j in range(1,k+1):
                #get max in the current partiton
                if i-j+1 >=0:
                    maxvalue = max(maxvalue,arr[i-j+1])
                    if i-j >=0:#fill current dp[i] value
                        #we know that we have k partition and for 
                        #each k we would have already had a dp[i] value
                        #hence max between them should be filled
                        dp[i] = max(dp[i],dp[i-j]+maxvalue*j)
                    else:
                        dp[i] = max(dp[i],maxvalue*j)
        return dp[n-1]