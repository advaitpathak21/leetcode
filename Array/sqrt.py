class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Babylonian method
        if x <= 1: return x
        
        r = 0.5 * x
        diff = 1
        while diff > 0.01:
            new_r = 0.5 * (r + x/r)
            diff = abs(new_r - r)
            r = new_r
        
        return int(new_r)
        
        # Exponent method
        return int(pow(x, 0.5))