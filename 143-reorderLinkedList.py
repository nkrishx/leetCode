# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLinkedList(head):
    if(head == None or head.next == None):
        return head
    reverse = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return reverse
    
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        '''combination of 3 problems
        find middle, reverse the right part and merge them both'''
        
        #find middle
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None): 
            #condition for handling even and odd len lists
            slow = slow.next
            fast = fast.next.next
            
        #reverse the list
        fast = reverseLinkedList(slow.next) #will return the revered head of the right side
        
        #reset the slow.next since it points to the mid.next element
        slow.next = None
        
        #set slow to head now
        slow = head
        
        #the split list will be of same size or the right side will be smaller than left
        while(fast != None):
            temp = slow.next
            slow.next = fast
            fast = fast.next
            slow.next.next = temp
            slow = temp