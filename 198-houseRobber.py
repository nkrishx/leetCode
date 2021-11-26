class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        we do this based on the below matrix logic for a sample array [0,1,1,2]. Dynamic Problem.
         skip take
        0 0  , nums[0] = 0
        1 max(previous skip,previous take) = 0 , 1+previous skip = 1
        1 max(1,1) = 1 , 1 + 0 = 1
        2 max(1,1) = 1,  2 + 1 = 3
        return max(skip,take)
        '''
        if(len(nums) == 0):
            return 0
        skip = 0
        take = nums[0]
        for each in range(1,len(nums)):
            temp = skip
            skip = max(skip,take)
            take = nums[each] + temp
        return max(skip,take)