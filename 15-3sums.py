class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        2 pointer solution
        '''
        if(len(nums) == 0):
            return []
        nums.sort()
        result = []
        for each in range(0,len(nums)-2):
            if nums[each] > 0:
                break
            if each>0 and nums[each] == nums[each - 1]:
                continue
            low = each + 1
            high = len(nums)-1
            while(low < high):
                s = nums[each] + nums[low] + nums[high]
                if s == 0:
                    result.append([nums[each],nums[low],nums[high]])
                    high -= 1
                    low += 1
                    while(low < high and nums[low] == nums[low - 1]):
                        low += 1
                    while(low < high and nums[high] == nums[high + 1]):
                        high -= 1
                elif s > 0:
                    high -= 1
                else:
                    low += 1
        return result
        