class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        res = 0
        
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[i])
            res = max(len(hashset), res)
                
        return res

#### My try below

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         haset = set()
#         s = list(s)
#         res = 0
        
#         for i in s:
#             profit = 0
#             if i in haset:
#                 profit = len(haset)                
#                 haset.remove(i)
#             haset.add(i)
                
#             res = max(profit, res, len(haset))
            
#         return res