# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getint(self, a: List):          # String to int
        a_string = "". join(a)
        an_int = int(a_string)
        return (an_int)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:          
        a = []
        b = []
        i = 0
        while l1 or l2:
            a.append(str(l1.val)) if l1 else 0
            b.append(str(l2.val)) if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        an = self.getint(a[::-1])       # Reverse the numbers for addition
        bn = self.getint(b[::-1])
        
        res = an + bn
        res = str(res)                  # Create a string so that it can be iterated
        
        total = len(res) - 1
        
        new = ListNode()
        head = new
        while total >= 0:
            new.next = ListNode(res[total])
            total -= 1
            new = new.next
            
        return head.next