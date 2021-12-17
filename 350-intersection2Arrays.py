# class Solution:
#     '''
#     hashMap solution
#     take smaller array as hashmap, iterate through the bigger one
#     hashmap has the nuber and the frequency of the number
#     reduce frequency when we see the number in the other array
#     ''' 
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         m = len(nums1)
#         n = len(nums2)
        
#         if m == 0 or n ==0: 
#             return []
        
#         #considering 1st as small and 2nd as big
#         if m > n:
#             return self.intersect(nums2, nums1)
        
#         mapp = {}
        
#         for each_val in nums1:
#             if each_val not in mapp:
#                 mapp[each_val] = 0
#             mapp[each_val] += 1
            
#         res = []
        
#         for each_val in nums2:
#             if each_val in mapp:
#                 mapp[each_val] -= 1
#                 res.append(each_val)
#                 if mapp[each_val] == 0:
#                     del mapp[each_val]
        
#         return res

# class Solution:
#     '''
#     2 pointer solution, we need to sort the arrays first
#     '''
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if len(nums1)==0 or len(nums2)==0:
#             return []
#         result = []
#         n1 = len(nums1)
#         n2 = len(nums2)
        
#         nums1.sort()
#         nums2.sort()
        
#         p1= 0
#         p2 =0
        
#         while p1<n1 and p2<n2:
#             if nums1[p1]==nums2[p2]:
#                 result.append(nums1[p1])
#                 p1+=1
#                 p2+=1
#             elif nums1[p1] < nums2[p2]:
#                 p1+=1
#             else:
#                 p2+=1
        
#         return result

class Solution:
    '''
    here we use binary search to check 
    for each element in array smaller among the 2 array inputs
    in the binary seacrh function we need to ensure that
    if we find the element in the larger array then we need
    to return the left most occurance of it, and permenantely set
    the low pointer to occurance+1 index and we skip checking for 
    next element in the smaller array until the occurance index.
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)==0 or len(nums2)==0:
            return []
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        #check which is larger in size, we will work with n1 as smaller one
        if n1>n2:
            self.intersect(nums2,nums1)
        
        low = 0
        high = len(nums2)-1
        
        result = []
        
        nums1.sort()
        nums2.sort()
        
        for each in nums1:
            bs = self.binarySearch(nums2,each,low,high)
            if bs != -1:
                low = bs+1
                result.append(each)
        
        return result
    
    def binarySearch(self,nums,target,low,high):
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                #we need to give out the left most occurance of the target
                if mid ==low or nums[mid] >nums[mid-1]:
                    return mid
                else:
                    high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1
            