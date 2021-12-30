class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        
        n = len(nums)
        
        if k>=n:
            k = k%n
            
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        
    def reverse(self,nums,l,r):
        while(l<r):
            self.swap(nums,l,r)
            l+=1
            r-=1
    
    def swap(self,nums,l,r):
        temp=nums[l]
        nums[l]=nums[r]
        nums[r]=temp