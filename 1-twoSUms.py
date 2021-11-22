class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for each in range(0,len(nums)):
            if(target - nums[each] in hashMap):
                return[hashMap[target-nums[each]],each]
            hashMap[nums[each]] = each
        return []