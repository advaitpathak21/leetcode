class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

### Solution 2
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         while head:
#             if head.val == 'x':
#                 return True
#             head.val = 'x'
#             head = head.next
        
#         return False