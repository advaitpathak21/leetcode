class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for i in s:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
        
#         count = 0
        
#         for i in s:
#             if i == ')':
#                 if stack:
#                     if stack.pop() != '(':
#                         count += 1
#                 else:
#                     count += 1
#             else:
#                 stack.append(i)
        
#         if stack:
#             count += len(stack)
#         return count