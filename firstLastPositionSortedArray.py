def bsFirst(nums,target):
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low+(high-low)/2
            if(nums[mid]==target):
                if(mid == 0 or nums[mid]>nums[mid-1]):
                    return mid
                else:
                    high = mid - 1
            elif(target < nums[mid]):
                high = mid -1
            else:
                low = mid+1
        return -1
    
def bsLast(nums,target):
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low+(high-low)/2
            if(nums[mid]==target):
                if(mid == len(nums)-1 or nums[mid+1]>nums[mid]):
                    return mid
                else:
                    low = mid + 1
            elif(target < nums[mid]):
                high = mid -1
            else:
                low = mid+1
        return -1
    
class Solution(object):
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums) == 0):
            return [-1,-1]
        if(nums[0]>target or nums[len(nums)-1] < target ):
            return [-1,-1]
        first = bsFirst(nums,target)
        if(first == -1):
            return [-1,-1]
        last = bsLast(nums,target)
        return [first,last]
        