class Solution:
    '''
    using binary search to find the closest element for the given element
    slight modification from the normal binary search framework
    we know that the given input is sorted, so if we find the closest element then
    we know the elements on either side will be greater in difference than that of the closest
    we compare among these 2 and move pointers accordingly
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 0 or arr is None:
            return []
        result = []
        closest = self.binarySearchClosest(arr,x)
        result.append(arr[closest])
        left = closest-1
        right = closest+1
        while k > 1: #since we already added the closest element into the result above from BS
            print("{}{}".format(result,k))
            if left<0: #we have moved till the last element on the left so only choice is to add elements from the right
                result.insert(len(result),arr[right])
                right +=1
            elif right == len(arr): #we have moved out of bounds on the right side and hence only option is to add left elements
                result.insert(0,arr[left])
                left -=1
            else: #we compare here left or right is greater and move accordingly
                if x-arr[left] > arr[right]-x:
                    result.insert(len(result),arr[right])
                    right +=1
                else:
                    result.insert(0,arr[left])
                    left -=1
            k -=1
        return result
    
    def binarySearchClosest(self,arr, target):
        low = 0
        high = len(arr)-1
        while low<high:
            mid = low+(high-low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid
            else:
                low = mid+1
        if low==0: #for cases we have negative target element and the closest might be the first element of the list
            return low
        if abs(arr[low]-target) < abs(arr[low-1]-target):
            return low
        return low-1

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         low = 0
#         high = len(arr) - k
#         res = []
#         index = self.binarySearch(arr, low, high, k, x)
#         for i in range(index, index + k):
#             res.append(arr[i])
            
#         return res
    
#     def binarySearch(self, arr, low, high, k, x):
#         while low <= high:
#             first = low  + (high - low)//2 
#             last = first + k - 1
#             if (first>0 and (x - arr[first - 1]  <= arr[last] - x)):
#                 high = first - 1
#             elif (last < len(arr) - 1 and (x - arr[first] > arr[last + 1] - x)):
#                 low = first + 1
#             else:
#                 return first
            
#         return low
    
                    
                
                
            