class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        here we have another dimension to consider unlike the previous dp problems, the order as well
        so we remove this order dimesnion and convert into normal dp matrix problem (similar to house robber)
        we create an auxillary array with length till the max value + 1, this is to capture all indexes till the max value
        we know that we need to delete the nums[n]-1 and nums[n]+1 values from the array if we choose nums[n]
        eg : if we pick value 2 from [1,2,2,3], then we delete 1 and 3 since nums[n]-1 and nums[n]+1 is 1 and 3 respectively
        our aux array for this case would become [0,1,2,3] (length is 4, since max value + 1,
        we have two 2's hence the value for number 2 is 4 and similarly we have no 0's in the array and the value for '0' is 0)
        This above step is for the condition we need to delete nums[n]+1 and nums[n]-1 when we select nums[n]/
        Then we solve this similar to house robber looking at the previous skip and the take values.
        '''
        if(len(nums) == 0):
            return 0
        max_val = max(nums)
        aux_array = [0 for each in range(0,max_val +1)]
        
        for each in nums:
            aux_array[each] = aux_array[each]+each
        
        skip = 0
        take = aux_array[0]
        
        for each in aux_array[1:len(aux_array)]:
            
            temp = skip
            skip = max(skip, take)
            take = temp + each
            
        return max(skip, take)
        