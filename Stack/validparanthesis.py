class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False
        stack = []
        inb = ['(','{','[']
        for i in range(len(s)):
            if s[i] in inb:
                stack.append(s[i])
            else:
                if stack:
                    x = stack.pop()
                    if s[i] == ')':
                        if x == '(':
                            continue
                        else:
                            return False
                    if s[i] == '}':
                        if x == '{':
                            continue
                        else:
                            return False
                    if s[i] == ']':
                        if x == '[':
                            continue
                        else:
                            return False
                else:
                    return False
        if not stack:    
            return True

########## OR #################
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False
        
        stack = []
        outb = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for i in s:
            if i in outb:
                if stack:
                    if stack.pop() == outb[i]:
                        continue    
                    else:
                        return False
                else:
                    return False
                
            else:
                stack.append(i)
        
        if not stack:
            return True