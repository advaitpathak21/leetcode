class Solution:
    # @param A : string
    # @return an integer
    def ispalindrome(self, s):
        s = "".join(s)
        if s == s[::-1]: 
            return True
        return False
        
    def solve(self, A):
        A = list(A)
        if self.ispalindrome(A):
            return 0
        del A[0]
        return 1 + self.solve(A)