class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        the logic is that we move from left to right first and get the product for each number till nums[each-1] elements
        repeat the same for right to left and get the product for each number till nums[each+1] elements
        eg [1,2,3,4]
        forwar pass will be [1,1,2,6]  we add a 1 to 0th index since we are going to multiply the respective element with nack pass element
        back pass will be [24,12,4,1] same as above we add 1 ro the 0th index
        return_arr = [1*24,1*12,2*4,6*1] = [24,12,8,6]
        '''
        if(len(nums) == 0):
            return []
        
        result_arr = [0] * len(nums)
       
        result_arr[0] = 1
        running_prod = 1

        #forward pass, from left to right
        for each in range(1,len(nums)):
            running_prod = running_prod * nums[each-1]
            result_arr[each] = running_prod
            
        running_prod = 1
        
        #backward pass, from right to left, we make use of the result_arr already set in forward pass and directly multiply here
        for each in range(len(nums)-2,-1,-1):
            running_prod = running_prod * nums[each+1]
            result_arr[each] = result_arr[each] * running_prod
        
        return result_arr