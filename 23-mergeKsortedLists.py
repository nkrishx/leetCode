# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        magic method for lesser than
        comparing 2 nodes values
        using min heap
        '''
        ListNode.__lt__ = lambda x, y: x.val < y.val
        
        result = ListNode(-1)
        dummy = result
        
        min_heap = []
        
        for li in lists:
            if li:
                heapq.heappush(min_heap, li)
            
        while min_heap:
            curr = heapq.heappop(min_heap)     
            dummy.next = curr
            dummy = dummy.next
            if curr.next:
                heapq.heappush(min_heap, curr.next)
            
        return result.next
        