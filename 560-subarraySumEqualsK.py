class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        rsum = 0
        count = 0
        hashMap = {0:1} # we store running sum and number of occurances
        for each in nums:
            rsum = rsum + each
            difference = rsum - k
            if(difference in hashMap):
                count = count + hashMap[difference]
            if(rsum in hashMap):
                hashMap[rsum] = hashMap[rsum]+1
            else:
                hashMap[rsum] = 1
                
        return count