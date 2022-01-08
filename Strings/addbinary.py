class Solution:
    def DtoB(self, num):
        res = ""
        if num == 0: return "0"
        while num > 0:
            d = num % 2
            res += str(d)
            num = num //2
        return (res[::-1])
        
    def bin(self, s):
        r = len(s) - 1
        num, pos = 0, 0
        while r >= 0:
            if s[r] == '1':
                k = pow(2, pos)
                num += k
            pos += 1
            r -= 1
        return num
        
    def addBinary(self, a: str, b: str) -> str:
        a_n = self.bin(a)
        b_n = self.bin(b)
        
        return self.DtoB(a_n + b_n) 