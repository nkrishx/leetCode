# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        2 pointers starting from the head,
        we move one of the pointer till we create a gap of n
        Once done we move until the first pointer hits null
        then set the other pointer.next = pointer.next.next
        We start with a dummy pointer since there are cases that we
        need to remove the head pointer itself
        '''
        dummy = ListNode(0) #dummy pointer and point its next to head
        dummy.next = head
        slow = dummy
        fast = dummy
        count = 0
        
        while(count <= n):
            fast = fast.next
            count += 1
        
        while(fast != None):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
        