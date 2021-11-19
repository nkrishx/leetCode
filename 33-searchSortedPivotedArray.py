class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums) == 0) :
            return -1
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low + (high-low)/2
            if(nums[mid] == target):
                return mid
            elif(nums[low]<=nums[mid]): #left side sortd
                if(nums[low] <= target and nums[mid]>target):
                    high = mid -1
                else:
                    low = mid + 1
            else: #right side sortd
                if(nums[mid] < target and nums[high] >= target):
                    low = mid + 1
                else :
                    high = mid -1
        return -1
        