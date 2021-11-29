class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums) == 0):
            return []
        result = []
        #get each number and the index where it has to be,
        #we know that numbers run between 1 to n and the index would 
        #be number-1 since starting from 1
        #a negative number at index means we have visited that number 
        #and don't want to mark it visited again, hence checking if number is neagtive
        for each in range(0,len(nums)):
            index = abs(nums[each]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        for each in range(0,len(nums)):
            if nums[each] > 0:
                result.append(each+1)
            else:
                nums[each]*=-1 #since we mutate the original array we set it back here
        
        return result
        
        