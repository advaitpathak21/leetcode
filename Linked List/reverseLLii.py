# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        new = ListNode()
        start = new
        head1 = head
        l = 0
        stack = []
        while head:
            l += 1
            if left <= l <= right:
                stack.append(str(head.val))
            head = head.next
        l = 0
        head = head1
        while head:
            l += 1
            if left <= l <= right:
                new.next = ListNode(stack.pop())
            else:
                new.next = ListNode(head.val)
            new = new.next
            head = head.next
            
        return start.next