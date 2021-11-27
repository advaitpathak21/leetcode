class Solution:
    def firstUniqChar(self, s: str) -> int:
        hamap = {}
        
        for i in s:
            if i in hamap:
                hamap[i] += 1
            else:
                hamap[i] = 1
        
        for i,val in enumerate(s):
            if hamap[val] == 1:
                return i
        return -1
