class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        2 pointers move slow pointer only when we enoucter a 
        different value between nums[slow] and nums[fast],
        if not then keep incrementing the fast pointer
        '''
        if(len(nums) == 0):
            return 0
        slow = 1
        count = 1
        for fast in range(1,len(nums)):
            if nums[fast] == nums[fast-1]:
                count += 1
            else:
                count = 1   
            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1
        return slow
            
                