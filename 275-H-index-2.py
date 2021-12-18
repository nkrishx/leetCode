class Solution:
    '''
    since sorted we can use a binary search approach for better complexity
    h index is a value that can lie between 0-N where N is the length of the array
    if for any index if the value of citation at that index is equal then that is the 
    meeting point and we retuen that as the h index, if the value is lesser than the index 
    then we moved towards lower h index values (since array is in ascending order we move low to mid+1, right hand side has lesser h index values)
    else we move towards left side which has higher h index values.
    The h index values are the difference between the length and the current index
    [0,1,2,5,6] -> h index array would be [5,4,3,2,1]
    '''
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        
        if n==0:
            return 0
        
        low = 0
        high = n-1
        
        while(low<=high):
            mid = low +(high-low)//2
            
            if citations[mid]==n-mid:
                return n-mid
            elif citations[mid] < n-mid:
                low = mid+1
            else:
                high = mid-1
                
        return n-low
        
        