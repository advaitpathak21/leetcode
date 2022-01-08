class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # if str(x) == str(x)[::-1]:
        #     return True
        # return False
    
        left = 0
        x = str(x)
        right = len(x) - 1
        
        while right >= left:
            if x[left] != x[right]:
                return False
            right -= 1
            left += 1
        
        return True