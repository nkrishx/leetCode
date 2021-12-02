# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        idea is that we use 2 pointers and move 1 at 1x speed and the otehr at 2x
        so if the linkedlist is circular the there will be a point when the 2 meet.
        To find out the head of the linked list we reset any one of the pointer and 
        move both of them at 1x until they meet. 
        Generic solution can be applied to any circularly connected linear data structure
        '''
        slow = head
        fast = head
        circular = False
        while(fast != None and fast.next != None ) :
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                circular = True
                break
        
        if circular == False:
            return 
        
        slow = head #this is for finding the head of the list, can set either fast or slow
        
        while(slow != fast):
            slow = slow.next
            fast = fast.next
            
        return slow #return any of the pointers