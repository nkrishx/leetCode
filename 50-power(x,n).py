class Solution(object):
    # def helper(self, x , n):
    #     if n == 0:
    #         return 1
        
    #     temp = self.helper(x, n//2)
        
    #     if n%2 == 0:
    #         return temp * temp
    #     else:
    #         return temp * temp * x
        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        linear solution will be to iterate till the power and keep multiplying
        recurrsive solution will be to half the power and check for conditions
        and also we know that anything raised to 0 will be 1 and that will be our return 
        from the recursive stack
        if odd the multiply it with x
        if even no need to multiply
        if negative then multiply with 1/x
        '''
        # if n == 0:
        #     return 1
        
        # if n > 0:
        #     res = self.helper(x, n)
            
        # else:
        #     res = self.helper(1/x, -n)
            
        # return res

        #base
        if n == 0:
            return 1
        
        #logic
        temp = self.myPow(x, int(n/2))
        
        if n%2 == 0:
            return temp * temp
        else:
            if n<0:
                return temp * temp * (1/x)
            else:
                return temp * temp * x
            
        return
                
        