class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n == 1: return x 
        def helper(x, n):
            print("helper:",x , n)
            if n == 1: return x
            
            res = helper(x, n//2)
            res = res * res
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n > 1 else (1 / res)