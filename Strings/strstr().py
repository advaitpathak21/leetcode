class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or needle == haystack:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i : i + len(needle)] == needle:
                    return i
            return -1
            
            
            
#         flag = 0
#         start = 0
#         res = []
#         if needle == "" or needle == haystack:
#             return 0
#         if needle not in haystack:
#             return -1
#         else:
#             while start < len(haystack):
#                 if haystack[start] != needle[flag]:
#                     flag = 0
#                     if res:
#                         start = res[0] + 1
#                         res = []
#                 if haystack[start] == needle[flag]:
#                     flag += 1
#                     res.append(start)
#                 if flag == len(needle):
#                     return res[0]
#                 start += 1
                    
#             if flag == len(needle):
#                 return res[0]
#             else:
#                 return -1