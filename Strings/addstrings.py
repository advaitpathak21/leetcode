class Solution:
    def giveval(self, val):
        a = ord(val) - 48
        return a
    
    def giveint(self, length, numarr):
        res = 0
        multiplier = 1
        while length >= 0:
            res += multiplier*self.giveval(numarr[length])
            multiplier = multiplier*10
            length -= 1
        return res
    
    def addStrings(self, num1: str, num2: str) -> str:
        a, b = 0, 0
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        
        a = self.giveint(len1, num1)
        b = self.giveint(len2, num2)
        
        return str(a+b)