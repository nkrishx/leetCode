class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        
        for i in range(0,len(nums)):
            if nums[i] in hashMap and abs(hashMap[nums[i]] - i) <= k :
                return True
            hashMap[nums[i]] = i
        return False
                