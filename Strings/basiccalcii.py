class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = ""
        sign = '+'
        for i in s+'+':
            if i not in "+-/* ":
                curr += i
            elif i in "+/-*":
                if sign == '+':
                    stack.append(int(curr))
                if sign == '-':
                    stack.append(-(int(curr)))
                if sign == '*':
                    stack.append(stack.pop() * int(curr))
                if sign == '/':
                    stack.append(int(stack.pop() / int(curr)))
                sign = i
                curr = ""
        return sum(stack)

# class Solution:
#     def calculate(self, s: str) -> int:
#         opd = []
#         opt = []
#         res = 0
#         curr = ""
#         for i in s:
#             if i not in "+-/* ":
#                 curr += i
#             if i in "+/*":
#                 opt.append(i)
#                 opd.append(curr)
#                 curr = ""
#             if i == "-":
#                 opt.append('+')
#                 opd.append(curr)
#                 curr = ""
#                 curr += i
#         opd.append(curr)

#         if not opt:
#             return int(s)
        
#         while opt:
#             i = opt.pop()
#             a = int(opd.pop())
#             b = int(opd.pop())
#             # print(a, b, i)
#             if i == '+':
#                 x = (b + a)
#             elif i == '-':
#                 x = (b - a)
#             elif i == '/':
#                 x = int(b/a)
#             elif i == '*':
#                 x = (b*a)
#             opd.append(x)
#         res = opd.pop()
#         return int(res)