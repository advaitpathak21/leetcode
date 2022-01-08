class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        pos = 0
        for c in s:
            if c == '(':
                stack.append([c, pos])
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    continue
            res.append(c)
            pos += 1
                
        while stack:
            c, x = stack.pop()
            res.pop(x)
        return ("".join(res))        