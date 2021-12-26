class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
            
        dp = [0]*(len(s)+1)
        flag = False
        dp[0] = True
        
        
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
                    
                    
        return dp[-1]
                    
        