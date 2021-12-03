# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''2 pointer, find out the max len between the 2 
        and move one pointer till equidistant 
        then check until they become same'''
        lenA = 0
        lenB = 0
        curr = headA
        while(curr != None):
            curr = curr.next
            lenA += 1
        curr = headB
        while(curr != None):
            curr = curr.next
            lenB += 1
            
        while(lenA > lenB):
            headA = headA.next
            lenA -= 1
            
        while(lenB > lenA):
            headB = headB.next
            lenB -= 1
            
        while(headA != headB):
            headA = headA.next
            headB = headB.next
        
        if headA != headB:
            return None
        
        return headA #return either