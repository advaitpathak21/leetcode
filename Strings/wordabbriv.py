class Solution:    
    def giveint(self, c, flag):
        multiplier = pow(10, flag)
        a = ord(c) - 48
        return (a*multiplier)
        
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        lenab = len(abbr) - 1
        lenw = len(word) - 1
        count = 0
        flag = 0
        fprev = 0
        while lenab >= 0:
            if not abbr[lenab].isdigit():
                if fprev == 1:
                    return False
                if abbr[lenab] == word[lenw - count]:
                    count += 1
                    flag = 0
                else: return False
            else:
                a = self.giveint(abbr[lenab], flag)
                if a == 0:
                    fprev = 1
                if flag:
                    if count == count + a:
                        return False
                    if fprev == 1:
                        fprev = 0
                count += a
                flag += 1
            lenab -= 1
        
        if fprev == 1:
            return False
        if count == len(word):
            return True
        return False