class Solution:
    '''
    binary search solution on the smallest array
    here we donot search any element but try to partition the arrays
    so the mid of the binary search gives us a partion value on the smaller array,
    using that we calcuate where we should partition on the larger array.
    the formula is (n1+n2)/2 - partitionX (paritionX is the mid of the binary search)
    Next we look at edge cases and conditions to move the low and high pointers of the BS
    conditions l1<=r1, l2<=r2, l2<=r1 if not then low=partition X+1, l1<=r2 if not then high=partitionX+1
    if partitionX ==0 then l1=-ve infinity 
    if partitionX ==len(n1) r1=+ve infinity
    if partitionY ==0 l2=-ve infinity
    if partititonY ==len(n2) l2=+ve infinity
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m == 0 and n == 0:
            return 0
        
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0
        high = m
        
        while low <= high:
            partX = low + (high - low)//2
            
            partY = (m+n)//2 - partX
            
            l1 = -2**32 if partX == 0 else nums1[partX-1]
            r1 = 2**32-1 if partX == m else nums1[partX]
            l2 = -2 ** 32 if partY == 0 else nums2[partY-1]
            r2 = 2 ** 32 -1 if partY == n else nums2[partY]
            
            if l1 <= r2 and l2 <= r1:
                #even
                if (n + m)%2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                #odd
                else:
                    return min(r1,r2)
                
            elif l2 > r1:
                low = partX + 1
            else:
                high = partX - 1
            
        return 1