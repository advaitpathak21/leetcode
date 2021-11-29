# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr, prev = head, head
        hashset = set()
        hashset.add(curr.val)
        curr = curr.next
        while curr:
            if curr.val not in hashset:
                hashset.add(curr.val)
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
            
        return head                