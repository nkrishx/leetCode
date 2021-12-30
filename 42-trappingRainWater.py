class Solution:
    '''
    4 pointers solution
    pairs of pointers on left and right side are made and moved
    '''
    def trap(self, height: List[int]) -> int:
        if len(height) <2:
            return 0
        
        #lw and rw are values and not indexes,
        #they are paired with respective left and righ pointers to calculate the result
        lw=0
        rw=0 
        l=0
        r=len(height)-1
        result=0
        
        while(l<=r):
            #check which side to process
            #we can only process a side if it is equal to or greater than the 
            #other side wall 
            if lw<=rw:
                #process left side
                if height[l]<lw:
                    result=result+lw-height[l]
                else:
                    lw=height[l]
                l+=1
            else:
                #process right side
                if height[r]<rw:
                    result=result+rw-height[r]
                else:
                    rw=height[r]
                r-=1
        
        return result