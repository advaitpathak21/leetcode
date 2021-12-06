# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        oddptr = curr = head
        evenptr = evenhead = head.next
        i = 1
        
        while curr:
            if (i>2) and (i%2 == 0):
                evenptr.next = curr
                evenptr = curr
            elif (i>2) and (i%2 != 0):
                oddptr.next = curr
                oddptr = curr
            curr = curr.next
            i += 1
        
        evenptr.next = None
        oddptr.next = evenhead
    
        return head