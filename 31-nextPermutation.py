class Solution:
    '''
    3 step solution
    iterate from behind to find a breach, a breach is where a[i] <= a[i+1]
    swap where breached with next greater elememnt from the back
    reverse all elements from a[i+1] to end
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=n-2
        j=n-1
        
        #breach
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        
        #swap
        if(i>=0):
            while(nums[i]>=nums[j]):
                j-=1
            self.swap(nums,i,j)
        
        #reverse
        self.reverse(nums,i+1,n-1)
            
    def swap(self,nums,i,j):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        
    def reverse(self,nums,l,r):
        while(l<=r):
            self.swap(nums,l,r)
            l+=1
            r-=1
            