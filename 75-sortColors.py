def swap(nums,i,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        2 poointer solution, works with 2 or 3 numbers, not more than that, might need counting sort
        we have 3 cases of num[i] being 0,1,2
        accordingly we push(swap) the elements to end or beginning
        '''
        if(len(nums) == 0):
            return []
        low = 0
        mid = 0
        high = len(nums)-1
        while(mid <= high):
            if nums[mid] == 0:
                swap(nums,mid,low)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(nums,mid,high)
                high -= 1
        return nums
        