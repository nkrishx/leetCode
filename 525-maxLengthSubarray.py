class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rsum = 0
        maxValue = 0
        hashMap = {0:-1} #in the hash map we will map rsum:index, {0:-1} for initial edge case of [1,0] 
        if(len(nums) == 0):
            return 0        
        for each in range(0,len(nums)):
            if(nums[each] == 0):
                rsum = rsum + 1
            else:
                rsum = rsum - 1
            if(rsum in hashMap):
                maxValue = max(maxValue,each-hashMap[rsum])
            else:
                hashMap[rsum] = each
        return maxValue