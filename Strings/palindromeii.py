class Solution:
    def ispalin(self, s, l, r):
        while r >= l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while r >= l:
            if s[l] != s[r]:
                return (self.ispalin(s, l+1, r) or self.ispalin(s, l, r-1))
            l += 1
            r -= 1
        
        return True