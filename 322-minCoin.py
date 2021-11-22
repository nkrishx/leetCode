# def recursiveBruteForce(coins, amount, index, minCoinCount):
#     #return logic
#     if(amount == 0):
#         return minCoinCount
#     if(index == len(coins) or amount < 0):
#         return -1
    
#     #choose the coin
#     choice1 = recursiveBruteForce(coins, amount-coins[index], index, minCoinCount+1)
    
#     #dont choose the coin
#     choice2 = recursiveBruteForce(coins, amount, index+1, minCoinCount)
    
#     if(choice1 == -1):
#         return choice2
#     if(choice2 == -1):
#         return choice1
#     return min(choice1,choice2)
    
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         # recursive/brute force, time limit exceeds
#         if(len(coins) == 0):
#             return 0
#         index = 0
#         minCoinCount = 0
#         minimum = recursiveBruteForce(coins, amount, index, minCoinCount) #(coins, amount, index, minCoinCount)
#         return minimum

class Solution:
    
    def coinChange(self, coins, amount):
        
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        
        for j in range(amount+1):
            dp[0][j] = 99999  # large number instead of max int value to avaoid overflow
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if coins[i-1]>j: # taking i-1 since in the dp matrix we have 0,0 row and column extra,
                    dp[i][j] = dp[i-1][j] # and till the value is less we use the value at the top of it [i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]]) #if not find the min between top and 1+value at denomination of coin 
                                                                        #1+dp[i][j-coins[i-1]]
        
        if dp[i][j] != 99999:
            return dp[i][j] #return the last index of the matrix
        else:
            return -1