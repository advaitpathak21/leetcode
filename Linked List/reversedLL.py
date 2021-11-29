# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        stack = []
        total = 0
        
        while curr and curr.next:
            total += 1
            stack.append(curr)
            curr = curr.next
        head = curr
        start = curr
        
        while total:
            start.next = stack.pop()
            total -= 1
            start = start.next
        start.next = None
        
        return head