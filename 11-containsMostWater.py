class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        2 pointer solution
        the constraining factor for area is the lower height amoung the 2 points 
        we consider at any time, so we calculate the area with respect to those points
        and move low or high pointer depending on which is lesser
        '''
        if(len(height) == 0):
            return 0
        low = 0
        high = len(height)-1
        maximum = 0
        for each in range(0,len(height)-1):
           # area = min(height[low],height[high])*(high -low)
            maximum = max(maximum,min(height[low],height[high])*(high -low))
            
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return maximum
        