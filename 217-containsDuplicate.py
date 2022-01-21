class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        
        for i in range(0,len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i  
        
        return False