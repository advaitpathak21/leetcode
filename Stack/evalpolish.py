class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in tokens:
            if i in operators:
                n = stack.pop()
                n1 = stack.pop()
                if i == '+':
                    stack.append(n1 + n)
                elif t == '-':
                    stack.append(n1 - n)
                elif t == '*':
                    stack.append(n1 * n)
                elif t == '/':
                    stack.append(int(n1/n))
            else:
                stack.append(int(i))
        
            
        return stack.pop()