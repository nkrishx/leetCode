class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) ==0):
            return 0
        count = 0
        # palindromeContainer = []
        palindromeContainer = set()
        for each in s:
            if(each in palindromeContainer):
                count +=2
                palindromeContainer.remove(each)
            else:
                palindromeContainer.add(each)
        if(len(palindromeContainer)!= 0):
            count +=1
        return count