class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i=0
        j=len(x)-1
        
        while i<=len(x)-1 and j >=0:
            if x[i] != x[j]:
                return False
            i+=1
            j-=1
        return True