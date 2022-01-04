class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIndexFront=0
        maxIndexFront=0
        
        if len(nums)==1:
            return 1
        
        if nums[0]<nums[1]:
            minIndexFront=0
            maxIndexFront=1
        else:
            maxIndexFront=0
            minIndexFront=1
            
        for i in range(2,len(nums)):
            if nums[i]<nums[minIndexFront]:
                minIndexFront=i
            if nums[i]>nums[maxIndexFront]:
                maxIndexFront=i
        
        minIndexBack=len(nums)-1-minIndexFront
        maxIndexBack=len(nums)-1-maxIndexFront
        
        print(minIndexFront)
        print(minIndexBack)
        print(maxIndexFront)
        print(maxIndexBack)
        
        return min(max(minIndexFront,maxIndexFront)+1,
                  max(minIndexBack,maxIndexBack)+1,
                   minIndexFront+1+maxIndexBack+1,
                   maxIndexFront+1+minIndexBack+1
                  )