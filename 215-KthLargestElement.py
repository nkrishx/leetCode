class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        heap solution
        heapq.nlargest returns the mentioned number
        of largest elements in descending order
        '''
        return heapq.nlargest(k,nums)[-1]
        