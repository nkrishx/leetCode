class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if(len(coins) ==0):
            return 0
        rows = len(coins) + 1
        columns = amount + 1
        dp = [[0] * columns] * rows
        
        for each in range(0,len(dp)):#each row first col value will be 1 since we can make value0 
            dp[each][0] = 1        #by not choosing that coin, so there is 1 way
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if(j<coins[i-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[len(dp)-1][len(dp[0])-1]
        
        
        