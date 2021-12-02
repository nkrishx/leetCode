# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        recursive solution
        '''
        if(head == None or head.next == None):
            return head
        
        reverse = self.reverseList(head.next)
        head.next.next = head #point the current head.next to the current head
        head.next = None #break the connection of current head to head.next
        return reverse
        