class Solution:
    res = ""
    def retain(self, a):
        b = a % 2
        new = a // 2
        if new != 0:
            self.res += (str(b))
            self.retain(new)
        return self.res[::-1]
        
    def addBinary(self, a: str, b: str) -> str:  
        a = int(a) + int(b)
        return self.retain(a)  
        