"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        curr = head
        #make copies and connect them side by side
        #1->1'->2->2`->... where 1 is current and 1` is the copy of it (currCopy)
        while(curr != None):
            currCopy = Node(curr.val)
            currCopy.next = curr.next
            curr.next = currCopy
            curr=curr.next.next
            
        curr = head
        #set the random pointers here
        while(curr != None):
            if curr.random != None:
                curr.next.random = curr.random.next
            curr=curr.next.next
            
        
        curr=head
        currCopy=curr.next
        copyHead=head.next
        #we need to seprate the linking of 1->1`->2->2` to 1->2->... 
        #and 1`->2`->...
        while(curr!=None):
            curr.next = curr.next.next
            if currCopy.next!=None:
                currCopy.next=currCopy.next.next
            curr=curr.next
            currCopy=currCopy.next
            
        return copyHead
            
        