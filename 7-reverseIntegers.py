class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        reverse=0
        while x!=0:
            reverse=reverse*10+abs(x)%10
            x=int(x/10)
       
        if reverse < -2**31 or reverse > 2**31 -1 :
            return 0
        else:
            if temp<0:
                return reverse*-1
            else:
                return reverse
        