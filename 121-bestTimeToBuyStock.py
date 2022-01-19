class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = sys.maxsize
        
        for i in range(0,len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > profit:
                profit = prices[i] - minPrice
        
        return profit